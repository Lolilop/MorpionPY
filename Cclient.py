#!/usr/bin/env python3
import socket
import time

"""
									███╗░░░███╗░█████╗░██████╗░██████╗░██╗░█████╗░███╗░░██╗
									████╗░████║██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗████╗░██║
									██╔████╔██║██║░░██║██████╔╝██████╔╝██║██║░░██║██╔██╗██║
									██║╚██╔╝██║██║░░██║██╔══██╗██╔═══╝░██║██║░░██║██║╚████║
									██║░╚═╝░██║╚█████╔╝██║░░██║██║░░░░░██║╚█████╔╝██║░╚███║
									╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝


			 		 ██████ ██       █████  ███████ ███████      ██████ ██      ██ ███████ ███    ██ ████████ 
					██      ██      ██   ██ ██      ██          ██      ██      ██ ██      ████   ██    ██    
					██      ██      ███████ ███████ ███████     ██      ██      ██ █████   ██ ██  ██    ██    
					██      ██      ██   ██      ██      ██     ██      ██      ██ ██      ██  ██ ██    ██    
					 ██████ ███████ ██   ██ ███████ ███████      ██████ ███████ ██ ███████ ██   ████    ██  """

class Client() :

	"""
								██╗███╗   ██╗██╗████████╗██╗ █████╗ ████████╗███████╗██╗   ██╗██████╗ 
								██║████╗  ██║██║╚══██╔══╝██║██╔══██╗╚══██╔══╝██╔════╝██║   ██║██╔══██╗
								██║██╔██╗ ██║██║   ██║   ██║███████║   ██║   █████╗  ██║   ██║██████╔╝
								██║██║╚██╗██║██║   ██║   ██║██╔══██║   ██║   ██╔══╝  ██║   ██║██╔══██╗
								██║██║ ╚████║██║   ██║   ██║██║  ██║   ██║   ███████╗╚██████╔╝██║  ██║
								╚═╝╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝  ╚═╝
	"""

	def __init__(self) :

		hote , port = 'localhost' , 5009

		self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.__socket.connect((hote,port))

		self.__values = []

		self.__nb_strokes = 1
		self.__nb_StrokesMax = 9

		self.__continue = True

	"""
							 █████╗ ███████╗███████╗███████╗███████╗███████╗███████╗██╗   ██╗██████╗ ███████╗
							██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝██║   ██║██╔══██╗██╔════╝
							███████║███████╗███████╗█████╗  ███████╗███████╗█████╗  ██║   ██║██████╔╝███████╗
							██╔══██║╚════██║╚════██║██╔══╝  ╚════██║╚════██║██╔══╝  ██║   ██║██╔══██╗╚════██║
							██║  ██║███████║███████║███████╗███████║███████║███████╗╚██████╔╝██║  ██║███████║
							╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════
	"""

	def get_nb_strockes(self) :
		return self.__nb_strokes

	def get_nb_strockesMax(self):
		return self.__nb_StrokesMax

	def get_continue(self) : 
		return self.__continue

	"""
							███████╗ ██████╗ ███╗   ██╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗███████╗
							██╔════╝██╔═══██╗████╗  ██║██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝
							█████╗  ██║   ██║██╔██╗ ██║██║        ██║   ██║██║   ██║██╔██╗ ██║███████╗
							██╔══╝  ██║   ██║██║╚██╗██║██║        ██║   ██║██║   ██║██║╚██╗██║╚════██║
							██║     ╚██████╔╝██║ ╚████║╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║███████║
							╚═╝      ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
                                                
	"""

	def seedValue(self) :

		"""
		=========================================================================
		|						seend chose to the server			 			|
		=========================================================================
		"""

		user = input("> ")
		self.__values[int(user) - 1 ] = 'o'

		user = str(user)		
		user = user.encode()

		self.__socket.send(user)

	def recv(self) :

		"""
		=========================================================================
		|						get the array to the server 		 			|
		=========================================================================
		"""

		self.__continue = True
		tmp = self.__values
		self.__values = []

		message = ""

		while message != b"seend all" and message != 'break' :

			message = self.__socket.recv(1024)
			
			if(message == b"break") :
				
				message = self.translate(message)

				self.__values = tmp
				self.__socket.send(b"ok")

				self.__continue = False
				
			elif(message != b"seend all") :
				
				message = self.translate(message)
				self.__values.append(message)
					
		

	def translate(self,message) :

		"""
		=========================================================================
		|						cut the message with good format	 			|
		=========================================================================
		"""


		message = str(message)
		message = message.split("b'")
		message = message[1].split("'")
	
		return message[0]

	def recvNumber(self) :

		"""
		=========================================================================
		|								get why_win		 						|
		=========================================================================
		"""

		message = self.__socket.recv(1024)
		message = int(translate(message))
		
		if(message == 1) :
			print("l'adversaire a gagner")
		elif(message == 2) :
			print("vous-avez gagner")
		elif(message == 3) :
			print("vous avez gagner")

	def color(self) :

		"""
		=========================================================================
		|							ADD color on the array 						|
		=========================================================================
		"""
		
		for i in range(0,len(self.__values)) :
			if(self.__values[i] == 'x') :
				self.__values[i] = '\033[35m' + self.__values[i] + '\033[37m' 
			elif(self.__values[i] == 'o') :
				self.__values[i] = '\033[36m' + self.__values[i] + '\033[37m'



	def print_tic_tac_toe(self):

		"""
		=========================================================================
		|							Print array for the morpion					|
		=========================================================================
		"""

		print("\n")
		print("\t     |     |")
		print("\t  {}  |  {}  |  {}".format(self.__values[0], self.__values[1], self.__values[2]))
		print('\t_____|_____|_____')
		print("\t     |     |")
		print("\t  {}  |  {}  |  {}".format(self.__values[3], self.__values[4], self.__values[5]))
		print('\t_____|_____|_____')
		print("\t     |     |")
		print("\t  {}  |  {}  |  {}".format(self.__values[6], self.__values[7], self.__values[8]))
		print("\t     |     |")
		print("\n")

client = Client()


while client.get_nb_strockes() < client.get_nb_strockesMax() and client.get_continue():

	client.recv()

	client.color()
	client.print_tic_tac_toe()

	if(client.get_continue()) :
		client.seedValue()

	client.color()
	client.print_tic_tac_toe()



client.recvNumber()




