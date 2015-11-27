from django.shortcuts import render
from students.models import Student
from courses.models import Course
from django.core.exceptions import ObjectDoesNotExist


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
