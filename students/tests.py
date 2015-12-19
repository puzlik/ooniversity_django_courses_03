# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test import Client
from students.models import Student


class StudentsListTest(TestCase):
	def test_student_list(self):
		response = self.client.get('/students/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(Student.objects.all().count(),0)
		student1 = Student.objects.create(
								name='Student1-name',
								surname='Student1-surname',
								date_of_birth='2015-12-15',
								email='stud@pybursa.com',
								phone='777-77-77',
								address='Ukraine',
								skype='stud1')
		self.assertEqual(Student.objects.all().count(),1)
	def test_list_template(self):
		response = self.client.get('/students/')
		self.assertTemplateUsed(response, 'students/student_list.html')
	def test_list_button(self):	
		response = self.client.get('/students/')
		success_message = {'add': u'Добавить нового студента'}
		self.assertContains(response, success_message['add'])
	def test_list_title(self):
		response = self.client.get('/students/')
		self.assertContains(response, 'Список студентов')
	def test_list_edit_button(self):
		response = self.client.get('/students/')
		self.assertContains(response, 'изменить')
	def test_list_delete_button(self):
		response = self.client.get('/students/')
		self.assertContains(response, 'удалить')


class StudentsDetailTest(TestCase):
	def test_student_detail_status_code(self):
		student1 = Student.objects.create(
								name='Student1-name',
								surname='Student1-surname',
								date_of_birth='2015-12-15',
								email='stud@pybursa.com',
								phone='777-77-77',
								address='Ukraine',
								skype='stud1')
		response = self.client.get('/students/1/')
		self.assertEqual(response.status_code, 200)
	def test_student_detail_template(self):
		student1 = Student.objects.create(
								name='Student1-name',
								surname='Student1-surname',
								date_of_birth='2015-12-15',
								email='stud@pybursa.com',
								phone='777-77-77',
								address='Ukraine',
								skype='stud1')
		response = self.client.get('/students/1/')
		self.assertTemplateUsed(response, 'students/student_detail.html')
	def test_student_detail_404(self):
		response = self.client.get('/students/1/')
		self.assertEqual(response.status_code, 404)
	def test_student_detail_fields(self):
		student1 = Student.objects.create(
								name='Student1-name',
								surname='Student1-surname',
								date_of_birth='2015-12-15',
								email='stud@pybursa.com',
								phone='777-77-77',
								address='Ukraine',
								skype='stud1')
		response = self.client.get('/students/1/')
		self.assertContains(response, 'курсы')
		self.assertContains(response, 'email')
		self.assertContains(response, 'адрес')
	def test_student_detail_links(self):
		student1 = Student.objects.create(
								name='Student1-name',
								surname='Student1-surname',
								date_of_birth='2015-12-15',
								email='stud@pybursa.com',
								phone='777-77-77',
								address='Ukraine',
								skype='stud1')
		response = self.client.get('/students/1/')
		self.assertContains(response, 'Main')
		self.assertContains(response, 'Contacts')
		self.assertContains(response, 'Students')

class StudentsCreateTest(TestCase):
	def test_student_create(self):
		response = self.client.get('/students/add/')
		self.assertEqual(response.status_code, 200)
		response = self.client.post('/students/add/', 
									{'name': 'Student1-name',
									'surname': 'Student1-surname',
									'date_of_birth': '2015-12-15',
									'email': 'stud@pybursa.com',
									'phone': '777-77-77',
									'address': 'Ukraine',
									'skype': 'stud1'},
									follow=True)
		self.assertEqual(response.status_code, 200)

class StudentDeleteTest(TestCase):
	def test_student_delete(self):
		student1 = Student.objects.create(
								name='Student1-name',
								surname='Student1-surname',
								date_of_birth='2015-12-15',
								email='stud@pybursa.com',
								phone='777-77-77',
								address='Ukraine',
								skype='stud1')		
		response = self.client.get('/students/remove/1/')
		self.assertEqual(response.status_code, 200)
		success_message = {'del': 'Удалить'}
		self.assertContains(response, success_message['del'])
	
class StudentEditTest(TestCase):
	def test_edit(self):
		student1 = Student.objects.create(
								name='Student1-name',
								surname='Student1-surname',
								date_of_birth='2015-12-15',
								email='stud@pybursa.com',
								phone='777-77-77',
								address='Ukraine',
								skype='stud1')
		response = self.client.get('/students/edit/1/')
		self.assertEqual(response.status_code, 200)
		response = self.client.post('/students/edit/1/', 
									{'name': 'Student2-name',
									'surname': 'Student2-surname',
									'date_of_birth': '2015-12-15',
									'email': 'stud@pybursa.com',
									'phone': '777-77-77',
									'address': 'Ukraine',
									'skype': 'stud1'},
									follow=True)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Student2')

class StudentTemplateTest(TestCase):

		
	def test_add_template(self):	
		response = self.client.get('/students/add/')
		self.assertTemplateUsed(response, 'students/student_form.html')
		success_message = {'title': 'Student registration'}
		self.assertContains(response, success_message['title'])