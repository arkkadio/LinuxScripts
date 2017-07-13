

def GetCommand():
	a = input('Comando: ')	
	ValidCommand(a)


def ValidCommand(x):
	
	if x == '+':
		print ('soma')
	elif x == '-':
		print ('menos')


GetCommand()

