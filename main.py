import ListePersonne.ListePersonne as Liste
import ListePersonne.Personne as Personne
import FileAttente.FileAttente as File
import Cinema.SalleCinema as Salle

        
###################################################################################################

###################################################################################################

###################################################################################################

###################################################################################################
            
def menu(): # Fonction du Menu Principale
    print("Entrer l'une des options suivante: ")
    print("1 - Gerer les personnes")
    print("2 - Gerer la liste d'attente")
    print("3 - Gerer la salle de cinema")
    print("0 - Quitter")
    
    choix = float(input())
    return choix

def menu_personne(): # Fonction de Personne
    print("Entrer l'une des options suivantes: ")
    print("1 - Ajouter une personne")
    print("2 - Afficher les personnes")
    print("3 - Rechercher une personne")
    print("4 - Filtrer les personnes par âge")
    print("5 - Quitter")
    choix = input("Entrez votre choix: ")
    return choix

def menu_liste(): # Fonction de Liste
    print("Entrer l'une des options suivante: ")
    print("1 - Ajouter une personne a la liste d'attente")
    print("2 - Retirer la 1ere personne de la liste d'attente")
    print("3 - Mettre en priorite quelqu'un")
    print("4 - Afficher la liste d'attente")
    print("5 - Quitter")
    choix = input()
    return choix

def menu_cinema(): # Fonction du Cinema
    print("Entrer l'une des options suivante: ")
    print("1 - Reserver une place")
    print("2 - Afficher les places reserver")
    print("3 - Nombre de place disponible")
    print("4 - Annuler une reservation")
    print("5 - Reserver une place speciale")
    print("6 - Recherche de place par nom")
    print("7 - Quitter")
    choix = input()
    return choix

###################################################################################################
liste_personne = Liste.ListePersonnes()
file_attente = File.FileAttente()
salle_cinema = Salle.SalleCinema()
choix = 3
quitter = '0'

while(choix != quitter):

    choix = menu()

    if choix == 1:

        while(choix != '5'):
            choix = menu_personne()
            if choix == '1':
                print("Cree une personne")
                nom = str(input("Entrer Nom : "))
                age = int(input("Entrer Age : "))
                pers = Personne.Personne(nom, age)
                liste_personne.ajouter_personne(pers)

            elif choix == '2':
                liste_personne.afficher_liste()

            elif choix == '3':
                liste_personne.rechercher_personne()

            elif choix == '4':
                liste_personne.filtrer_personnes_par_age()

            elif choix == '5':
                break
            else:
                print("Choix Invalide")
            break

    elif choix == 2:
        
        while(choix != '5'):

            choix = menu_liste()

            if choix == '1':
                file_attente.ajouter_personne_en_attente()

            elif choix == '2':
                file_attente.supprimer_personne_de_attente()
            
            elif choix == '3':
                file_attente.ajouter_personne_prioritaire()

            elif choix == '4':
                file_attente.afficher_liste()

            elif choix == '5':
                break
            else:
                print("Choix Invalide")
                break

    elif choix == 3:
        while(choix != '7'):
            choix = menu_cinema()
            if choix == '1':
                salle_cinema.reserver_place()

            elif choix == '2':
                salle_cinema.afficher_places_reservées()

            elif choix == '3':
                salle_cinema.nombre_places_disponibles()

            elif choix == '4':
                salle_cinema.annuler_reservation()

            elif choix == '5':
                salle_cinema.reserver_place_speciale()

            elif choix =='6':
                salle_cinema.filtrer_reservations_par_personne()
            elif choix == '7':
                break
            else:
                print("Choix Invalide")
                break
    