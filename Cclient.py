import socket
import time

class Client() :

	def __init__(self) :

		hote , port = 'localhost' , 5005

		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.connect((hote,port))

		self.values = []


		self.nb_coups = 1
		self.nb_coupsMax = 9

		self.continuer = True

	def seedValue(self) :

	

		user = input("> ")
		self.values[int(user) - 1 ] = 'o'

		user = str(user)		
		user = user.encode()

		self.socket.send(user)

	def recv(self) :

		self.continuer = True
		temporaire = self.values
		self.values = []

		message = ""

		while message != b"seend all" and message != 'break' :

			message = self.socket.recv(1024)
			
			if(message == b"break") :
				
				message = self.translate(message)

				self.values = temporaire
				self.socket.send(b"ok")

				self.continuer = False
				
			elif(message != b"seend all") :
				
				message = self.translate(message)
				self.values.append(message)
					
		

	def translate(self,message) :

		message = str(message)
		message = message.split("b'")
		message = message[1].split("'")
	
		return message[0]

	def recvNumber(self) :

		message = self.socket.recv(1024)
		message = int(translate(message))
		
		if(message == 1) :
			print("l'adversaire a gagner")
		elif(message == 2) :
			print("vous-avez gagner")
		elif(message == 3) :
			print("vous avez gagner")

	def color(self) :
		
		for i in range(0,len(self.values)) :
			if(self.values[i] == 'x') :
				self.values[i] = '\033[35m' + self.values[i] + '\033[37m' 
			elif(self.values[i] == 'o') :
				self.values[i] = '\033[36m' + self.values[i] + '\033[37m'



	def print_tic_tac_toe(self):

		print("\n")
		print("\t     |     |")
		print("\t  {}  |  {}  |  {}".format(self.values[0], self.values[1], self.values[2]))
		print('\t_____|_____|_____')
		print("\t     |     |")
		print("\t  {}  |  {}  |  {}".format(self.values[3], self.values[4], self.values[5]))
		print('\t_____|_____|_____')
		print("\t     |     |")
		print("\t  {}  |  {}  |  {}".format(self.values[6], self.values[7], self.values[8]))
		print("\t     |     |")
		print("\n")

client = Client()


while client.nb_coups < client.nb_coupsMax and client.continuer:


	#print et get the date on values

	client.recv()


	client.color()
	client.print_tic_tac_toe()

	if(client.continuer) :
		client.seedValue()

	client.color()
	client.print_tic_tac_toe()



client.recvNumber()




