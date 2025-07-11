
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
from .models import Subject, Chapter, Topic, MCQ, ShortQuestion
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


logger = logging.getLogger(__name__)

def is_admin(user):
    return user.is_authenticated and user.is_staff

def process_mcq(text):
    """Process MCQ format questions from txt file"""
    questions = []
    current_question = None
    
    for line in text.split('\n'):
        line = line.strip()
        if not line:
            continue
            
        if line.startswith('Q.'):
            if current_question:
                questions.append(current_question)
            current_question = {
                'type': 'mcq',
                'question': line[2:].strip(),
                'options': [],
                'correct_answer': None,
                'explanation': None
            }
        elif current_question and line.startswith(('A)', 'B)', 'C)', 'D)')):
            current_question['options'].append(line[2:].strip())
        elif current_question and line.startswith('Answer :'):
            current_question['correct_answer'] = line[8:].strip()
        elif current_question and line.startswith('Explanation:'):
            current_question['explanation'] = line[12:].strip()
    
    if current_question:
        questions.append(current_question)
    
    return questions

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
            document = request.FILES.get('document')
            question_type = request.POST.get('question_type')
            subject_slug = request.POST.get('subject', '')
            grade = request.POST.get('grade', '')
            chapter_slug = request.POST.get('chapter', '')
            topic_slug = request.POST.get('topic', '')

            if not document:
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
                raise UnicodeDecodeError("Could not decode file with any supported encoding")


            # Process and save MCQs or Short Questions
            if question_type == 'mcq':
                questions = process_mcq(content)
            else:
                questions = process_short_question(content)

            with transaction.atomic():
                # Get or create subject
                subject, _ = Subject.objects.get_or_create(
                    slug=subject_slug,
                    defaults={'name': subject_slug.replace('-', ' ').title()}
                )
                # Get or create chapter
                chapter, _ = Chapter.objects.get_or_create(
                    subject=subject,
                    slug=chapter_slug,
                    grade=int(grade),
                    defaults={'name': chapter_slug.replace('-', ' ').title()}
                )
                # Get or create topic
                topic_name = topic_slug.replace('-', ' ').title()
                topic, created = Topic.objects.get_or_create(
                    chapter=chapter,
                    slug=topic_slug,
                    defaults={'name': topic_name}
                )
                
                # Log topic information
                logger.info(f"Topic {'created' if created else 'found'}: name='{topic.name}', slug='{topic.slug}'")
                if created:
                    logger.info("New topic created")

                if question_type == 'mcq':
                    mcqs_created = 0
                    logger.info(f"Topic: {topic.name}, Slug: {topic.slug}")
                    
                    for q in questions:
                        try:
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
                            logger.info(f"Created MCQ: {mcq.id} for topic: {topic.slug}")
                            mcqs_created += 1
                        except Exception as e:
                            logger.error(f"Error creating MCQ: {str(e)}")
                            raise
                            
                    context.update({
                        'success': True,
                        'message': f'Successfully uploaded and processed {mcqs_created} MCQ questions'
                    })
                else:
                    shorts_created = 0
                    for q in questions:
                        ShortQuestion.objects.create(
                            topic=topic,
                            question_text=q['question'],
                            answer=q['answer'],
                            marks=q.get('marks')
                        )
                        shorts_created += 1
                    context.update({
                        'success': True,
                        'message': f'Successfully uploaded and processed {shorts_created} Short Questions'
                    })

        except Exception as e:
            context['error'] = f'Error processing file: {str(e)}'
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
    grade_chapters = chapters_data.get(int(grade), [])  # Convert grade to int since it comes as string from URL
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

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .models import Subject, MCQ, ShortQuestion

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
    from django.db import connection
    import logging
    logger = logging.getLogger(__name__)
    
    # Get global data
    global_data = global_variables(request)
    
    # Get subject info
    subject_name = subject_slug.replace('-', ' ').title()
    subject = {
        'slug': subject_slug,
        'name': subject_name,
        'grade': grade
    }
    
    # Get chapter data
    chapters_data = global_data['chapters'].get(subject_slug.lower(), {})
    grade_chapters = chapters_data.get(int(grade), [])
    chapter = next((ch for ch in grade_chapters if ch['slug'] == chapter_slug), None)
    
    # Debug information
    logger.info(f"Looking for MCQs with: subject_slug={subject_slug}, grade={grade}, chapter_slug={chapter_slug}, topic={topic}")
    
    # First verify if the topic exists
    topic_exists = Topic.objects.filter(
        chapter__subject__slug=subject_slug,
        chapter__grade=grade,
        chapter__slug=chapter_slug,
        slug=topic
    ).exists()
    
    if not topic_exists:
        logger.warning(f"Topic not found with: subject_slug={subject_slug}, grade={grade}, chapter_slug={chapter_slug}, topic={topic}")
    
    # Get MCQs from database using the topic relationship
    # Convert topic to proper slug format
    topic_slug = topic  # topic comes from URL already in slug format
    
    # Debug query parameters
    logger.info(f"Query params: topic_slug={topic_slug}, topic_name={topic.replace('-', ' ')}")
    
    # Try to find MCQs
    mcqs = MCQ.objects.filter(
        topic__chapter__subject__slug=subject_slug,
        topic__chapter__grade=int(grade),  # Ensure grade is integer
        topic__chapter__slug=chapter_slug,
        topic__slug=topic_slug
    ).order_by('?')  # Random order
    
    # Debug the actual query
    logger.info(f"SQL Query: {mcqs.query}")
    
    # If no MCQs found, try to find the topic first to verify it exists
    if not mcqs.exists():
        topic_obj = Topic.objects.filter(
            chapter__subject__slug=subject_slug,
            chapter__grade=int(grade),
            chapter__slug=chapter_slug,
            slug=topic_slug
        ).first()
        if topic_obj:
            logger.info(f"Topic found: {topic_obj.name} (slug: {topic_obj.slug}) but no MCQs")
        else:
            logger.warning("Topic not found in database")
    
    # Log the query and count
    logger.info(f"MCQs found: {mcqs.count()}")
    logger.info(f"SQL Query: {mcqs.query}")
    
    # Check if we have any MCQs
    if not mcqs.exists():
        logger.warning("No MCQs found for this topic")
    
    context = {
        'subject': subject,
        'chapter': chapter,
        'topic': {
            'name': topic.replace('-', ' ').title(),  # Display name
            'slug': topic  # Original slug
        },
        'mcqs': mcqs,
        'grade': grade,
        'debug': settings.DEBUG,  # This will show debug info only in development
    }
    
    return render(request, 'pages/mcq_test.html', context)

@login_required
def short_questions_test(request, subject_slug, grade, chapter_slug, topic):
    # Get global data
    global_data = global_variables(request)
    
    # Get subject info
    subject_name = subject_slug.replace('-', ' ').title()
    subject = {
        'slug': subject_slug,
        'name': subject_name,
        'grade': grade
    }
    
    # Get chapter data
    chapters_data = global_data['chapters'].get(subject_slug.lower(), {})
    grade_chapters = chapters_data.get(int(grade), [])
    chapter = next((ch for ch in grade_chapters if ch['slug'] == chapter_slug), None)
    
    # Get Short Questions from database using the topic relationship
    short_questions = ShortQuestion.objects.filter(
        topic__chapter__subject__slug=subject_slug,
        topic__chapter__grade=grade,
        topic__chapter__slug=chapter_slug,
        topic__slug=topic
    ).order_by('?')  # Random order
    
    context = {
        'subject': subject,
        'chapter': chapter,
        'topic': topic.replace('-', ' '),
        'questions': short_questions,
        'grade': grade,
    }
    
    return render(request, 'pages/short_questions_test.html', context)

