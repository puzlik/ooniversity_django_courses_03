from django.shortcuts import render, render_to_response
from courses.models import Course
from django.template import RequestContext


def index(request):
	courses = Course.objects.all()
	return render(request, 'index.html', {
		"courses": courses,
		})

def contact(request):
	return render(request, 'contact.html')

def student_list(request):
	return render(request, 'student_list.html')

def student_detail(request):
	return render(request, 'student_detail.html')

def page_not_found(request):
    response = render_to_response('404.html', { 'message' : 'Sorry, page is not found' }, 
    							  context_instance=RequestContext(request))
    response.status_code = 404
    return response

def internal_error(request):
    response = render_to_response('500.html', { 'message' : 'Sorry, internal server error occurred' }, context_instance=RequestContext(request))
    response.status_code = 500
    return response