import ListePersonne.PersonneDAO as dao
import ListePersonne.Personne as Personne


class ListePersonnes:
    
    def __init__(self):
        self.liste = []


    def ajouter_personne(self,personne:Personne):

        self.liste.append(personne)
        dao.insertion(personne.nom, personne.age)
        print(self)


    def afficher_liste(cls):
        for i in dao.get_all():
            print(i)        
    
    def rechercher_personne():
        nom = input("Entrer Nom : ")
        age = input("Entrer Age : ")
        personne =  dao.recherche(nom, age)
        print (personne)


    def filtrer_personnes_par_age(self):
        min_age = int(input("Entrer Age Minimum: "))
        max_age = int(input("Entrer Age Maximum: "))
        for personne in self.liste:
            if min_age <= personne.age <= max_age:
                print(f"Nom: {personne.nom}, Age: {personne.age}")
