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