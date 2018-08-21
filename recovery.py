
import json  
import requests




def importarInstapaper():

	#leyendo configuracion
	try:
		with open("config.json") as fconfig:
			config = json.load(fconfig)
	except IOError:
		print "No se pudo leer el archivo de configuracion config.json"
		return

	#Pidiendo path del backup
	path = raw_input("Ingresa el path del archivo json a leer:\n")   

	#Leyendo archivo
	try:
		print "Leyendo archivo"
		with open(path) as f:
			data = json.load(f)
	except IOError:
		print "No se pudo leer el archivo especificado"
		return


	#Mostrando enlaces
	print "Leyendo data: \n Se han leido los siguientes enlaces:\n"
	for item in data:
		print item["url"]

	#Probando conexion
	print "\n Probando autenticacion de usuario....\n"
	r = requests.post("https://www.instapaper.com/api/authenticate",
		 params={"username":config["username"], "password":config["password"]})

	if(r.status_code == 200):
		print "Autenticacion con exito"
	else:
		print "No se pudo autenticar al usuario"
		return





	print "Realizando las inserciones"
	#Realizando inserciones
	for item in data:
		r = requests.post("https://www.instapaper.com/api/add",
			params={"username":config["username"], "password":config["password"], "url":item["url"]})
		if(r.status_code == 201):
			print "Se agrego el siguiente enlace: ", item["url"]
		else:
			print "No se pudo agregar el siguiente enlace:", item["url"]

	print "Realizado!"

importarInstapaper()
