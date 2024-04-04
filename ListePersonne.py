class ListePersonnes:
    def __init__(self):
        self.personnes = []


    def ajouter_personne(self, nom, age):
        self.personnes.append(Personne(nom, age))
        datab.cree_pers(nom, age)
        


    def afficher_personnes(self):
        datab.afficher_pers()
        #for personne in self.personnes:
            #print(f"Nom: {personne.nom}, Age: {personne.age}")

    
    def rechercher_personne(self, nom, age):
        datab.recher_pers(nom, age)
        #for personne in self.personnes:
            #if personne.nom == nom:
                #print(f"Voici la personne trouve: Nom: {personne.nom}, Age: {personne.age}")
                #return
        #print("Personne non trouvée.")


    def filtrer_personnes_par_age(self, min_age, max_age):
        for personne in self.personnes:
            if min_age <= personne.age <= max_age:
                print(f"Nom: {personne.nom}, Age: {personne.age}")
