import datetime

from django.db import models

class Student(models.Model):
	name = models.CharField(max_length = 100)
	surname = models.CharField(max_length = 100)
	date_of_birth = models.DateField()
	email = models.EmailField()
	phone = models.CharField(max_length = 50)
	address = models.CharField(max_length = 100)
	skype = models.CharField(max_length = 50)
	courses = models.ManyToManyField('courses.Course')
