from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from courses.models import Course, Lesson
from django.core.exceptions import ObjectDoesNotExist
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

import logging
logger = logging.getLogger(__name__)


class CourseDetailView(DetailView):
	model = Course
	template_name = 'courses/detail.html'
	context_object_name = 'course_now'

	logger.debug("Courses detail view has been debugged")
	logger.info("Logger of courses detail view informs you!")
	logger.warning("Logger of courses detail view warns you!")
	logger.error("Courses detail view went wrong!")

class CourseCreateView(CreateView):
	model = Course
	template_name = 'courses/add.html'
	success_url = reverse_lazy('index')

	def get_context_data(self, **kwargs):
		context = super(CourseCreateView, self).get_context_data(**kwargs)
		context['title'] = u'Course creation'
		return context

	def form_valid(self, form):
		messages.success(self.request, u'Course %s has been successfully added.' %(form.instance.name))
		return super(CourseCreateView, self).form_valid(form)

class CourseUpdateView(UpdateView):
	model = Course
	template_name = 'courses/edit.html'
	context_object_name = 'form'

	def get_success_url(self, **kwargs):
		return reverse_lazy('courses:edit', args=(self.object.pk,))
	
	def get_context_data(self, **kwargs):
		context = super(CourseUpdateView, self).get_context_data(**kwargs)
		context['title'] = u'Course update'
		return context
	
	def form_valid(self, form):
		messages.success(self.request, u'The changes have been saved.') 
		return super(CourseUpdateView, self).form_valid(form)

class CourseDeleteView(DeleteView):
	model = Course	
	template_name = 'courses/remove.html'
	success_url = reverse_lazy('index')
	context_object_name = 'course'

	def get_context_data(self, **kwargs):
		context = super(CourseDeleteView, self).get_context_data(**kwargs)
		context['title'] = u'Course deletion'
		return context

	def delete(self, request, pk, *args, **kwargs):
		course = Course.objects.get(id=pk)
		messages.success(self.request, u'Course %s has been deleted.' %(course.name))
		return super(CourseDeleteView, self).delete(request, *args, **kwargs)


class LessonCreateView(CreateView):
	model = Lesson
	template_name = 'courses/add_lesson.html'
	print template_name
	context_object_name = 'form'

	def get_initial(self, **kwargs):
		initial = {'course': self.kwargs['pk']}
		return initial

	def get_success_url(self, **kwargs):
		return reverse_lazy('courses:detail', args=(self.kwargs['pk'],))

	def form_valid(self, form):
		messages.success(self.request, "Lesson %s has been successfully added." %(form.instance.subject))		
		return super(LessonCreateView, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(LessonCreateView, self).get_context_data(**kwargs)
		context['title'] = u'Lesson creation'
		return context