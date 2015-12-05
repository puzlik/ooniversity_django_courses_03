#-*-coding: utf-8-*-
from django.shortcuts import render, redirect
from students.models import Student
from courses.models import Course
from django.core.exceptions import ObjectDoesNotExist
from students.forms import StudentModelForm
from django.contrib import messages


def detail(request, pk):
	student_by_id = Student.objects.get(id=pk)
	student_by_id.courses_id = Course.objects.filter(student=student_by_id)
	return render(request, 'students/detail.html', {
		"student_by_id": student_by_id,
		})
	

def list_view(request):
	try:
		pk = str(request.GET['course_id'])
		students = Student.objects.filter(courses=pk)
		i=1
		for student in students:
			student.courses_id = Course.objects.filter(student=student)
			student.id_l = i
			i=i+1
	except: 
		students = Student.objects.all()
		
		i=1
		for student in students:
			student.courses_id = Course.objects.filter(student=student)
			student.id_l = i
			i=i+1
	return render(request, 'students/list.html', {
			"students": students,
			})

def create(request):
	context = {}
	if request.method == 'POST': 
		form = StudentModelForm(request.POST)
		if form.is_valid():
			student_add = form.save()
			messages.success(request, 'Student %s %s has been successfully added.' %(student_add.name, student_add.surname))
			return redirect('students:list_view')
	else:
		context = {'form': StudentModelForm()}
	return render(request, 'students/add.html', context)

def edit(request, pk):
	student_by_id = Student.objects.get(id=pk)
	if request.method == 'POST':
		form = StudentModelForm(request.POST, instance=student_by_id)
		context = {'form': form}
		if form.is_valid:
			form.save()
			messages.success(request, 'Info on the student has been sucessfully changed.')
	else:
		context = {'form': StudentModelForm(instance=student_by_id)}
	return render(request, 'students/edit.html', context)

def remove(request, pk):
	student_by_id = Student.objects.get(id=pk)
	remove_message = "Student %s %s will be deleted" %(student_by_id.name, student_by_id.surname)
	if request.method == 'POST':
		student_by_id.delete()
		messages.success(request, "Info on %s %s has been successfully deleted." %(student_by_id.name, student_by_id.surname))
		return redirect('students:list_view')
	context = {'remove_message': remove_message}
	return render(request, 'students/remove.html', context)