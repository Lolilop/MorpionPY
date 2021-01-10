#coding : utf-8
#!/usr/bin/env python3

import Cserver
import CToc


def  Screen(morpion) :

		morpion.print_tic_tac_toe()

		if(morpion.nb_coups % 2 == 0) :

			morpion.User('x','\033[35m')

		else :

			morpion.User('o','\033[36m')

		morpion.search()


def Local(morpion,server) :
	
	if(morpion.nb_coups % 2 == 1) :

		morpion.User_local('x','\033[35m')

		if(morpion.continuer) :
			server.seedValue(morpion.liste)
		else :
			server.seedValueB(morpion.partie)
		

	else :
		
		user = server.receive()
		user = user.split("'")
		user = int(user[0])
		
	
		morpion.comb_local(user,'\033[36m','o')
		morpion.search_local()

	morpion.print_tic_tac_toe()
		

print("1) simple Screen")
print("2) double screen")

lan = input("> ")
lan = int(lan)

server = None
morpion = None

if(lan == 1) :
	morpion = CToc.TIC()
elif(lan == 2) :

	print("En attente du client : ")
	server = Cserver.Server()
	morpion = CToc.TIC(server)
	print("Connexion etablie : ")

while morpion.nb_coups < morpion.nb_coupsMax and morpion.continuer  :

	if(lan == 1) :
		Screen(morpion)

	elif(lan == 2) :
		Local(morpion,server)


	
	morpion.nb_coups = morpion.nb_coups + 1


if(morpion.continuer) :
	print("partie nul")
	morpion.partie = 3

if(lan == 2) :

	server.seedValueNum(morpion.partie)