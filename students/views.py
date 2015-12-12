#-*-coding: utf-8-*-
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from students.models import Student
from courses.models import Course
from django.core.exceptions import ObjectDoesNotExist
from students.forms import StudentModelForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class StudentDetailView(DetailView):
	model = Student
	
class StudentListView(ListView):
	model = Student
	paginate_by = 2

	def get_queryset(self):
		pk = self.request.GET.get('course_id', None)
		if pk:
			students = Student.objects.filter(courses__id=pk)
		else:
			students = Student.objects.all()
		return students


class StudentCreateView(CreateView):
	model = Student
	success_url = reverse_lazy('students:list_view')

	def get_context_data(self, **kwargs):
		context = super(StudentCreateView, self).get_context_data(**kwargs)
		context['title'] = u'Student registration'
		return context

	def form_valid(self, form):
		messages.success(self.request, u'Student %s %s has been successfully added.' 
						%(form.instance.name, form.instance.surname))
		return super(StudentCreateView, self).form_valid(form)
		

class StudentUpdateView(UpdateView):
	model = Student

	def get_success_url(self, **kwargs):
		return reverse_lazy('students:edit', args=(self.object.pk,))

	def get_context_data(self, **kwargs):
		context = super(StudentUpdateView, self).get_context_data(**kwargs)
		context['title'] = u'Student info update'
		return context

	def form_valid(self, form):
		messages.success(self.request, u'Info on the student has been sucessfully changed.')
		return super(StudentUpdateView, self).form_valid(form)

class StudentDeleteView(DeleteView):
	model = Student	
	success_url = reverse_lazy('students:list_view')

	def get_context_data(self, **kwargs):
		context = super(StudentDeleteView, self).get_context_data(**kwargs)
		context['title'] = u'Student info suppression'
		return context

	def form_valid(self, form):
		messages.success(self.request, u'Info on %s %s has been successfully deleted.' 
						%(self.object.name, self.object.surname))
		return super(StudentCreateView, self).form_valid(form)