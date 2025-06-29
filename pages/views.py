from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.files.storage import FileSystemStorage
from globalvar import global_variables
from django.conf import settings
from django.contrib import messages
import json
import re
import os
from datetime import datetime
from .models import Subject, Chapter, Topic, MCQ, Test, UserTestAttempt, UserAnswer
from django.db import transaction

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

            # Process questions
            if question_type == 'mcq':
                questions = process_mcq(content)
                
                # Save MCQs to database
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
                    topic, _ = Topic.objects.get_or_create(
                        chapter=chapter,
                        slug=topic_slug,
                        defaults={'name': topic_slug.replace('-', ' ').title()}
                    )
                    
                    # Create MCQs
                    mcqs_created = 0
                    for q in questions:
                        MCQ.objects.create(
                            topic=topic,
                            question_text=q['question'],
                            option_a=q['options'][0],
                            option_b=q['options'][1],
                            option_c=q['options'][2],
                            option_d=q['options'][3],
                            correct_answer=q['correct_answer'],
                            explanation=q.get('explanation')
                        )
                        mcqs_created += 1
                
                context.update({
                    'success': True,
                    'message': f'Successfully uploaded and processed {mcqs_created} MCQ questions'
                })
            else:
                # Handle short questions as before (file storage)
                # ...existing short question handling code...

                return render(request, 'admin_user/admin_user.html', context)

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
def chapter_detail(request, subject_slug, chapter_slug):
    # Get global data
    global_data = global_variables(request)
    
    # Get subject info
    subject_name = subject_slug.replace('-', ' ').title()
    subject = {
        'slug': subject_slug,
        'name': subject_name,
    }
    
    # Get chapter data
    chapters_data = global_data['chapters'].get(subject_slug.lower(), {})
    chapter = None
    
    # Find the chapter across all grades
    for grade_chapters in chapters_data.values():
        for ch in grade_chapters:
            if ch['slug'] == chapter_slug:
                chapter = ch
                break
        if chapter:
            break
    
    context = {
        'subject': subject,
        'chapter': chapter,
    }
    
    return render(request, 'chapter_detail.html', context)

@login_required
def test_view(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    
    # Check premium access
    if test.is_premium and not request.user.profile.is_premium:
        return render(request, 'test/premium_required.html')
    
    if request.method == 'POST':
        # Handle test submission
        data = json.loads(request.body)
        answers = data.get('answers', [])
        
        # Create test attempt
        attempt = UserTestAttempt.objects.create(
            user=request.user,
            test=test,
            score=calculate_score(answers)
        )
        
        # Save answers
        for answer in answers:
            if answer.get('type') == 'mcq':
                UserAnswer.objects.create(
                    attempt=attempt,
                    mcq_question_id=answer['questionId'],
                    selected_option_id=answer.get('selectedOptionId'),
                    is_correct=answer.get('isCorrect')
                )
            else:
                UserAnswer.objects.create(
                    attempt=attempt,
                    short_question_id=answer['questionId'],
                    uploaded_image=answer.get('uploadedImageUrl')
                )
        
        return JsonResponse({'success': True, 'score': attempt.score})
    
    context = {
        'test': test,
        'mcq_questions': test.mcq_questions.prefetch_related('options').all(),
        'short_questions': test.short_questions.all()
    }
    return render(request, 'test/test_view.html', context)

@login_required
def test_review(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    attempt = get_object_or_404(UserTestAttempt, user=request.user, test=test)
    
    context = {
        'test': test,
        'attempt': attempt,
        'answers': attempt.answers.select_related('mcq_question', 'short_question', 'selected_option').all()
    }
    return render(request, 'test/test_review.html', context)

@login_required
def mcq_test_view(request, topic_slug):
    # Get global data
    global_data = global_variables(request)
    
    # Find the topic and its MCQs
    topic_found = False
    topic_mcqs = []
    topic_name = topic_slug.replace('-', ' ').title()
    
    # Search through the chapters data structure
    for subject_slug, subject_chapters in global_data['chapters'].items():
        for grade, chapters in subject_chapters.items():
            for chapter in chapters:  # chapters is a list
                if 'topics' in chapter:
                    for topic in chapter['topics']:
                        if topic.lower() == topic_name.lower():
                            topic_found = True
                            # Get MCQs if they exist
                            if 'mcqs' in chapter:
                                topic_mcqs = [
                                    mcq for mcq in chapter['mcqs'] 
                                    if mcq.get('topic', '').lower() == topic_name.lower()
                                ]
                            break
                if topic_found:
                    break
            if topic_found:
                break
        if topic_found:
            break

    if not topic_found:
        messages.error(request, f"Topic '{topic_name}' not found")
        return redirect('home')

    context = {
        'topic': topic_name,
        'mcqs': topic_mcqs,
        'total_questions': len(topic_mcqs)
    }
    
    return render(request, 'test/mcq_test.html', context)

@login_required
def short_test_view(request, topic_slug):
    # Similar implementation for short questions
    pass


def html_sitemap(request):
    subjects = Subject.objects.all().prefetch_related('chapters__topics')
    return render(request, 'pages/html_sitemap.html', {'subjects': subjects})

