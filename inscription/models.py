from django.db import models
from alumn.models import Alumn
from grade.models import Grade
from section.models import Section

class Inscription(models.Model):
    number = models.IntegerField()
    alumn = models.OneToOneField(Alumn, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.alumn)
# Create your models here.
