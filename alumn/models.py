from django.db import models

class Alumn(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    adress = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
# Create your models here.
