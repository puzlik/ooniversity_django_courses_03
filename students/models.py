import datetime

from django.db import models

class Student(models.Model):
	name = models.CharField(max_length = 255)
	surname = models.CharField(max_length = 255)
	date_of_birth = models.DateField()
	email = models.EmailField()
	phone = models.CharField(max_length = 255)
	address = models.CharField(max_length = 255)
	skype = models.CharField(max_length = 255)
	courses = models.ManyToManyField('courses.Course')

	def __unicode__(self): 
		full_name = "%s %s" % (self.name, self.surname)
		return full_name
