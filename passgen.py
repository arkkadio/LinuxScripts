#!-*- conding: utf8 -*-

from random import randint
#from functions import *

def ArrayToString(x):
	temp_array = x
	temp_string = ""

	for i in temp_array:
		i = str(i)
		temp_string = temp_string + i
		
	return (temp_string)

def GeneratePassword():
	password = []
	chars = ("111111111111111111111111111111111111")
	c = 0

	while c < 10:
		n = randint(0,34)
		x = chars[n]
		a = password.append(x)
		c = c + 1	

password = []
chars = ("qwertyuiopçlkjhgfdsazxcvbnm123456789!@#$&")
c = 0

while c < 20:
	n = randint(0,39)
	x = chars[n]
	a = password.append(x)
	c = c + 1

print ("Sua senha: %s" %ArrayToString(password))
#print (PrintDateExt())



#"qwertyuiopçlkjhgfdsazxcvbnm123456789"