from datetime import *
from filter_html import *

def ArrayToString(x):
	temp_array = x
	temp_string = ""

	for i in temp_array:
		i = str(i)
		temp_string = temp_string + i
		
	return (temp_string)


def PrintDate():
	now = datetime.now()
	y = now.year
	m = now.month
	d = now.day
	now_show = ("%s/%s/%s" %(d,m,y))

	return now_show

def PrintDateExt():
	months = ["Janeiro","Fevereiro","Marco","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novebro","Dezembro"]

	now = datetime.now()
	y = now.year
	m = months[now.month-1]
	d = now.day

	now_show = ("%s de %s do ano de %s" %(d,m,y))

	return now_show

TextCleaner.tester('teste')
