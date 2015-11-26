from django.shortcuts import render
from courses.models import Course, Lesson
from django.core.exceptions import ObjectDoesNotExist

def detail(request, pk):
	try:
		course_now = Course.objects.get(pk=pk)
		lessons = Lesson.objects.filter(course_id=pk)
		return render(request, 'courses/detail.html', {
	    	"course_now": course_now,
	    	"lessons": lessons,
	    	})
	except ObjectDoesNotExist:
		message = "Sorry, no course with id = {0} exist yet.".format(pk) 
		return render(request, 'courses/detail.html', {
		    "message": message,
            })