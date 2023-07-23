from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=250)
    student_id = models.PositiveIntegerField()
    date_of_birth = models.DateField()
    gpa = models.PositiveIntegerField()
    gender = models.CharField(
        max_length=6,
        choices=[('Male', 'Male'), ('Female', 'Female')]
    )
    level = models.CharField(
        max_length=len('Level-1'),
        choices=[('Level-1', 'Level-1'), ('Level-2', 'Level-2'),
                 ('Level-3', 'Level-3'), ('Level-4', 'Level-4')]
    )
    active = models.CharField(
        max_length=len('InActive'),
        choices=[('Active', 'Active'), ('InActive', 'InActive')]
    )
    department = models.CharField(
        max_length=len("General"),
        choices=[('General', 'General'), ('IT', 'IT'), ('CS', 'CS'), ('AI', 'AI'),
                 ('DS', 'DS'), ('IS', 'IS')]
    )
    email = models.EmailField()
    mobile = models.CharField(max_length=len("01552452691"))
