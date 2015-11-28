from django.shortcuts import render
from courses.models import Course, Lesson

from django.core.exceptions import ObjectDoesNotExist

def detail(request, pk):
	try:
		course_now = Course.objects.get(pk=pk)
		lessons = course_now.lesson_set.all()
		coaches = course_now.coach.user.get_full_name()
		assistants = course_now.assistant.user.get_full_name()
		num = course_now.coach.id
		return render(request, 'courses/detail.html', {
	    	"course_now": course_now,
	    	"lessons": lessons,
	    	"coaches": coaches,
	    	"assistants": assistants,
	    	"num": num, 
	    	})
	except ObjectDoesNotExist:
		message = "Sorry, no course with id = {0} exist yet.".format(pk) 
		return render(request, 'courses/detail.html', {
		    "message": message,
            })