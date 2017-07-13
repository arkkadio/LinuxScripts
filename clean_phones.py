#SCRIPT PARA LIMPEZA DE ARQUIVOS TXT CONTENDO UM TELEFONE POR LINHA
##OKAY#TODAS AS LETRAS SERAO REMOVIDAS 
#NUMEROS UNICIADOS DIFERENTE DE 8 OU 9 SERA MOVIDOS PARA OUTRO ARUIQVO CHAMADO FIXOS.TXT
#SERA ADICIONADO O 9 DIGITO PARA TELEFONES COM 8 DIGITOS
#SERA ADICIONADO O DDI ANTES DE TODOS OS NUMEROS EX.: 051

numeros = ["0","1","2","3","4","5","6","7","8","9"]
telefones = []
telefones2 = []
tel_files = open("telefones2.txt", "r")
file = tel_files.readlines()

init3 = '3'

def cleanphones():
	for line in file:

		for i in line:
			if i in numeros:
				pass
			else:
				line = line.replace(i, "")
		telefones.append(line)

def remove9_51(x):
	tel = x
	if len(tel) > 8:
		telinit = int(tel[0])
			
		if telinit == 5:
			tel = tel[2:]
		elif telinit == 9:
			tel = tel[1:]
		else:
			pass
	else:
		pass
	return (tel)

def inicial():
	
	for i in telefones:
		TelPrint = remove9_51(i)

		telefones2.append(TelPrint)

cleanphones()
inicial()

for i in telefones2:
	if len(i) == 9:
		print ("051" + i)
		pass
	elif len(i) < 8:
		pass
	elif i[0] == init3
		print ('fuck')
	else:
		print ("0519" + i )
		pass
	

