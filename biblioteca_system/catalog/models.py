from django.db import models

class catalog(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length= 100)
    creat_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name