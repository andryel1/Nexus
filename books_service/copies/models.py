from django.db import models

class Copy(models.Model):
    isbn = models.CharField(max_length=13)  # ISBN-13
    TYPE_CHOICES = [
        ('F', 'Físico'),
        ('D', 'Digital'),
    ]
    type = models.CharField(max_length=1, choices=TYPE_CHOICES, default='F')

    availability = models.BooleanField(default=True)  # True = disponível, False = não disponível

    book = models.ForeignKey(
        'Book',            # Nome da classe do model
        on_delete=models.CASCADE,
        related_name='copies'
    )

    def __str__(self):
        return f"Exemplar {self.isbn} ({'Disponível' if self.availability else 'Indisponível'})"
