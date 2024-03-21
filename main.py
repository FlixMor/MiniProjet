class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

###################################################################################################
        
class ListePersonnes:
    def __init__(self):
        self.personnes = []


    def ajouter_personne(self, nom, age):
        self.personnes.append(Personne(nom, age))


    def afficher_personnes(self):
        for personne in self.personnes:
            print(f"Nom: {personne.nom}, Age: {personne.age}")

    
    def rechercher_personne(self, nom):
        for personne in self.personnes:
            if personne.nom == nom:
                print(f"Voici la personne trouve: Nom: {personne.nom}, Age: {personne.age}")
                return
        print("Personne non trouvée.")


    def filtrer_personnes_par_age(self, min_age, max_age):
        for personne in self.personnes:
            if min_age <= personne.age <= max_age:
                print(f"Nom: {personne.nom}, Age: {personne.age}")

###################################################################################################

class FileAttente:
    def __init__(self):
        self.attente = []

    def ajouter_personne_en_attente(self, nom):
        self.attente.append(nom)

    def supprimer_personne_de_attente(self):
        if self.attente:
            personne = self.attente.pop(0)
            print(f"{personne} a été supprimé de la file d'attente.")
        else:
            print("La file d'attente est vide.")

    def afficher_liste(self):
        print(self.attente)

    def ajouter_personne_prioritaire(self, nom):
        self.attente.remove(nom)
        self.attente.insert(0, nom)

###################################################################################################
    
class SalleCinema:
    def __init__(self, capacite):
        self.capacite = capacite
        self.places_reserves = {}

    def reserver_place(self, nom, place):
        if len(self.places_reserves) < self.capacite:
            self.places_reserves[nom] = place
            print(f"{nom} a reserver la place: {place}.")
        else:
            print("Salle pleine.")

    def afficher_places_reservées(self):
        for nom, place in self.places_reserves.items():
            print(f"Personne: {nom}, Place Reserver: {place}")
            print("-----------------------------------------")

    def nombre_places_disponibles(self):
        print("Place Disponible : ",self.capacite - len(self.places_reserves))

    def filtrer_reservations_par_personne(self, nom):
        for nom_reserv, place in self.places_reserves.items():
            if nom_reserv == nom:
                print(f"Place: {place}, Reserver par: {nom_reserv}")
                print("-----------------------------------------")

    def annuler_reservation(self, nom):
        reservations_annulees = [nom_reserv for nom_reserv in self.places_reserves.keys() if nom_reserv == nom]
        for nom_reserv in reservations_annulees:
            del self.places_reserves[nom_reserv]

    def reserver_place_speciale(self, nom):
        if len(self.places_reserves) < self.capacite:
            self.places_reserves[nom] = "Place spéciale"
            print(f"Place spéciale pour {nom}.")
        else:
            print("La salle est pleine.")

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
    choix = int(input("Entrez votre choix: "))
    return choix

def menu_liste(): # Fonction de Liste
    print("Entrer l'une des options suivante: ")
    print("1 - Ajouter une personne a la liste d'attente")
    print("2 - Retirer la 1ere personne de la liste d'attente")
    print("3 - Mettre en priorite quelqu'un")
    print("4 - Afficher la liste d'attente")
    print("5 - Quitter")
    choix = int(input())
    return choix

def menu_cinema(): # Fonction du Cinema
    print("Entrer l'une des options suivante: ")
    print("1 - Reserver une place")
    print("2 - Afficher les places reserver")
    print("3 - Nombre de place disponible")
    print("4 - Annuler une reservation")
    print("5 - Reserver une place speciale")
    print("6 - Quitter")
    choix = float(input())
    return choix

###################################################################################################

liste_personne = ListePersonnes()
file_attente = FileAttente()
salle_cinema = SalleCinema(10)
choix = 1
quitter = 0

while(choix != quitter):

    choix = menu()

    if choix == 1:

        while(choix != 5):
            choix = menu_personne()
            if choix == 1:
                print("Cree une personne")
                nom = str(input("Entrer Nom : "))
                age = int(input("Entrer Age : "))
                liste_personne.ajouter_personne(nom, age)

            elif choix == 2:
                liste_personne.afficher_personnes()

            elif choix == 3:
                nom = str(input("Entrer Nom a chercher: "))
                liste_personne.rechercher_personne(nom)

            elif choix == 4:
                min_age = int(input("Entrer Age Minimum: "))
                max_age = int(input("Entrer Age Maximum: "))
                liste_personne.filtrer_personnes_par_age(min_age, max_age)
            elif choix == 5:
                break
            else:
                print("Choix Invalide")
            break

    elif choix == 2:
        
        while(choix != 5):
            choix = menu_liste()
            if choix == 1:
                nom = str(input("Entrer Nom a ajouter a la liste: "))
                file_attente.ajouter_personne_en_attente(nom)

            elif choix == 2:
                file_attente.supprimer_personne_de_attente()
            
            elif choix == 3:
                nom = str(input("Entrer Nom a ajouter en priorite: "))
                file_attente.ajouter_personne_prioritaire(nom)

            elif choix == 4:
                file_attente.afficher_liste()

            elif choix == 5:
                break
            else:
                print("Choix Invalide")
                break

    elif choix == 3:
        while(choix != 6):
            choix = menu_cinema()
            if choix == 1:
                nom = str(input("Entrer le Nom : "))
                place = str(input("Entrer la place desirer : "))
                salle_cinema.reserver_place(nom, place)

            elif choix == 2:
                salle_cinema.afficher_places_reservées()

            elif choix == 3:
                salle_cinema.nombre_places_disponibles()

            elif choix == 4:
                nom = str(input("Entrer le nom de la personne a annuler la reservation: "))
                salle_cinema.annuler_reservation(nom)

            elif choix == 5:
                nom = str(input("Entrer le nom de la personne speciale: "))
                salle_cinema.reserver_place_speciale(nom)

            elif choix == 6:
                break
            else:
                print("Choix Invalide")
                break
    