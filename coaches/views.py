from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.detail import DetailView

class CoachDetailView(DetailView):
	model = Coach
	template_name = 'coaches/detail.html'
	context_object_name = 'coach'

	def get_context_data(self, **kwargs):
		coach = self.get_object()
		context = super(CoachDetailView, self).get_context_data(**kwargs)
		context['courses_coach'] = Course.objects.filter(coach=coach)
		context['courses_assistant'] = Course.objects.filter(assistant=coach)
		return context