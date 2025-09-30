from django.db import models

class Reservation(models.Model):
    date_start = models.DateField()
    date_end = models.DateField()
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Reservation from {self.date_start} to {self.date_end} - {self.status}"
