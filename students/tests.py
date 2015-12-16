from django.test import TestCase
from django.test import Client
from students.models import Student


class StudentsListTest(TestCase):


	def test_list(self):
		response = self.client.get('/students/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(Student.objects.all().count(),0)
		self.test_create()
		self.assertEqual(Student.objects.all().count(),1)

	def test_detail(self):
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
		self.assertContains(response, student1)

	def test_create(self):
		student1 = Student.objects.create(
								name='Student1-name',
								surname='Student1-surname',
								date_of_birth='2015-12-15',
								email='stud@pybursa.com',
								phone='777-77-77',
								address='Ukraine',
								skype='stud1')
		self.assertEqual(Student.objects.all().count(), 1)

	#def test_template(self):
	#	response1 = self.client.get('/students/')
	#	self.assertTemplateUsed(response1, 'students/student_list.html')
	#	
	#	response2 = self.client.get('/students/add/')
	#	self.assertTemplateUsed(response2, 'students/student_form.html')
	#	
	#	student1 = Student.objects.create(
	#							name='Student1-name',
	#							surname='Student1-surname',
	#							date_of_birth='2015-12-15',
	#							email='stud@pybursa.com',
	#							phone='777-77-77',
	#							address='Ukraine',
	#							skype='stud1')
	#	response3 = self.client.get('/students/1/')
	#	self.assertTemplateUsed(response3, 'students/student_detail.html')

		response4 = self.client.get('/students/edit/1/')
		self.assertTemplateUsed(response4, 'students/student_form.html')

		response5 = self.client.get('/students/remove/1/')
		self.assertTemplateUsed(response4, 'students/student_form.html')