import Cinema.SalleCinemaDAO as dao
class SalleCinema:
    def __init__(self):
        self.places_reserves = {}
        self.capacite = 99

    def reserver_place(self):
        if (self.capacite - len(self.places_reserves)) <= 0 :
            print("Salle Pleine")
            return
        nom = str(input("Entrer le Nom : "))
        place = str(input("Entrer la place desirer : "))
        self.places_reserves[nom] = place
        print(f"{nom} a reserver la place: {place}.")
        dao.insertion(nom, place)


    def afficher_places_reservées(self):
        for nom, place in dao.get_all():
            print("-----------------------------------------")
            print(f"Personne: {nom}, Place Reserver: #{place}")
            print("-----------------------------------------")

    def nombre_places_disponibles(self):
        print("Place Disponible : ",self.capacite - len(self.places_reserves))

    def filtrer_reservations_par_personne(self):
        nom = str(input("Entrer le nom de la personne a chercher: "))
        for i in dao.get_by_name(nom):    
            print("-----------------------------------------")            
            print(f"Place: {i[0]}, Reserver par: {i[1]}")
            print("-----------------------------------------")

    def annuler_reservation(self):
        nom = str(input("Entrer le nom de la personne a annuler la reservation: "))
        dao.remove(nom)
        
            
    def reserver_place_speciale(self):
        nom = str(input("Entrer le nom de la personne speciale: "))
        if len(self.places_reserves) < self.capacite:
            self.places_reserves[nom] = "Place spéciale"
            print(f"Place spéciale pour {nom}.")
            dao.insertion(nom, "Place spéciale")
        else:
            print("La salle est pleine.")