from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.files.storage import FileSystemStorage
from globalvar import global_variables
import json
import re

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
        question_type = request.POST.get('question_type')
        subject = request.POST.get('subject')
        grade = request.POST.get('grade')
        chapter = request.POST.get('chapter')
        topic = request.POST.get('topic')
        document = request.FILES.get('document')
        
        if not all([question_type, subject, grade, chapter, topic, document]):
            context['error'] = 'Please fill all fields and select a file'
            return render(request, 'admin_user/admin_user.html', context)
        
        try:
            # Read the txt file
            content = document.read().decode('utf-8')
            
            # Process questions based on type
            questions = []
            if question_type == 'mcq':
                questions = process_mcq(content)
            else:
                questions = process_short_question(content)
            
            # Save processed questions
            # Add your storage logic here
            
            context['success'] = True
            context['questions_processed'] = len(questions)
            return render(request, 'admin_user/admin_user.html', context)
            
        except Exception as e:
            context['error'] = str(e)
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

