from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from feedbacks.models import Feedback
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.core.mail import mail_admins


class FeedbackView(CreateView):
	model = Feedback
	template_name = 'feedbacks/feedback.html'
	success_url = reverse_lazy('feedback')
	context_object_name = 'feedback'

#	def get_context_data(self, **kwargs):
#		context = super(FeedbackView, self).get_context_data(**kwargs)
#		context['title'] = u'Leave feedback'
#		return context

	def form_valid(self, form):
		feedback_message = form.save()
		messages.success(self.request, u'Thank you for your feedback! We will keep in touch with you very soon!')
		mail_admins(feedback_message.subject, feedback_message.message)
		#email = EmailMessage(self.object.subject, self.object.message, self.object.from_email, ['admin@pybursa.com'])
		return super(FeedbackView, self).form_valid(form)
