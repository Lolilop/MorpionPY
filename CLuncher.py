#!/usr/bin/env python3

import Cserver
import CToc


class Luncher():

	def __init__(self) :
		self.lan = 0
		self.server = None
		self.morpion = None

	def get_lan(self) :
		return self.lan 

	def GUI(self) :

		"""
		=========================================================================
		|							Interface for the user 		 				|
		=========================================================================
		"""

		print("""
			███╗░░░███╗░█████╗░██████╗░██████╗░██╗░█████╗░███╗░░██╗
			████╗░████║██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗████╗░██║
			██╔████╔██║██║░░██║██████╔╝██████╔╝██║██║░░██║██╔██╗██║
			██║╚██╔╝██║██║░░██║██╔══██╗██╔═══╝░██║██║░░██║██║╚████║
			██║░╚═╝░██║╚█████╔╝██║░░██║██║░░░░░██║╚█████╔╝██║░╚███║
			╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝\n\n""")

		print("1) Screen")
		print("2) Local")

		self.lan = input("> ")
		self.lan = int(self.lan)

		self.init(self.lan)



	def lunche(self) :
		
		self.morpion.print_tic_tac_toe()

		while self.morpion.get_nb_strockes() < self.morpion.get_nb_strockesMax() and self.morpion.get_continue()  :

			if(self.lan == 1) :
				self.Screen()
			elif(self.lan == 2) :
				self.Local()

			self.morpion.set_nb_strockes()


		if self.morpion.get_continue()  :
			self.morpion.set_nb_whyWin(3)

		if(self.lan == 2) :
			self.server.seedValueNum(morpion.get_whyWin())

		self.why_win(morpion)

	def Local(self) :

	
	
		if(self.morpion.get_nb_strockes() % 2 == 1) :

			self.morpion.user('x','\033[35m')

			if(self.morpion.get_continue()) :
				self.server.seedValue(self.morpion.get_list())
			else :
				self.server.seedValueB(self.morpion.why_win())
		else :
		
			_user = self.server.receive()
			_user = _user.split("'")
			_user = int(_user[0])
	
			self.morpion.combination(_user,'\033[36m','o')

		if(self.morpion.get_nb_strockes() > 2) :
			self.morpion.search()

		self.morpion.print_tic_tac_toe()
	

	def  Screen(self) :

		if(self.morpion.get_nb_strockes() % 2 == 0) :
			self.morpion.user('x','\033[35m')
		else :
			self.morpion.user('o','\033[36m')

		if(self.morpion.get_nb_strockes() > 2) :
			self.morpion.search()

		self.morpion.print_tic_tac_toe()

	def why_win(self,morpion) :

		if(self.morpion.get_whyWin() == 1) :
			print("player x win")
		elif(self.morpion.get_whyWin() == 2):
			print("player o win")
		else :
			print("partie nul")

	def init(self,lan : int) :

		if(lan == 1) :
			self.morpion = CToc.TIC()
		elif(lan == 2) :
			print("En attente du client : ")
			self.server = Cserver.Server()
			self.morpion = CToc.TIC(server)
			print("Connexion etablie : ")



