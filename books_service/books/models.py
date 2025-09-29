from django.db import models

class books(models.Model):
    Title = models.CharField(max_length= 100, unique= True)
    pages = models.IntegerField()
    year = models.DateTimeField()
    bookedition = models.CharField()
    author = models.CharField(max_length=100)

    category = models.ForeignKey(
        'category',
        on_delete=models.CASCADE
                             )
    
    def __str__(self):
        return self.Title