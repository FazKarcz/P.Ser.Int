from django.db import models


class News(models.Model):
    """ News model"""
    title = models.CharField(max_length=35)  # Tytuł newsa
    date = models.DateField()  # Data newsa
    text = models.TextField(max_length=1500)  # Środek newsa

    def __str__(self):
        return f"{self.title}"