from django.shortcuts import render
from globalvar import global_variables
from django.http import HttpResponse
# Create your views here.
def layouts(request):
    return render(request, 'layouts/layouts.html')
def home(request):
    pass
def subjects(request):
    pass
def premium(request):
    pass
def profile(request):
    pass
def contact(request):
    pass
def about(request):
    pass
def subject_detail(request):
    pass
def english(request):
    pass


def ads_txt(request):
    content = "google.com, pub-4959773968938981, DIRECT, f08c47fec0942fa0"
    return HttpResponse(content, content_type="text/plain")


def privacy_policy(request):
    return render(request, 'components\policites_and_terms\Privacy Policy.html')
def terms_and_conditions(request):
    return render(request, 'components\policites_and_terms\Terms And Conditions.html')
