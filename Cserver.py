# coding: utf-8

import socket
import time

"""
									███╗░░░███╗░█████╗░██████╗░██████╗░██╗░█████╗░███╗░░██╗
									████╗░████║██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗████╗░██║
									██╔████╔██║██║░░██║██████╔╝██████╔╝██║██║░░██║██╔██╗██║
									██║╚██╔╝██║██║░░██║██╔══██╗██╔═══╝░██║██║░░██║██║╚████║
									██║░╚═╝░██║╚█████╔╝██║░░██║██║░░░░░██║╚█████╔╝██║░╚███║
									╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝


			 		 ██████ ██       █████  ███████ ███████     ███████ ███████ ██████  ██    ██ ███████ ██████      
					██      ██      ██   ██ ██      ██          ██      ██      ██   ██ ██    ██ ██      ██   ██     
					██      ██      ███████ ███████ ███████     ███████ █████   ██████  ██    ██ █████   ██████      
					██      ██      ██   ██      ██      ██          ██ ██      ██   ██  ██  ██  ██      ██   ██     
		             ██████ ███████ ██   ██ ███████ ███████     ███████ ███████ ██   ██   ████   ███████ ██   ██ """

class Server() :

	"""
								██╗███╗   ██╗██╗████████╗██╗ █████╗ ████████╗███████╗██╗   ██╗██████╗ 
								██║████╗  ██║██║╚══██╔══╝██║██╔══██╗╚══██╔══╝██╔════╝██║   ██║██╔══██╗
								██║██╔██╗ ██║██║   ██║   ██║███████║   ██║   █████╗  ██║   ██║██████╔╝
								██║██║╚██╗██║██║   ██║   ██║██╔══██║   ██║   ██╔══╝  ██║   ██║██╔══██╗
								██║██║ ╚████║██║   ██║   ██║██║  ██║   ██║   ███████╗╚██████╔╝██║  ██║
								╚═╝╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝  ╚═╝
	"""

	def __init__(self) :

		host , port = '' , 5009

		try :
			self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creation socket IPV4 TCP
			self.__socket.bind((host,port)) #associe le socket à une adresse locale
			self.__socket.listen(5) #commence à écouter les connexions entrantes
			self.__client , self.__info = self.__socket.accept() #accepte une connexion, retourne un nouveau socket et une adresse client
		except socket.error :
			self.__socket.close() #ferme la connexion
			exit()

	"""
							███████╗ ██████╗ ███╗   ██╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗███████╗
							██╔════╝██╔═══██╗████╗  ██║██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝
							█████╗  ██║   ██║██╔██╗ ██║██║        ██║   ██║██║   ██║██╔██╗ ██║███████╗
							██╔══╝  ██║   ██║██║╚██╗██║██║        ██║   ██║██║   ██║██║╚██╗██║╚════██║
							██║     ╚██████╔╝██║ ╚████║╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║███████║
							╚═╝      ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
                                                
	"""

	def receive(self) :

		"""
		=========================================================================
		|							get the data of the client	 				|
		=========================================================================
		"""

		try :
			message = str(self.__client.recv(1024))
		except socket.error:
			self.__socket.close()
			exit()

		message = message.split("b'")
		message = message[1]

		return message

	def seedValue(self,values) :

		"""
		=========================================================================
		|						seend the data of the client	 				|
		=========================================================================
		"""

		for valeur in values :
		
			message = valeur.encode()
		
			try :
				self.__client.send(message)
			except socket.error :
				self.__socket.close()
				exit()
			time.sleep(0.0001)

		try :
			self.__client.send(b"seend all")
		except socket.error :
			self.__socket.close()
			exit()


	def seedValueB(self) :

		"""
		=========================================================================
		|						seend the data of the client	 				|
		=========================================================================
		"""

		message = ""
		
		while message != b"ok":

			try :
				self.client.send(b"break")
				message = self.client.recv(1024)
			except socket.error :
				self.__socket.close()
				exit()

	def seedValueNum(self,partie) :

		"""
		=========================================================================
		|						seend the data of the why_win				|
		=========================================================================
		"""

		game = str(partie.encode())

		try :
			self.client.send(game)
		except :
			self.__socket.close()
			exit()

