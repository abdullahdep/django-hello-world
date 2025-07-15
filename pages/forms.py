from django import forms
from .models import Subject, MCQ, ShortQuestion

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'slug']

class MCQForm(forms.ModelForm):
    class Meta:
        model = MCQ
        fields = ['question_text', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_answer', 'explanation', 'topic']

class ShortQuestionForm(forms.ModelForm):
    class Meta:
        model = ShortQuestion
        fields = ['question_text', 'answer', 'marks', 'topic']
