class Voiture:

    def _init_(self, matricule, annee, marque, kilometrage):
        self.matricule = matricule
        self.annee = annee
        self.marque = marque
        self.kilometrage = kilometrage
        self.chauffeur = None

    def afficherInformations(self):
            print("Voiture :", self.marque)
            print("Matricule :", self.matricule)
            print("Année :", self.annee)
            print("Kilométrage :", self.kilometrage)

            if self.chauffeur != None:
                print("Chauffeur :", self.chauffeur.nom, self.chauffeur.prenom)
            else:
                print("Aucun chauffeur")
class Employe:

    def _init_(self, numeroPermis, nom, prenom):
        self.numeroPermis = numeroPermis
        self.nom = nom
        self.prenom = prenom
        self.voitureService = None