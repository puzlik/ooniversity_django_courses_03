#-*-coding: utf-8-*-
from django.shortcuts import render
from quadratic.forms import QuadraticForm


def quadratic_results(request):
	if request.method == "GET":
		form = QuadraticForm(request.GET)
		context = {'form': form}
		if form.is_valid():
			a = int(form['a'].value())
			b = int(form['b'].value())
			c = int(form['c'].value())
			d = b * b - 4 * a * c
			if d < 0:
				d_text = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
			elif d == 0:
				x1 = - b / (2.0 * a)
				d_text = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = {0}".format(x1)
			else:
				x1 = (- b + d ** (1/2.0)) / (2 * a)
				x2 = (- b - d ** (1/2.0)) / (2 * a)
				d_text = "Квадратное уравнение имеет два действительных корня: x1 = {0}, x2 = {1}".format(x1, x2)
			context['d_text'] = d_text
			context['d'] = d
		elif form['a'].value() == form['b'].value() == form['c'].value() == None:
			context['form'] = QuadraticForm()
	return render(request, 'quadratic/results.html', context)