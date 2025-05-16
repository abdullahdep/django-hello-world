from django.shortcuts import render, Http404
from django.utils.text import slugify
from globalvar import global_variables

# Create your views here.
def index(request):
    return render(request, 'index/index.html')
def premium(request):
    return render(request, 'premium/premium.html')
def upgrade_premium(request):
    pass
def subjects(request):
    return render(request, 'components/subject_list.html')
def subject_detail(request, subject_name):
    # Get subjects from global variables function
    subjects_data = global_variables(request)['subjects']
    
    # Convert slug back to subject name
    unslugified_name = subject_name.replace('-', ' ').title()
    
    # Get subject info
    subject_info = subjects_data.get(unslugified_name)
    
    if not subject_info:
        raise Http404("Subject not found")
        
    context = {
        'subject': {
            'name': unslugified_name,
            'description': subject_info['description'],
            'slug': subject_name,
        },
        'grades': range(9, 13),
        'selected_grade': request.GET.get('grade')
    }
    
    return render(request, 'subject_detail.html', context)

