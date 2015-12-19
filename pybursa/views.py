from django.shortcuts import render
from courses.models import Course

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

def handler404(request):
    response = render_to_response('404.html')
    response.status_code = 404
    return response

def handler500(request):
    response = render_to_response('500.html')
    response.status_code = 500
    return response