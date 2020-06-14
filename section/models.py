from django.db import models

class Section(models.Model):
    section = models.CharField(max_length=25)
    jordanian = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.section
# Create your models here.
