import FileAttente.FileAttenteDAO as dao

class FileAttente:
    def __init__(self):
        self.attente = []

    def ajouter_personne_en_attente(self):
        try:
            nom = str(input("Entrer Nom a ajouter a la liste: "))
        except:
            print("Erreur de saisie")
        dao.insertion(nom)
        self.attente.append(nom)

    def supprimer_personne_de_attente(self):
        try:
            personne = self.attente.pop(0)
            dao.suppression(personne)
            print(f"{personne} a été supprimé de la file d'attente.")
        except:
            print("La file d'attente est vide.")

    def afficher_liste(self):
        print(self.attente)

    def ajouter_personne_prioritaire(self):
        try:
            nom = str(input("Entrer Nom a ajouter en priorite: "))
        except:
            print("Erreur dans l'entrée")
        self.attente.remove(nom)
        self.attente.insert(0, nom)
        

