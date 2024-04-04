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
