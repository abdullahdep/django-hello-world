from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Chapter(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='chapters')
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    grade = models.IntegerField()

    class Meta:
        unique_together = ['subject', 'slug']

    def __str__(self):
        return f"{self.subject.name} - {self.name} (Grade {self.grade})"

class Topic(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='topics')
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    class Meta:
        unique_together = ['chapter', 'slug']

    def __str__(self):
        return self.name

class MCQ(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='mcqs')
    question_text = models.TextField()
    option_a = models.CharField(max_length=500)
    option_b = models.CharField(max_length=500)
    option_c = models.CharField(max_length=500)
    option_d = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=1, choices=[
        ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')
    ])
    explanation = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"MCQ: {self.question_text[:50]}..."

# class Test(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField(blank=True)
#     duration = models.IntegerField(help_text="Duration in seconds")
#     is_premium = models.BooleanField(default=False)
#     subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
#     chapter = models.ForeignKey('Chapter', on_delete=models.CASCADE)
#     topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)

# class MCQQuestion(models.Model):
#     test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='mcq_questions')
#     text = models.TextField()
#     explanation = models.TextField(blank=True)

# class MCQOption(models.Model):
#     question = models.ForeignKey(MCQQuestion, on_delete=models.CASCADE, related_name='options')
#     text = models.CharField(max_length=500)
#     is_correct = models.BooleanField(default=False)

# class ShortQuestion(models.Model):
#     test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='short_questions')
#     text = models.TextField()
#     marks = models.IntegerField()
#     answer = models.TextField()

# class UserTestAttempt(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     test = models.ForeignKey(Test, on_delete=models.CASCADE)
#     score = models.FloatField()
#     completed_at = models.DateTimeField(auto_now_add=True)

# class UserAnswer(models.Model):
#     attempt = models.ForeignKey(UserTestAttempt, on_delete=models.CASCADE, related_name='answers')
#     mcq_question = models.ForeignKey(MCQQuestion, on_delete=models.CASCADE, null=True, blank=True)
#     short_question = models.ForeignKey(ShortQuestion, on_delete=models.CASCADE, null=True, blank=True)
#     selected_option = models.ForeignKey(MCQOption, on_delete=models.CASCADE, null=True, blank=True)
#     uploaded_image = models.ImageField(upload_to='answers/', null=True, blank=True)
#     is_correct = models.BooleanField(null=True, blank=True)