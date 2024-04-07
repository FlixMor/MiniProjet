class Personne:
    def __init__(self, nom, age):
        self.__nom = nom
        self.__age = age


    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, v):
        self.__nom = v


    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, v):
        self.__age = v