# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test import Client
from courses.models import Course, Lesson
from coaches.models import Coach
from django.contrib.auth.models import User


class CoursesListTest(TestCase):

	def test_course_list(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
		
	def test_couse_list_update_count(self):
		response = self.client.get('/')
		self.assertEqual(Course.objects.all().count(),0)
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
		self.assertEqual(Course.objects.all().count(),1)

	def test_course_list_links(self):
		response = self.client.get('/')
		self.assertContains(response, 'Main')
		self.assertContains(response, 'Contacts')
		self.assertContains(response, 'Students')

	def test_course_list_template(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'index.html')

	def test_course_list_add_course_button(self):
		response = self.client.get('/')
		self.assertContains(response, 'Добавить новый курс')

class CoursesDetailTest(TestCase):
	def test_course_detail_status_code(self):
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

	def test_course_detail_template(self):
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
		self.assertTemplateUsed(response, 'courses/detail.html')

	def tes_course_detail_titles(self):
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
		self.assertContains(response, 'Преподаватели')
		self.assertContains(response, 'План курса')

	def test_course_detail_404(self):
		response = self.client.get('/courses/1/')
		self.assertEqual(response.status_code, 404)

	def test_course_detail_add_lesson_button(self):
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
		self.assertContains(response, 'Добавить занятие')

class CourseCreateTest(TestCase):
	def test_course_create(self):
		course1 = Course.objects.create(
						name='Course1-name',
						short_description='Short',
						description='description')
		self.assertEqual(Course.objects.all().count(), 1)


class CourseEditTest(TestCase):
	def test_course_edit(self):
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
		response = self.client.post('/courses/edit/1/', 
									  {'name': 'Course2-name', 
										'short_description': 'Short2',
										'description': 'description2',
										'coach': coach1,
										'assistant': coach1})
		response = self.client.get('/courses/edit/1/')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Course2')

	def test_add_template(self):	
		response = self.client.get('/courses/add/')
		self.assertTemplateUsed(response, 'courses/add.html')
		success_message = {'title': 'Course creation'}
		self.assertContains(response, success_message['title'])	


class LessonAddTest(TestCase):
	def test_add_lesson_template(self):
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
		response = self.client.get('/courses/1/add_lesson/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'courses/add_lesson.html')
		self.assertContains(response, 'Lesson creation')

	def test_add_lesson(self):
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
		self.assertEqual(Lesson.objects.all().count(), 0)
		lesson1 = Lesson.objects.create( 
						subject='Lesson1',
						description='Description',
						course=course1,
						order='1')
		response = self.client.get('/courses/1/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(Lesson.objects.all().count(), 1)