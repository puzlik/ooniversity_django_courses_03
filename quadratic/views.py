#-*-coding: utf-8-*-
from django.shortcuts import render
from quadratic.forms import QuadraticForm

class Coefficient(object):
	
	def __init__(self, name, value):
		self.name = name
		self.value = value
		self.value_int = None
		self.error_message = None

	def is_valid(self):
		if not self.value:
			self.error_message = "коэффициент не определен"
			return False

		try:
			self.value_int = int(self.value)
		except ValueError:
			self.error_message = "коэффициент не целое число"
			return False

		if self.name == 'a' and self.value_int == 0:
			self.error_message = "коэффициент при первом слагаемом уравнения не может быть равным нулю"
			return False
		return True

def quadratic_results(request):
	context = {'error': False}
	for name_value in ['a', 'b', 'c']:
		coefficient = Coefficient(name_value, request.GET.get(name_value, ''))
		if coefficient.is_valid():
			context[name_value] = coefficient.value_int
		else:
			context['error'] = True
			context[name_value + '_error'] = coefficient.error_message
			context[name_value] = coefficient.value
	if not context['error']:
		a = context['a']
		b = context['b']
		c = context['c']

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
		return render(request, 'results.html', context)
	else:
		return render(request, 'results.html', context)
