#-*-coding: utf-8-*-
from django.shortcuts import render

def quadratic_results(request):
	errors = list()
	flag_digits = list()

	def input_parameter(parameter_name = 'a'):
		p = str(request.GET[parameter_name])
		error_text = False
		if p.replace('-', '').isdigit():
			res = int(p)
			flag_digit = True
		elif len(p) == 0:
			res = p
			flag_digit = False
			error_text = "коэффициент не определен"
		else:
			res = p
			flag_digit = False
			error_text = "коэффициент не целое число"
		flag_digits.append(flag_digit)
		errors.append(error_text)
		return res

	coef_a = input_parameter('a')
	if str(request.GET['a']) == '0':
		flag_digits[0] = False
		errors[0] = "коэффициент при первом слагаемом уравнения не может быть равным нулю"
	coef_b = input_parameter('b')
	coef_c = input_parameter('c')

	if False not in flag_digits:
		a = int(coef_a)
		b = int(coef_b)
		c = int(coef_c)

		d = b * b - 4 * a * c
		if d < 0:
			d_text = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
			x1 = False
			x2 = False
		elif d == 0:
			x1 = - b / (2.0 * a)
			x2 = False
			d_text = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = {0}".format(x1)
		else:
			x1 = (- b + d ** (1/2.0)) / (2 * a)
			x2 = (- b - d ** (1/2.0)) / (2 * a)
			d_text = "Квадратное уравнение имеет два действительных корня: x1 = {0}, x2 = {1}".format(x1, x2)
		return render(request, 'results.html',{
			'value_a': a,
			'value_b': b,
			'value_c': c,
			'disc_eq': str(d),
			'disc_text': d_text,
			'first_root': x1,
			'second_root': x2,
			})
	else:
		return render(request, 'results.html',{
			'value_a': coef_a,
			'value_b': coef_b,
			'value_c': coef_c,
			'error_a': errors[0],
			'error_b': errors[1],
			'error_c': errors[2],
			})
