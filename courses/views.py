from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from django.core.exceptions import ObjectDoesNotExist
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages


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

def add(request):
	context = {}
	if request.method == 'POST': 
		form = CourseModelForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			course_add = form.save()
			messages.success(request, "Course %s has been successfully added." %(course_add.name))
			return redirect('index')
	else:
		form = CourseModelForm()
	context = {'form': form}
	return render(request, 'courses/add.html', context)

def edit(request, pk):
	course_by_id = Course.objects.get(id=pk)
	if request.method == 'POST':
		form = CourseModelForm(request.POST, instance=course_by_id)
		if form.is_valid:
			form.save()
			messages.success(request, "The changes have been saved.")
			return redirect('courses:edit', pk)
	else:
		form = CourseModelForm(instance=course_by_id)
	context = {'form': form}
	return render(request, 'courses/edit.html', context)

def remove(request, pk):
	course_by_id = Course.objects.get(id=pk)
	remove_message = "Course %s will be deleted" %(course_by_id.name)
	if request.method == 'POST':
		course_by_id.delete()
		messages.success(request, "Course %s has been deleted." %(course_by_id.name))
		return redirect('index')
	context = {'remove_message': remove_message}
	return render(request, 'courses/remove.html', context)

def add_lesson(request, pk):
	context = {}
	#course = Course.objects.get(id=pk)
	#lesson = LessonModelForm(id=pk)
	if request.method == 'POST': 
		form = LessonModelForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			lesson_add = form.save()
			messages.success(request, "Lesson %s has been successfully added." %(lesson_add.subject))
			return redirect('courses:detail', pk)
		else:
			messages.warning(request, "Attention!!! Wrong data in the form fields!!!")
	else:
		form = LessonModelForm(initial={'course': pk})
	context = {'form': form}
	return render(request, 'courses/add_lesson.html', context)