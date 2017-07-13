import os
from os import listdir
from os.path import isfile, join


download_foder = "C:\Users\gustavo.arejano\Downloads\\"
documents_folder = "C:\Users\gustavo.arejano\Documents\\" 
bakp_folder = "C:\bkp_folder\\"
shared_folder = "\\m07-ti-004\Suporte-Gustavo\\"
desktop = "C:\Users\gustavo.arejano\Desktop\\"

a = os.listdir(desktop)

for i in a:
	print (i)