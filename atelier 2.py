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