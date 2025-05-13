from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100)
    grade = models.CharField(max_length=2)
    email = models.EmailField(max_length=254)

    class Meta:
        db_table = 'auth_app_profile'
        
    def __str__(self):
        return self.user.username
