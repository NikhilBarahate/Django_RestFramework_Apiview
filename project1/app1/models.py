from django.db import models

# Create your models here.
class Teacher(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    salary = models.FloatField()

    def __str__(self):
        return self.name
