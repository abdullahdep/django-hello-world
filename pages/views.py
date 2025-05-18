from django.shortcuts import render
from globalvar import global_variables

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
            # Get chapters for selected grade from chapters data in globalvar
            chapters = global_data['chapters'].get(slug.lower(), {}).get(grade, [])
            print(f"Found {len(chapters)} chapters for grade {grade}")  # Debug output
        except (ValueError, TypeError):
            print(f"Invalid grade value: {selected_grade}")  # Debug output
    
    context = {
        'subject': subject,
        'selected_grade': selected_grade,
        'chapters': chapters,
        'grades': range(9, 13)  # Grades 9-12
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

