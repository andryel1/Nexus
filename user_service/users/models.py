from django.db import models

class user(models.Model):
    name = models.CharField(max_length= 50)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique= True)
    adress = models.CharField()
    