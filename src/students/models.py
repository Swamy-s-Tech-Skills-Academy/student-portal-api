from django.db import models


# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=10)
    age = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    batch = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.student_id}. {self.name}"
