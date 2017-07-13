class TextCleaner(object):
	
		def __init__(x):
			my_file = x

			with open (my_file, "r") as f:
				texto = f.read()
				texto = texto.replace(' |','>')
				texto = texto.replace('"','')
				#texto = texto.replace(''','')
				texto = texto.split(">")
				ind = texto.index("<title id=pageTitle")

				#print (texto)
				#print (ind)
				print (texto[ind+1])

a = TextCleaner
a.__init__("texto_html.txt")