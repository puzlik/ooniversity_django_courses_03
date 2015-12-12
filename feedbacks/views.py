from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from feedbacks.models import Feedback
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.core.mail import mail_admins


class FeedbackView(CreateView):
	model = Feedback
	template_name = 'feedback.html'
	success_url = reverse_lazy('feedback')
	context_object_name = 'form'

	def get_context_data(self, **kwargs):
		context = super(FeedbackView, self).get_context_data(**kwargs)
		context['title'] = u'Leave feedback'
		return context

	def form_valid(self, form):
		
		mail_admins(form.instance.subject, form.instance.message)

		#email = EmailMessage(form.instance.subject, form.instance.message, form.instance.from_email, ['admin@pybursa.com'])
		messages.success(self.request, u'Thank you for your feedback! We will keep in touch with you very soon!')
		return super(FeedbackView, self).form_valid(form)