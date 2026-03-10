class Voiture:

    def __init__(self, matricule, annee, marque, kilometrage):
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
    def __init__(self,numeroPermis, nom, prenom):
        self.numeroPermis = numeroPermis
        self.nom =nom
        self.prenom = prenom
        self.voitureService = None

    def afficherInformations(self):
            print("Employé :", self.nom, self.prenom)
            print("Permis :", self.numeroPermis)

            if self.voitureService != None:
                print("Voiture de service :", self.voitureService.matricule)
            else:
                print("Aucune voiture assignée")

    def affecterVoiture(self, voiture):

            if self.voitureService != None:
                print("Cet employé a déjà une voiture.")
                return

            if voiture.chauffeur != None:
                print("Cette voiture est déjà attribuée.")
                return

            self.voitureService = voiture
            voiture.chauffeur = self
            print("Voiture attribuée.")

    def retirerVoiture(self):

            if self.voitureService == None:
                print("Aucune voiture à retirer.")
                return

            self.voitureService.chauffeur = None
            self.voitureService = None
            print("Voiture retirée.")


e1 =Employe("654587", "Dupont", "Jean")
e2 =Employe("67890", "Martin", "Paul")
v1 =Voiture("AA123BB", 2020, "Toyota", 20000)
v2 =Voiture("CC456DD", 2021, "Honda", 15000)

e1.afficherInformations()
print()
v1.afficherInformations()
print()
e1.affecterVoiture(v1)
print()


