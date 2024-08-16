from django.db import models

class Student(models.Model):
    roll_number = models.CharField(max_length=20, unique=True)
    student_name = models.CharField(max_length=100)
    exam_name = models.CharField(max_length=100)
    sub1 = models.IntegerField(null=True, blank=True)
    sub2 = models.IntegerField(null=True, blank=True)
    sub3 = models.IntegerField(null=True, blank=True)
    sub4 = models.IntegerField(null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)
    result = models.CharField(max_length=50)
    mediam = models.CharField(max_length=50)
    exam_address = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=50)
    stud_address = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.student_name} ({self.roll_number})"
