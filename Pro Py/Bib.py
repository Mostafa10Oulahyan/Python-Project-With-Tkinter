from Livre import *
from Adherent import *
from Auteur import *
from Emprunt import *
from Personne import *
from datetime import date, timedelta


class Bib:
    def __init__(self):
        self.__livres = []
        self.__adherents = []
        self.__emprunts = []

    def ajouterLivre(self, code, titre, auteur_nom, auteur_prenom, auteur_code, nbr_ttl_exemplaire):
        for livre in self.__livres:
            if livre.get_code() == code:
                raise Exception("Il existe déjà un livre avec ce code !")
        auteur = Auteur(auteur_nom, auteur_prenom, auteur_code)
        livre_instance = livree(code, titre, auteur, nbr_ttl_exemplaire, nbr_ttl_exemplaire)
        self.__livres.append(livre_instance)

    def ajouterAdherent(self, nom, prenom, dateAdhesion):
        adherent = Adherent(nom, prenom, dateAdhesion)
        self.__adherents.append(adherent)

    def rechercherAdherent(self, code):
        for adherent in self.__adherents:
            if str(adherent.getCode()) == str(code):  # Ensure comparison as strings
                return adherent
        return None

    def rechercherLivre(self, code):
        for livre in self.__livres:
            if str(livre.get_code()) == str(code):  # Ensure comparison as strings
                return livre
        return None
    def ajouterEmprunt(self, codeA, codeL):
        adherent = self.rechercherAdherent(int(codeA))
        livre = self.rechercherLivre(codeL)
        if livre and adherent and livre.LivreDisponible():
            dateEmprunt = date.today()
            dateRetourPrevue = dateEmprunt + timedelta(days=3)
            emprunt = Emprunt(livre, adherent, dateEmprunt, dateRetourPrevue, dateREffective=None)
            self.__emprunts.append(emprunt)
            livre.set_nbr_exemplaire_disponible(livre.get_nbr_exemplaire_disponible()-1)
            livre.addNbrEmprunt()
            

    def retourEmprunt(self,codeEmprunt):
        for elt in self.__emprunts:
            if elt.getCode() == int(codeEmprunt):
                if elt.etatEmprunt() != "rendu" or elt.getDateRetourEffective():
                    elt.setDateRetourEffective(date.today())
                    elt.getLivreEmprunte().set_nbr_exemplaire_disponible(elt.getLivreEmprunte().get_nbr_exemplaire_disponible()+1) 
                    return True
                else:
                    raise Exception("Ce livre est deja rendu")
        raise Exception("il n'y a pas de emprunt avec ce code!")

    def topEmprunts(self):
        if not self.__livres:
            raise Exception("Aucun livre disponible.")
        livres_avec_emprunts = [livre for livre in self.__livres if livre.getNbrEmprunt() is not None]
        if not livres_avec_emprunts:
            raise Exception("Aucun emprunt enregistré.")
        max_emprunt = max(livre.getNbrEmprunt() for livre in livres_avec_emprunts)
        return [livre for livre in livres_avec_emprunts if livre.getNbrEmprunt() == max_emprunt]

    def emprunteurs(self):
        emprunteurs_actifs = []
        for emprunt in self.__emprunts:
            if emprunt.etatEmprunt() in ["en cours", "non rendu"]:
                if emprunt.getEmprunteurLivre() not in emprunteurs_actifs:
                    emprunteurs_actifs.append(emprunt.getEmprunteurLivre())
        if not emprunteurs_actifs:
            raise Exception("Aucun emprunteur actif.")
        return emprunteurs_actifs
    def datePossibiliteEmprunt(self, codeL):
        livre_instance = self.rechercherLivre(codeL)
        if not livre_instance:
            raise Exception("Livre introuvable.")
        if livre_instance.LivreDisponible():
            return "Le livre est disponible."
        for emprunt in self.__emprunts:
            if emprunt.getLivreEmprunte() == livre_instance and emprunt.etatEmprunt() == "en cours":
                return f"Ce livre sera disponible le : {emprunt.getDateRetourPrevue().strftime('%d/%m/%Y')}"
        return "Il n'est pas prévu qu'il soit disponible."
      

    
    
    
    
    
    
    
    
    
    
    
    def getLivres(self):
        if not self.__livres:
            raise Exception("Aucun livre disponible.")
        return self.__livres

    def getAdherents(self):
        if not self.__adherents:
            raise Exception("Aucun adhérent enregistré.")
        return self.__adherents

    def getRapport(self):
        return {
            "Nombres des livres": len(self.__livres),"\n"
            "Nombres des adhérents": len(self.__adherents),"\n"
            "Nombres des emprunts": len(self.__emprunts),
        }
