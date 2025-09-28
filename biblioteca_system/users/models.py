from django.db import models
from django.core.validators import MinLengthValidator, EmailValidator

class users(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
