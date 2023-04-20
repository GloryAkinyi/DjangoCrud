from django.db import models

# Create your models here.
class Student(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    email=models.EmailField()

    class Meta:
        db_table="student"
