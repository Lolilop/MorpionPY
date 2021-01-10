# coding: utf-8

import socket
import Cserver


class TIC():
	"""docstring for TIC"""
	def __init__(self,serveur = None):

		self.nb_coups = 1

		self.nb_coupsMax = 9

		self.values = ["1","2","3","4","5","6","7","8","9"]

		self.partie = 0

		self.continuer = True
		
		self.combinaison = [
								[0,1,2],
								[3,4,5],
								[6,7,8],

								[0,3,6],
								[1,4,7],
								[2,5,8],

								[0,4,8],
								[2,4,6],

			  				]
		

		if(serveur != None) :
			self.liste = ["1","2","3","4","5","6","7","8","9"]

	def GUI(self) :

		print("""
			███╗░░░███╗░█████╗░██████╗░██████╗░██╗░█████╗░███╗░░██╗
			████╗░████║██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗████╗░██║
			██╔████╔██║██║░░██║██████╔╝██████╔╝██║██║░░██║██╔██╗██║
			██║╚██╔╝██║██║░░██║██╔══██╗██╔═══╝░██║██║░░██║██║╚████║
			██║░╚═╝░██║╚█████╔╝██║░░██║██║░░░░░██║╚█████╔╝██║░╚███║
			╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝\n\n""")

		print("1) Screen")
		print("2) Local")

		lan = input("> ")
		return int(lan)

	def comb(self,user,color,char) :

		continuer = True

		if(self.values[int(user)-1] != '\033[36m' + 'o' + '\033[37m' and self.values[int(user)-1] != '\033[35m' + 'x' + '\033[37m') :

			self.values[int(user)-1] = color + str(char) + '\033[37m'

			for i in range(len(self.combinaison)) :
				for j in range(len(self.combinaison[i])) :

					if(self.combinaison[i][j] == int(user)-1) :
						self.combinaison[i][j] = char

			continuer = False

		else :

			print("vous allez pas prendre la position de votre adversaire")

		return continuer

	def User(self,char,color) :

		continuer = True

		while continuer:
			user = input("> ")
			continuer = self.comb(user,color,char)


	def User_local(self,char,color) :

		continuer = True

		while continuer:
			user = input("> ")
			continuer = self.comb_local(user,color,char)

	def search(self) :

		self.print_tic_tac_toe()
		point = len(self.combinaison)
		i = 0

		while i < point and self.continuer:

			if(i < point and 'x' in self.combinaison[i] and 'o' in self.combinaison[i]) :			
			
				del self.combinaison[i]
				point = len(self.combinaison)
				i = i - 1

			elif(i < point and self.combinaison[i].count('x') > 2) :
			
				print("x win")
				self.continuer = False

			elif(i < point and self.combinaison[i].count('o') > 2) :
				print("o win")
				self.continuer = False

			else :

				i = i + 1

	def search_local(self) :


		self.print_tic_tac_toe()
		point = len(self.combinaison)
		i = 0

		while i < point and self.continuer:

			if(i < point and 'x' in self.combinaison[i] and 'o' in self.combinaison[i]) :			
			
				del self.combinaison[i]
				point = len(self.combinaison)
				i = i - 1

			elif(i < point and self.combinaison[i].count('x') > 2) :
			
				print("x win")
				self.continuer = False
				self.partie = 1

			elif(i < point and self.combinaison[i].count('o') > 2) :
				print("o win")
				self.continuer = False
				self.partie = 2

			else :

				i = i + 1


	def comb_local(self,user,color,char) :

		continuer = True

		if(self.values[int(user)-1] != '\033[36m' + 'o' + '\033[37m' and self.values[int(user)-1] != '\033[35m' + 'x' + '\033[37m') :

			self.values[int(user)-1] = color + str(char) + '\033[37m'
			self.liste[int(user)-1] = str(char) 

			for i in range(len(self.combinaison)) :
				for j in range(len(self.combinaison[i])) :

					if(self.combinaison[i][j] == int(user)-1) :
						self.combinaison[i][j] = char

			continuer = False

		else :

			print("vous allez pas prendre la position de votre adversaire")

		return continuer

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
































