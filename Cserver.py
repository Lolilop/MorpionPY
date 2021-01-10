# coding: utf-8

import socket
import time

class Server() :

	def __init__(self) :


		host , port = '' , 5005

		self.values = []

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creation socket IPV4 TCP

		self.sock.bind((host,port)) #associe le socket à une adresse locale
		self.sock.listen(5) #commence à écouter les connexions entrantes

		self.client , self.info = self.sock.accept() #accepte une connexion, retourne un nouveau socket et une adresse client

	def client(self) :

		continuer  = False

		while continuer == False :

			user = input("> ")
			user = int(user)

			if(self.values[user - 1] != 'o' or self.values[user - 1] != 'x' ) :

				self.values[user - 1] = 'x'
				continuer = True

	def receive(self) :

		message = str(self.client.recv(1024))
		message = message.split("b'")
		message = message[1]

		return message

	def seedValue(self,values) :

		for valeur in values :
		
			message = valeur.encode()
		
			self.client.send(message)
			time.sleep(0.0001)

			time.sleep(0.0001)
		self.client.send(b"seend all")


	def seedValueB(self) :

		message = ""
		
		while message != b"ok":

			self.client.send(b"break")
			message = self.client.recv(1024)

	def seedValueNum(self,partie) :

		game = str(partie.encode())
		self.client.send(game)

