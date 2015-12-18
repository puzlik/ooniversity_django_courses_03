from django.test import TestCase
from django.test import Client
from courses.models import Course, Lesson
from coaches.models import Coach
from django.contrib.auth.models import User


class CourseListTest(TestCase):

	def test_list(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(Course.objects.all().count(),0)
		self.test_create()
		self.assertEqual(Course.objects.all().count(),1)

	def test_detail(self):
		coach1 = Coach.objects.create(
								user=User.objects.create(),
								date_of_birth='2015-12-15',
								gender='M',
								phone='111-11-11',
								address='address',
								skype='skype',
								description = 'desc')
		course1 = Course.objects.create(
								name='Course1-name',
								short_description='Short',
								description='description',
								coach=coach1,
								assistant=coach1)
		response = self.client.get('/courses/1/')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Course1-name')

	def test_create(self):
		course1 = Course.objects.create(
								name='Course1-name',
								short_description='Short',
								description='description')
		self.assertEqual(Course.objects.all().count(), 1)

	def test_edit(self):
		coach1 = Coach.objects.create(
								user=User.objects.create(),
								date_of_birth='2015-12-15',
								gender='M',
								phone='111-11-11',
								address='address',
								skype='skype',
								description = 'desc')
		course1 = Course.objects.create(
								name='Course1-name',
								short_description='Short',
								description='description',
								coach=coach1,
								assistant=coach1)
		response = self.client.get('/courses/edit/1/')
		self.assertEqual(response.status_code, 200)


		response = self.client.post('/courses/edit/1/', {'name': 'Course2-name', 
														'short_description': 'Short2',
														'description': 'description2'})
		self.assertEqual(response.status_code, 302)

	#def test_add_lesson(self):
	#	coach1 = Coach.objects.create(
	#							user=User.objects.create(),
	#							date_of_birth='2015-12-15',
	#							gender='M',
	#							phone='111-11-11',
	#							address='address',
	#							skype='skype',
	#							description = 'desc')
	#	course1 = Course.objects.create(
	#							name='Course1-name',
	#							short_description='Short',
	#							description='description',
	#							coach=coach1,
	#							assistant=coach1)
	#	response = self.client.get('/courses/1/')
	#	lesson = Lesson.objects.all()
	#	self.assertEqual(self.lesson, 0)