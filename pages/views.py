from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.core.files.storage import FileSystemStorage
from globalvar import global_variables
from django.conf import settings
from django.contrib import messages
from django.utils.text import slugify
from django.db import transaction
import json
import re
import os
from datetime import datetime
from .models import Subject, Chapter, Topic, MCQ, ShortQuestion, MCQTestScore
from django.db import transaction
from django.http import HttpResponse
from django.utils import timezone
from hashlib import sha256
import datetime
import random
import time  # Add this import
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import hashlib
import logging
from .models import Transaction  # Add this import at the top
from decimal import Decimal  # Add this at the top with other imports
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .models import Subject, MCQ, ShortQuestion
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Subject, Chapter, Topic, ShortQuestion

from PIL import Image
import pytesseract
import logging




logger = logging.getLogger(__name__)

def is_admin(user):
    return user.is_authenticated and user.is_staff

def process_mcq(text):
    """Process MCQ format questions from txt file"""
    questions = []
    current_question = None
    
    # Split the text into lines and remove empty lines
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    
    for line in lines:
        if line.startswith('Q.'):
            # If we have a previous question, save it if it's complete
            if current_question and len(current_question['options']) == 4 and current_question['correct_answer']:
                questions.append(current_question)
            
            # Start a new question
            current_question = {
                'question': line[2:].strip(),  # Remove 'Q.' prefix
                'options': [],
                'correct_answer': None,
                'explanation': None
            }
            
        elif current_question and (line.startswith('A)') or line.startswith('A.')):
            # Store option A
            current_question['options'] = [''] * 4  # Initialize with empty strings
            current_question['options'][0] = line[2:].strip() if line.startswith('A)') else line[3:].strip()
            
        elif current_question and (line.startswith('B)') or line.startswith('B.')):
            # Store option B
            if len(current_question['options']) < 4:
                current_question['options'] = [''] * 4
            current_question['options'][1] = line[2:].strip() if line.startswith('B)') else line[3:].strip()
            
        elif current_question and (line.startswith('C)') or line.startswith('C.')):
            # Store option C
            if len(current_question['options']) < 4:
                current_question['options'] = [''] * 4
            current_question['options'][2] = line[2:].strip() if line.startswith('C)') else line[3:].strip()
            
        elif current_question and (line.startswith('D)') or line.startswith('D.')):
            # Store option D
            if len(current_question['options']) < 4:
                current_question['options'] = [''] * 4
            current_question['options'][3] = line[2:].strip() if line.startswith('D)') else line[3:].strip()
            
        elif current_question and line.startswith('Answer :'):
            # Store the correct answer
            answer = line[8:].strip()  # Remove 'Answer : ' prefix
            if answer in ['A', 'B', 'C', 'D']:
                current_question['correct_answer'] = answer
            
        elif current_question and line.startswith('Explanation:'):
            # Store the explanation
            current_question['explanation'] = line[12:].strip()  # Remove 'Explanation:' prefix
    
    # Don't forget to add the last question if it's complete
    if current_question and len(current_question['options']) == 4 and current_question['correct_answer']:
        questions.append(current_question)
    
    # Validate all questions
    valid_questions = []
    for q in questions:
        if (len(q['options']) == 4 and 
            all(opt.strip() for opt in q['options']) and  # All options must have content
            q['correct_answer'] in ['A', 'B', 'C', 'D'] and 
            q['question'].strip()):  # Question must have content
            valid_questions.append(q)
        else:
            logger.warning(f"Invalid question found: {q['question'][:50]}...")
    
    logger.info(f"Processed {len(valid_questions)} valid MCQs out of {len(questions)} total questions")
    return valid_questions

def process_short_question(text):
    """Process short answer format questions from txt file"""
    questions = []
    current_question = None
    
    for line in text.split('\n'):
        line = line.strip()
        if not line:
            continue
            
        if line.startswith('Q.'):
            if current_question:
                questions.append(current_question)
            question_text = line[2:].strip()
            marks = None
            marks_match = re.search(r'\((\d+)\s*marks?\)', question_text)
            if marks_match:
                marks = int(marks_match.group(1))
                question_text = question_text.replace(marks_match.group(0), '').strip()
            
            current_question = {
                'type': 'short',
                'question': question_text,
                'answer': None,
                'marks': marks
            }
        elif current_question and line.startswith('Answer:'):
            current_question['answer'] = line[7:].strip()
    
    if current_question:
        questions.append(current_question)
    
    return questions

@user_passes_test(is_admin)
def admin_content_upload(request):
    import logging
    logger = logging.getLogger(__name__)
    
    global_data = global_variables(request)
    
    # Get subjects and grades from global data
    subjects_list = []
    for slug, data in global_data['subjects'].items():
        subjects_list.append({
            'slug': slug,
            'name': slug.replace('-', ' ').title(),
            'description': data.get('description', '')
        })
    
    # Get all available grades
    grades = sorted(set(
        grade
        for subject_chapters in global_data['chapters'].values()
        for grade in subject_chapters.keys()
    ))
    
    context = {
        'subjects': subjects_list,
        'grades': grades
    }
    
    if request.method == 'POST':
        try:
            # Get form data
            document = request.FILES.get('document')
            question_type = request.POST.get('question_type')
            subject_slug = request.POST.get('subject', '')
            grade = request.POST.get('grade', '')
            chapter_slug = request.POST.get('chapter', '')
            topic_slug = request.POST.get('topic', '')

            # Log received data
            logger.info(f"Received upload request - Subject: {subject_slug}, Grade: {grade}, "
                       f"Chapter: {chapter_slug}, Topic: {topic_slug}, Type: {question_type}")

            if not document:
                logger.error("No document uploaded")
                return render(request, 'admin_user/admin_user.html', 
                            {'error': 'Please select a file to upload', **context})

            # Read file content with different encodings
            content = None
            encodings = ['utf-8', 'utf-8-sig', 'latin-1', 'cp1252']
            
            for encoding in encodings:
                try:
                    content = document.read().decode(encoding)
                    document.seek(0)
                    break
                except UnicodeDecodeError:
                    document.seek(0)
                    continue

            if content is None:
                logger.error("Could not decode file with any supported encoding")
                raise UnicodeDecodeError("Could not decode file with any supported encoding")

            # Process the content
            if question_type == 'mcq':
                questions = process_mcq(content)
                logger.info(f"Processed {len(questions)} MCQ questions")
            else:
                questions = process_short_question(content)
                logger.info(f"Processed {len(questions)} Short questions")

            with transaction.atomic():
                # Create or get the subject
                subject_name = subject_slug.replace('-', ' ').title()
                subject, subject_created = Subject.objects.get_or_create(
                    slug=subject_slug,
                    defaults={'name': subject_name}
                )
                logger.info(f"Subject {'created' if subject_created else 'found'}: {subject.name}")

                # Create or get the chapter
                chapter_name = chapter_slug.replace('-', ' ').title()
                chapter, chapter_created = Chapter.objects.get_or_create(
                    subject=subject,
                    slug=chapter_slug,
                    grade=int(grade),
                    defaults={'name': chapter_name}
                )
                logger.info(f"Chapter {'created' if chapter_created else 'found'}: {chapter.name}")

                # Create or get the topic
                topic_name = topic_slug.replace('-', ' ').title()
                topic, topic_created = Topic.objects.get_or_create(
                    chapter=chapter,
                    slug=topic_slug,
                    defaults={'name': topic_name}
                )
                logger.info(f"Topic {'created' if topic_created else 'found'}: {topic.name}")

                if question_type == 'mcq':
                    mcqs_created = 0
                    for q in questions:
                        try:
                            # Validate MCQ data
                            if len(q['options']) != 4:
                                logger.error(f"Invalid number of options for question: {q['question'][:50]}...")
                                continue
                                
                            if q['correct_answer'] not in ['A', 'B', 'C', 'D']:
                                logger.error(f"Invalid correct answer for question: {q['question'][:50]}...")
                                continue

                            mcq = MCQ.objects.create(
                                topic=topic,
                                question_text=q['question'],
                                option_a=q['options'][0],
                                option_b=q['options'][1],
                                option_c=q['options'][2],
                                option_d=q['options'][3],
                                correct_answer=q['correct_answer'],
                                explanation=q.get('explanation')
                            )
                            logger.info(f"Created MCQ {mcq.id}: {mcq.question_text[:50]}...")
                            mcqs_created += 1
                        except Exception as e:
                            logger.error(f"Error creating MCQ: {str(e)}")
                            logger.error(f"Question data: {q}")
                            raise

                    message = f'Successfully uploaded and processed {mcqs_created} MCQ questions'
                    logger.info(message)
                    context.update({'success': True, 'message': message})
                else:
                    shorts_created = 0
                    for q in questions:
                        try:
                            short = ShortQuestion.objects.create(
                                topic=topic,
                                question_text=q['question'],
                                answer=q['answer'],
                                marks=q.get('marks')
                            )
                            logger.info(f"Created Short Question {short.id}: {short.question_text[:50]}...")
                            shorts_created += 1
                        except Exception as e:
                            logger.error(f"Error creating Short Question: {str(e)}")
                            logger.error(f"Question data: {q}")
                            raise

                    message = f'Successfully uploaded and processed {shorts_created} Short Questions'
                    logger.info(message)
                    context.update({'success': True, 'message': message})

        except Exception as e:
            error_message = f'Error processing file: {str(e)}'
            logger.error(error_message)
            context['error'] = error_message
            return render(request, 'admin_user/admin_user.html', context)

    return render(request, 'admin_user/admin_user.html', context)

@user_passes_test(is_admin)
@require_http_methods(["GET"])
def get_chapters(request, subject_slug):
    global_data = global_variables(request)
    chapters = []
    
    # Get chapters for the subject from global data
    subject_chapters = global_data['chapters'].get(subject_slug.lower(), {})
    
    for grade, grade_chapters in subject_chapters.items():
        for chapter in grade_chapters:
            chapters.append({
                'slug': chapter['slug'],
                'name': chapter['name'],
                'grade': grade
            })
    
    return JsonResponse(chapters, safe=False)

@user_passes_test(is_admin)
@require_http_methods(["GET"])
def get_topics(request, chapter_slug):
    global_data = global_variables(request)
    topics = []
    
    # Find the chapter and its topics in global data
    for subject_chapters in global_data['chapters'].values():
        for grade_chapters in subject_chapters.values():
            for chapter in grade_chapters:
                if chapter['slug'] == chapter_slug:
                    topics = [
                        {'slug': topic.lower().replace(' ', '-'), 'name': topic}
                        for topic in chapter.get('topics', [])
                    ]
                    break
    
    return JsonResponse(topics, safe=False)

@user_passes_test(is_admin)
@require_http_methods(["GET"])
def get_grade_chapters(request, subject_slug, grade):
    """Get chapters for a specific subject and grade"""
    try:
        global_data = global_variables(request)
        chapters = []
        
        # Get chapters for the subject and grade from global data
        subject_chapters = global_data['chapters'].get(subject_slug.lower(), {})
        grade_chapters = subject_chapters.get(int(grade), [])
        
        # Format chapters for response
        chapters = [
            {
                'slug': chapter['slug'],
                'name': chapter['name'],
                'topics': chapter.get('topics', [])
            }
            for chapter in grade_chapters
        ]
        
        return JsonResponse(chapters, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

def index(request):
    return render(request, 'index/index.html')
def premium(request):
    return render(request, 'premium/premium.html')
def upgrade_premium(request):
    pass
def subjects(request):
    return render(request, 'components/subject_list.html')
def subject_detail(request, slug):
    # Get global data
    global_data = global_variables(request)
    
    # Convert slug to subject name
    subject_name = slug.replace('-', ' ').title()
    
    # Get subject info
    subject = {
        'slug': slug,
        'name': subject_name,
        'description': global_data['subjects'].get(subject_name, {}).get('description', '')
    }
    
    selected_grade = request.GET.get('grade')
    chapters = []
    
    if selected_grade:
        try:
            grade = int(selected_grade)
            chapters = global_data['chapters'].get(slug.lower(), {}).get(grade, [])
        except (ValueError, TypeError):
            pass
    
    # Add chapters data as JSON for JavaScript
    chapters_json = json.dumps(global_data['chapters'].get(slug.lower(), {}))
    
    context = {
        'subject': subject,
        'selected_grade': selected_grade,
        'chapters': chapters,
        'chapters_json': chapters_json,
        'grades': range(9, 13)
    }
    
    return render(request, 'subject_detail.html', context)
def chapter_detail(request, subject_slug, grade, chapter_slug):
    # Get global data
    global_data = global_variables(request)
    
    # Get subject info
    subject_name = subject_slug.replace('-', ' ').title()
    subject = {
        'slug': subject_slug,
        'name': subject_name,
    }
    
    # Get chapter data for the specific grade
    chapters_data = global_data['chapters'].get(subject_slug.lower(), {})
    grade_chapters = chapters_data.get(int(grade), [])
    chapter = None
    
    # Find the chapter in the current grade
    for ch in grade_chapters:
        if ch['slug'] == chapter_slug:
            chapter = ch
            break
            
    context = {
        'subject': subject,
        'chapter': chapter,
        'grade': grade  # Pass the grade to the template
    }
    
    return render(request, 'chapter_detail.html', context)





def html_sitemap(request):
    subjects = Subject.objects.all().prefetch_related('chapters__topics')
    return render(request, 'pages/html_sitemap.html', {'subjects': subjects})


def is_admin(user):
    return user.is_superuser or user.is_staff

@user_passes_test(is_admin)
def manage_content(request):
    # Get filter parameters
    q_type = request.GET.get('type')
    subject = request.GET.get('subject')
    grade = request.GET.get('grade')
    
    # Start with all questions
    mcqs = MCQ.objects.all()
    short_questions = ShortQuestion.objects.all()
    
    # Apply filters
    if subject:
        mcqs = mcqs.filter(topic__chapter__subject__slug=subject)
        short_questions = short_questions.filter(topic__chapter__subject__slug=subject)
    
    if grade:
        mcqs = mcqs.filter(topic__chapter__grade=grade)
        short_questions = short_questions.filter(topic__chapter__grade=grade)
    
    # Combine or filter by type
    if q_type == 'mcq':
        questions = mcqs
    elif q_type == 'short':
        questions = short_questions
    else:
        # Combine both types if no specific type is selected
        questions = list(mcqs) + list(short_questions)
    
    context = {
        'questions': questions,
        'subjects': Subject.objects.all(),
        'grades': range(1, 13),  # Grades 1-12
        'current_type': q_type,
        'current_subject': subject,
        'current_grade': grade,
    }
    
    return render(request, 'admin_user/manage_content.html', context)

def generate_jazzcash_form(request):
    if not request.user.is_authenticated:
        messages.error(request, "Please login to make a payment")
        return redirect('login')

    try:
        price = "500"  # PKR 500 as per your premium plan
        bill_ref = f"BILL-{int(time.time())}"
        
        pp_Amount = price + "00"  # Amount in cents/paisa
        pp_BillReference = bill_ref
        pp_Description = "Safar Academy Premium Subscription"
        pp_Language = "EN"
        pp_MerchantID = settings.JAZZCASH_MERCHANT_ID
        pp_Password = settings.JAZZCASH_PASSWORD
        
        # Get current date and time
        pp_TxnDateTime = timezone.now().strftime('%Y%m%d%H%M%S')
        
        # Generate a unique transaction reference
        pp_TxnRefNo = f"T{pp_TxnDateTime}{random.randint(1,10000)}"

        # Make sure return URL is absolute and uses http
        pp_ReturnURL = 'http://127.0.0.1:8000/payment/callback/'
        
        # Prepare string to generate hash
        hash_string = (
            f"{pp_Amount}|"
            f"{pp_BillReference}|"
            f"{pp_Description}|"
            f"{pp_Language}|"
            f"{pp_MerchantID}|"
            f"{pp_Password}|"
            f"{pp_ReturnURL}|"
            f"{pp_TxnDateTime}|"
            f"{pp_TxnRefNo}|"
            f"1.1|"
            f"{settings.JAZZCASH_HASH_KEY}"
        )
        
        pp_SecureHash = sha256(hash_string.encode()).hexdigest()
        
        # Create transaction record
        transaction = Transaction.objects.create(
            user=request.user,
            transaction_ref=pp_TxnRefNo,
            amount=Decimal(price),
            bill_reference=pp_BillReference,
            status='pending'
        )
        
        context = {
            'pp_Amount': pp_Amount,
            'pp_BillReference': pp_BillReference,
            'pp_Description': pp_Description,
            'pp_Language': pp_Language,
            'pp_MerchantID': pp_MerchantID,
            'pp_Password': pp_Password,
            'pp_TxnDateTime': pp_TxnDateTime,
            'pp_TxnRefNo': pp_TxnRefNo,
            'pp_Version': "1.1",
            'pp_SecureHash': pp_SecureHash,
            'pp_ReturnURL': pp_ReturnURL,
            'pp_CustomerID': request.user.id,
            'pp_CustomerEmail': request.user.email,
            'JAZZCASH_API_URL': 'https://sandbox.jazzcash.com.pk/CustomerPortal/transactionmanagement/merchantform/'
        }
        
        # Debug logging
        print("JazzCash Parameters:")
        print(f"Return URL: {pp_ReturnURL}")
        print(f"API URL: {context['JAZZCASH_API_URL']}")
        print(f"MerchantID: {pp_MerchantID}")
        
        return render(request, 'premium/jazzcash-form.html', context)
        
    except Exception as e:
        logger.error(f"Error generating payment form: {str(e)}")
        messages.error(request, f"Error generating payment form: {str(e)}")
        return redirect('premium')

@csrf_exempt
def payment_callback(request):
    """Handle JazzCash payment callback"""
    if request.method == 'POST':
        try:
            # Get transaction details
            pp_ResponseCode = request.POST.get('pp_ResponseCode')
            pp_ResponseMessage = request.POST.get('pp_ResponseMessage')
            pp_TxnRefNo = request.POST.get('pp_TxnRefNo')
            
            # Log the callback data
            logger.info(f"Payment callback received: TxnRefNo={pp_TxnRefNo}, Response={pp_ResponseCode}")
            
            try:
                # Find the transaction
                transaction = Transaction.objects.get(transaction_ref=pp_TxnRefNo)
                
                if pp_ResponseCode == '000':
                    if not transaction.is_completed:
                        # Update transaction status
                        transaction.status = 'completed'
                        transaction.is_completed = True
                        transaction.completed_at = timezone.now()
                        transaction.response_code = pp_ResponseCode
                        transaction.response_message = pp_ResponseMessage
                        transaction.save()
                        
                        # Activate premium subscription
                        user = transaction.user
                        user_profile = user.userprofile  # Make sure you have a UserProfile model
                        user_profile.is_premium = True
                        user_profile.premium_until = timezone.now() + timezone.timedelta(days=30)
                        user_profile.save()
                        
                        logger.info(f"Payment completed successfully for transaction {pp_TxnRefNo}")
                        messages.success(request, "Payment successful! Your premium subscription is now active.")
                    else:
                        logger.warning(f"Transaction {pp_TxnRefNo} was already processed")
                else:
                    # Payment failed
                    transaction.status = 'failed'
                    transaction.response_code = pp_ResponseCode
                    transaction.response_message = pp_ResponseMessage
                    transaction.save()
                    logger.error(f"Payment failed for transaction {pp_TxnRefNo}: {pp_ResponseMessage}")
                    messages.error(request, f"Payment failed: {pp_ResponseMessage}")
                
            except Transaction.DoesNotExist:
                logger.error(f"Transaction not found: {pp_TxnRefNo}")
                return HttpResponse("Transaction not found", status=400)
                
            # Always return success to JazzCash
            return HttpResponse("OK")
            
        except Exception as e:
            logger.error(f"Error processing payment callback: {str(e)}")
            return HttpResponse("Error processing callback", status=500)
    
    return HttpResponse("Invalid request method", status=400)

@csrf_exempt
@require_POST
def jazzcash_ipn(request):
    """Handle JazzCash Instant Payment Notifications"""
    try:
        # Get the POST data
        pp_Amount = request.POST.get('pp_Amount')
        pp_ResponseCode = request.POST.get('pp_ResponseCode')
        pp_MerchantID = request.POST.get('pp_MerchantID')
        pp_SecureHash = request.POST.get('pp_SecureHash')
        pp_TxnRefNo = request.POST.get('pp_TxnRefNo')
        pp_BillReference = request.POST.get('pp_BillReference')

        # Log the IPN data for debugging
        logger.info(f"JazzCash IPN received: TxnRefNo={pp_TxnRefNo}, Amount={pp_Amount}, Response={pp_ResponseCode}")

        # Verify the merchant ID
        if pp_MerchantID != settings.JAZZCASH_MERCHANT_ID:
            logger.error(f"Invalid merchant ID: {pp_MerchantID}")
            return HttpResponse("Invalid merchant", status=400)

        # Reconstruct hash string for verification
        hash_string = (
            f"{pp_Amount}|"
            f"{pp_BillReference}|"
            f"{settings.JAZZCASH_MERCHANT_ID}|"
            f"{pp_TxnRefNo}|"
            f"{settings.JAZZCASH_HASH_KEY}"
        )
        
        calculated_hash = hashlib.sha256(hash_string.encode()).hexdigest()

        # Verify secure hash
        if calculated_hash != pp_SecureHash:
            logger.error("Hash verification failed")
            return HttpResponse("Hash verification failed", status=400)

        # Process the payment status
        if pp_ResponseCode == '000':
            # Payment successful
            try:
                # Find the transaction
                transaction = Transaction.objects.get(transaction_ref=pp_TxnRefNo)
                
                if not transaction.is_completed:
                    # Update transaction status
                    transaction.is_completed = True
                    transaction.status = 'completed'
                    transaction.completed_at = timezone.now()
                    transaction.save()

                    # Activate user's premium subscription
                    user = transaction.user
                    user_profile = user.userprofile
                    user_profile.is_premium = True
                    user_profile.premium_until = timezone.now() + timezone.timedelta(days=30)  # 30 days subscription
                    user_profile.save()

                    logger.info(f"Payment completed for transaction {pp_TxnRefNo}")
                else:
                    logger.warning(f"Transaction {pp_TxnRefNo} already processed")

            except Transaction.DoesNotExist:
                logger.error(f"Transaction not found: {pp_TxnRefNo}")
                return HttpResponse("Transaction not found", status=400)
            
        else:
            # Payment failed
            try:
                transaction = Transaction.objects.get(transaction_ref=pp_TxnRefNo)
                transaction.status = 'failed'
                transaction.save()
                logger.warning(f"Payment failed for transaction {pp_TxnRefNo}: {pp_ResponseCode}")
            except Transaction.DoesNotExist:
                logger.error(f"Transaction not found: {pp_TxnRefNo}")

        return HttpResponse("OK")

    except Exception as e:
        logger.error(f"Error processing IPN: {str(e)}")
        return HttpResponse("Error processing IPN", status=500)

@login_required
def mcq_test(request, subject_slug, grade, chapter_slug, topic):
    import logging
    logger = logging.getLogger(__name__)
    
    logger.info("Starting MCQ test view...")
    
    try:
        # Step 1: Get topic by name (convert URL slug to proper name)
        topic_name = topic.replace('-', ' ').title()
        logger.info(f"Looking for topic with name: {topic_name}")
        
        # Try to find the topic
        topic_obj = Topic.objects.filter(name=topic_name).first()
        
        if topic_obj:
            logger.info(f"Found topic: {topic_obj.name} (ID: {topic_obj.id})")
            logger.info(f"Topic's chapter ID: {topic_obj.chapter.id}")
            
            # Step 2: Get MCQs using the topic's chapter_id
            mcqs = MCQ.objects.filter(
                topic__chapter_id=topic_obj.chapter.id,
                topic__id=topic_obj.id
            ).order_by('?')
            
            logger.info(f"SQL Query for MCQs: {mcqs.query}")
            logger.info(f"Found {mcqs.count()} MCQs")
            
            # Get subject and chapter info for context
            subject = topic_obj.chapter.subject
            chapter = topic_obj.chapter
            
        else:
            logger.warning(f"No topic found with name: {topic_name}")
            mcqs = []
            subject = Subject.objects.filter(slug=subject_slug).first()
            if not subject:
                subject = Subject.objects.create(
                    name=subject_slug.replace('-', ' ').title(),
                    slug=subject_slug
                )
            chapter = Chapter.objects.filter(
                subject=subject,
                grade=int(grade),
                slug=chapter_slug
            ).first()

        submitted_answers = {}
        score = 0
        score_percentage = 0

        # Handle form submission
        if request.method == 'POST':
            total_questions = len(mcqs)
            for mcq in mcqs:
                answer_key = f'q{mcq.id}'
                user_answer = request.POST.get(answer_key)
                submitted_answers[mcq.id] = user_answer
                if user_answer == mcq.correct_answer:
                    score += 1
            
            score_percentage = (score / total_questions * 100) if total_questions > 0 else 0
            logger.info(f"Test submitted - Score: {score}/{total_questions} ({score_percentage}%)")
            
            # Store the score in MCQTestScore
            try:
                # Create answer details dictionary
                answer_details = {
                    str(mcq.id): {
                        'question': mcq.question_text,
                        'user_answer': submitted_answers.get(mcq.id),
                        'correct_answer': mcq.correct_answer,
                        'is_correct': submitted_answers.get(mcq.id) == mcq.correct_answer,
                        'options': {
                            'A': mcq.option_a,
                            'B': mcq.option_b,
                            'C': mcq.option_c,
                            'D': mcq.option_d
                        }
                    } for mcq in mcqs
                }
                
                # Save to MCQTestScore
                test_score = MCQTestScore.objects.create(
                    user=request.user,
                    subject=subject,
                    chapter=chapter,
                    topic=topic_obj,
                    score=score,
                    total_questions=total_questions,
                    score_percentage=score_percentage,
                    correct_answers=answer_details
                )
                logger.info(f"Score saved successfully for user {request.user.username} with ID {test_score.id}")
            except Exception as e:
                logger.error(f"Error saving score: {str(e)}")
    
    except Exception as e:
        logger.error(f"Error in mcq_test view: {str(e)}")
        mcqs = []
        subject = Subject.objects.get_or_create(
            slug=subject_slug,
            defaults={'name': subject_slug.replace('-', ' ').title()}
        )[0]
        chapter = None
        submitted_answers = {}
        score = 0
        score_percentage = 0
    
    context = {
        'subject': {
            'slug': subject.slug,
            'name': subject.name,
            'grade': grade
        },
        'chapter': {
            'slug': chapter.slug if chapter else chapter_slug,
            'name': chapter.name if chapter else chapter_slug.replace('-', ' ').title()
        },
        'topic': {
            'id': topic_obj.id if topic_obj else None,
            'name': topic_obj.name if topic_obj else topic_name,
            'slug': topic_obj.slug if topic_obj else topic,
            'chapter_id': topic_obj.chapter.id if topic_obj else None
        },
        'mcqs': mcqs,
        'grade': grade,
        'debug': True,  # Always show debug info while troubleshooting
        'submitted_answers': submitted_answers,
        'score': score,
        'score_percentage': round(score_percentage, 1),
        'debug_data': {
            'submitted_data': dict(request.POST) if request.method == 'POST' else None,
            'raw_answers': submitted_answers,
            'answer_details': [
                {
                    'question_id': str(mcq.id),  # Convert to string for consistency
                    'question': mcq.question_text,
                    'user_answer': submitted_answers.get(mcq.id),
                    'correct_answer': mcq.correct_answer,
                    'is_correct': submitted_answers.get(mcq.id) == mcq.correct_answer if mcq.id in submitted_answers else None
                } for mcq in mcqs
            ] if submitted_answers else []
        }
    }
    
    return render(request, 'pages/mcq_test.html', context)



# Optional: set path to tesseract if on Windows
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text(image_file):
    try:
        image = Image.open(image_file)
        return pytesseract.image_to_string(image).strip()
    except Exception as e:
        return f"[OCR Error: {str(e)}]"

@login_required
def short_question_test(request, subject_slug, grade, chapter_slug, topic):
    logger = logging.getLogger(__name__)
    logger.info("Starting Short Question test view...")

    try:
        topic_name = topic.replace('-', ' ').title()
        topic_obj = Topic.objects.filter(name=topic_name).first()

        if topic_obj:
            logger.info(f"Found topic: {topic_obj.name} (ID: {topic_obj.id})")
            short_questions = ShortQuestion.objects.filter(
                topic__chapter_id=topic_obj.chapter.id,
                topic__id=topic_obj.id
            )
            logger.info(f"Found {short_questions.count()} Short Questions")
            subject = topic_obj.chapter.subject
            chapter = topic_obj.chapter
        else:
            logger.warning(f"No topic found with name: {topic_name}")
            short_questions = []
            subject = Subject.objects.get_or_create(
                slug=subject_slug,
                defaults={'name': subject_slug.replace('-', ' ').title()}
            )[0]
            chapter = Chapter.objects.filter(
                subject=subject,
                grade=int(grade),
                slug=chapter_slug
            ).first()

        submitted_answers = {}

        if request.method == 'POST':
            for sq in short_questions:
                answer_key = f'q{sq.id}'
                image_key = f'img_q{sq.id}'

                user_answer = request.POST.get(answer_key, "").strip()
                image_file = request.FILES.get(image_key)

                # If answer is empty and image uploaded, use OCR
                if not user_answer and image_file:
                    ocr_text = extract_text(image_file)
                    submitted_answers[sq.id] = ocr_text
                    logger.info(f"OCR extracted for q{sq.id}: {ocr_text[:50]}...")
                else:
                    submitted_answers[sq.id] = user_answer

            logger.info(f"User submitted answers for {len(submitted_answers)} questions.")

    except Exception as e:
        logger.error(f"Error in short_question_test view: {str(e)}")
        short_questions = []
        submitted_answers = {}
        subject = Subject.objects.get_or_create(
            slug=subject_slug,
            defaults={'name': subject_slug.replace('-', ' ').title()}
        )[0]
        chapter = None

    context = {
        'subject': {
            'slug': subject.slug,
            'name': subject.name,
            'grade': grade
        },
        'chapter': {
            'slug': chapter.slug if chapter else chapter_slug,
            'name': chapter.name if chapter else chapter_slug.replace('-', ' ').title()
        },
        'topic': {
            'id': topic_obj.id if topic_obj else None,
            'name': topic_obj.name if topic_obj else topic_name,
            'slug': topic_obj.slug if topic_obj else topic,
            'chapter_id': topic_obj.chapter.id if topic_obj else None
        },
        'short_questions': short_questions,
        'submitted_answers': submitted_answers,
        'debug': True
    }

    return render(request, 'pages/short_question_test.html', context)

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse
from .models import Subject, Chapter, Topic, MCQ, ShortQuestion
from .forms import SubjectForm, MCQForm, ShortQuestionForm


def is_admin(user):
    return user.is_staff or user.is_superuser


@user_passes_test(is_admin)
def saved_content_list(request):
    subject_slug = request.GET.get("subject")
    grade = request.GET.get("grade")
    topic_id = request.GET.get("topic")

    # Dropdown data
    subjects = Subject.objects.all()
    chapters = Chapter.objects.all()
    topics = Topic.objects.all()

    # Base queryset
    mcqs = MCQ.objects.select_related("topic", "topic__chapter", "topic__chapter__subject")
    shorts = ShortQuestion.objects.select_related("topic", "topic__chapter", "topic__chapter__subject")

    # Filtering
    if subject_slug:
        mcqs = mcqs.filter(topic__chapter__subject__slug=subject_slug)
        shorts = shorts.filter(topic__chapter__subject__slug=subject_slug)
        chapters = chapters.filter(subject__slug=subject_slug)

    if grade:
        mcqs = mcqs.filter(topic__chapter__grade=grade)
        shorts = shorts.filter(topic__chapter__grade=grade)
        chapters = chapters.filter(grade=grade)

    if topic_id:
        mcqs = mcqs.filter(topic__id=topic_id)
        shorts = shorts.filter(topic__id=topic_id)

    # Handle POST
    if request.method == "POST":
        action = request.POST.get("action")
        obj_type = request.POST.get("type")
        obj_id = request.POST.get("id")

        # ✅ Bulk save all changes
        if action == "bulk_save":
            # Update MCQs
            mcq_ids = request.POST.getlist("mcq_ids")
            for mid in mcq_ids:
                try:
                    mcq = MCQ.objects.get(id=mid)
                    mcq.question_text = request.POST.get(f"mcq_{mid}_question_text", mcq.question_text)
                    mcq.option_a = request.POST.get(f"mcq_{mid}_option_a", mcq.option_a)
                    mcq.option_b = request.POST.get(f"mcq_{mid}_option_b", mcq.option_b)
                    mcq.option_c = request.POST.get(f"mcq_{mid}_option_c", mcq.option_c)
                    mcq.option_d = request.POST.get(f"mcq_{mid}_option_d", mcq.option_d)
                    mcq.correct_answer = request.POST.get(f"mcq_{mid}_correct_answer", mcq.correct_answer)
                    mcq.explanation = request.POST.get(f"mcq_{mid}_explanation", mcq.explanation)
                    mcq.save()
                except MCQ.DoesNotExist:
                    pass

            # Update Shorts
            short_ids = request.POST.getlist("short_ids")
            for sid in short_ids:
                try:
                    sq = ShortQuestion.objects.get(id=sid)
                    sq.question_text = request.POST.get(f"short_{sid}_question_text", sq.question_text)
                    sq.answer = request.POST.get(f"short_{sid}_answer", sq.answer)
                    sq.marks = request.POST.get(f"short_{sid}_marks") or None
                    sq.save()
                except ShortQuestion.DoesNotExist:
                    pass

            return redirect(reverse("saved_content_list"))

        # ✅ Handle single delete
        elif action == "delete":
            if obj_type == "mcq":
                mcq = get_object_or_404(MCQ, id=obj_id)
                mcq.delete()
            elif obj_type == "short":
                short = get_object_or_404(ShortQuestion, id=obj_id)
                short.delete()
            return redirect(reverse("saved_content_list"))

        # ✅ Handle single update
        elif action == "edit":
            if obj_type == "mcq":
                mcq = get_object_or_404(MCQ, id=obj_id)
                mcq.question_text = request.POST.get("question_text")
                mcq.option_a = request.POST.get("option_a")
                mcq.option_b = request.POST.get("option_b")
                mcq.option_c = request.POST.get("option_c")
                mcq.option_d = request.POST.get("option_d")
                mcq.correct_answer = request.POST.get("correct_answer")
                mcq.explanation = request.POST.get("explanation")
                mcq.save()
            elif obj_type == "short":
                short = get_object_or_404(ShortQuestion, id=obj_id)
                short.question_text = request.POST.get("question_text")
                short.answer = request.POST.get("answer")
                short.marks = request.POST.get("marks") or None
                short.save()
            return redirect(reverse("saved_content_list"))

    context = {
        "subjects": subjects,
        "chapters": chapters,
        "topics": topics,
        "selected_subject": subject_slug,
        "selected_grade": grade,
        "selected_topic": topic_id,
        "mcqs": mcqs,
        "short_questions": shorts,
    }
    return render(request, "admin_user/saved_content_list.html", context)


@user_passes_test(is_admin)
def subject_create(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('saved_content_list')
    else:
        form = SubjectForm()
    return render(request, 'admin_user/form.html', {'form': form, 'title': 'Add Subject'})


@user_passes_test(is_admin)
def mcq_create(request):
    if request.method == 'POST':
        form = MCQForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('saved_content_list')
    else:
        form = MCQForm()
    return render(request, 'admin_user/form.html', {'form': form, 'title': 'Add MCQ'})


@user_passes_test(is_admin)
def shortquestion_create(request):
    if request.method == 'POST':
        form = ShortQuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('saved_content_list')
    else:
        form = ShortQuestionForm()
    return render(request, 'admin_user/form.html', {'form': form, 'title': 'Add Short Question'})


# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import MCQTestScore, Subject

@login_required
def mcq_dashboard(request):
    user = request.user
    subjects = Subject.objects.all()

    subject_data = []
    for subject in subjects:
        scores = MCQTestScore.objects.filter(user=user, subject=subject).order_by('-created_at')
        if scores.exists():
            total_attempts = scores.count()
            average_score = sum(score.score_percentage for score in scores) / total_attempts
        else:
            total_attempts = 0
            average_score = 0

        subject_data.append({
            'subject': subject,
            'scores': scores,
            'average_score': round(average_score, 2),
            'total_attempts': total_attempts
        })

    return render(request, 'dashboard/mcq_dashboard.html', {
        'subject_data': subject_data
    })
