from django.db import models
from django.contrib.auth.models import User  # لربط الطالب بالمستخدم المسجل

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    price = models.FloatField(default = 0.0)
    edition = models.SmallIntegerField(default = 1)









    ############### lab 8

from django.db import models

class Address(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    




    ## lab 9


class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.IntegerField()

    def __str__(self):
        return f"{self.title} ({self.code})"


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name   

class Student2(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name


class Card(models.Model):
    student = models.OneToOneField(Student2, on_delete=models.PROTECT)
    card_number = models.CharField(max_length=20, unique=True)
    issue_date = models.DateField()

    def __str__(self):
        return f"{self.card_number} - {self.student.name}"
    









