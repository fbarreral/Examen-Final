from django.db import models

class Grade(models.Model):
    nameGrade = models.CharField( max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nameGrade
# Create your models here.
