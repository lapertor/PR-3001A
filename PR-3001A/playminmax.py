# Imports
from fonctionsminmax import *
import random as r

def main():
	N = 4
	A = 4
	P = []
	# Qui commence ? ==> Pierre Feuille Ciseaux avec l'ordinateur !
	InitPosition(N, P)
	(P, idjoueur) = PierreFeuilleCiseaux(P, N)
	AffichePosition(N, P)
	end = PlusDeCasesLibres(N,P) 
	while end != 0:
		if idjoueur == 1:
			P = SaisirCoupJoueur(N,P)
			AffichePosition(N,P)
			end = PlusDeCasesLibres(N,P)
			print()
			print("################################")
			print()
			idjoueur = -1
			
		#print(max_value_joueur)
		# print(coord_max_joueur)
		# print(directions_joueur)
		#print(max_value_ordi)
		# print(coord_max_ordi)
		# print(directions_ordi)
		else:
			# Evaluation de la position
			(M, score, infos_joueur, infos_ordi) = EvalPosition(N,P,A)
			max_value_joueur = infos_joueur[0]
			coord_max_joueur = infos_joueur[1]
			directions_joueur = infos_joueur[2]
			max_value_ordi = infos_ordi[0]
			coord_max_ordi = infos_ordi[1]
			directions_ordi = infos_ordi[2]
			#print(max_value_joueur)
			if max_value_joueur[0] == A: 
				print("Vous avez gagne")
				break
			if score <= 0:
				# L'ordinateur a un avantage
				max_values = max_value_ordi + max_value_joueur
				coord_max = coord_max_ordi + coord_max_joueur
				directions = directions_ordi + directions_joueur
			else:
				# Le joueur a un avantage
				max_values = max_value_joueur + max_value_ordi
				coord_max = coord_max_joueur + coord_max_ordi
				directions = directions_joueur + directions_ordi
			# print(max_value)
			#print(coord_max)
			# print(directions)
			
			if max_values[0] == 1:
				# On n'a aucune ligne/colonne/diagonale d'entammée
				for i in range(len(coord_max)):
					# Du coup on essaye d'en créer une, en privilégiant une diagonale
					# de longueur >= à A (Placer1)
					coord = coord_max[i]
					max_value = int(max_values[i])
					(P, place) = Placer1(P, N, A, max_value, coord)
					if place == 1:
						break
				if place == 0:
					#Si on n'y arrive pas on place aléatoirement
					PlacerAleat(P, N)
			else:
				# On a une ligne à compléter ==> on essaye de la continuer (dans la même direction)
				for i in range(len(coord_max)):
					coord = coord_max[i]
					direction = directions[i]
					max_value = int(max_values[i])
					place = 0
					if direction == 0:
						(P, place) = PlacerDiagGD(P, N, max_value, coord)
					elif direction == 1:
						(P, place) = PlacerVert(P, N, max_value, coord)
					elif direction == 2:
						(P, place) = PlacerDiagDG(P, N, max_value, coord)
					else:
						(P, place) = PlacerHoriz(P, N, max_value, coord)
					if place == 1:
						break
				if place == 0:
					# Si on n'y arrive pas on place aléatoirement encore une fois
					print("placement aléatoire")
					PlacerAleat(P,N)
			AffichePosition(N,P)
			(M, score, infos_joueur, infos_ordi) = EvalPosition(N,P,A)
			if infos_ordi[0][0] == A:
				print("L'ordinateur a gagne")
				break
			end = PlusDeCasesLibres(N,P)
			print()
			print("################################")
			print()
			idjoueur = 1
	print("Jeu fini. Merci pour votre participation !")


main()
