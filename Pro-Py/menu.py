from Livre import *
from Adherent import *
from Auteur import *
from Emprunt import *
from Personne import *
from Bib import *
from datetime import date, timedelta


b = Bib()
while True:
    print('''
      ------MENU--------
        1. Ajouter Livre
        2. Ajouter Adhérent
        3. Rechercher Adhérent
        4. Rechercher Livre
        5. Ajouter Emprunt
        6. Retour Emprunt
        7. Top Emprunts
        8. Liste des Emprunteurs Actifs
        9. Date Disponibilité Livre
        10. Afficher Livres
        11. Afficher Adhérents
        12. Rapport
        13. Quitter
    ''')
    choix = int(input("Entrez votre choix : "))

    try:
        if choix == 1:
            code = input("Code (Ex : L1234) : ")
            titre = input("Titre : ")
            auteur_nom = input("Nom de l'auteur : ")
            auteur_prenom = input("Prénom de l'auteur : ")
            auteur_code = input("Code de l'auteur (Ex : A1234) : ")
            nbr_ttl_exemplaire = int(input("Nombre total d'exemplaires : "))
            b.ajouterLivre(code, titre, auteur_nom, auteur_prenom, auteur_code, nbr_ttl_exemplaire)
            print("Livre ajouté avec succès.")

        elif choix == 2:
            nom = input("Nom : ")
            prenom = input("Prénom : ")
            jour = int(input("Jour d'adhésion : "))
            mois = int(input("Mois d'adhésion : "))
            annee = int(input("Année d'adhésion : "))
            dateAdhesion = date(annee, mois, jour)
            b.ajouterAdherent(nom, prenom, dateAdhesion)
            print("Adhérent ajouté avec succès.")

        elif choix == 3:
            codeA = int(input("Entrez le code de l'adhérent : "))
            adherent = b.rechercherAdherent(codeA)
            if adherent:
                print(adherent)
            else:
                print("Adhérent introuvable.")

        elif choix == 4:
            codeL = input("Entrez le code du livre : ")
            livre_instance = b.rechercherLivre(codeL)
            if livre_instance:
                print(livre_instance)
            else:
                print("Livre introuvable.")

        # elif choix == 5:
        #     codeA = int(input("Code de l'adhérent : "))
        #     codeL = input("Code du livre : ")
        #     b.ajouterEmprunt(codeA, codeL)
        #     print("Emprunt ajouté avec succès.")

        # elif choix == 6:
        #     codeEmprunt = int(input("Code de l'emprunt : "))
        #     b.retourEmprunt(codeEmprunt)
        #     print("Retour d'emprunt enregistré avec succès.")
        elif choix==5:
                CodeA=int(input("Enter Votre Code De Adherent "))
                CodeL=input("Enter Votre Code De Livre ")
                try:
                    b.ajouterEmprunt(CodeA,codeL)
                    print("Emprunt ajouté avec Succès")
                except Exception as e:
                    print(e)
        elif choix==6:
            codeEmprunt=int(input("Entrer le Code de L'Emprent "))
            try:
                b.retourEmprunt(codeEmprunt)
                print("Le retour de Emprunt enregister Avec succès")
            except Exception as a:
                print(a)

        elif choix == 7:
            livres = b.topEmprunts()
            print("Les livres les plus empruntés :")
            for livre_instance in livres:
                print(livre_instance)

        elif choix == 8:
            emprunteurs = b.emprunteurs()
            print("Liste des emprunteurs actifs :")
            for emprunteur in emprunteurs:
                print(emprunteur)

        elif choix == 9:
            codeL = input("Entrez le code du livre : ")
            disponibilite = b.datePossibiliteEmprunt(codeL)
            print(disponibilite)

        elif choix == 10:
            livres = b.getLivres()
            print("Liste des livres :")
            for livre_instance in livres:
                print(livre_instance)

        elif choix == 11:
            adherents = b.getAdherents()
            print("Liste des adhérents :")
            for adherent in adherents:
                print(adherent)

        elif choix == 12:
            rapport = b.getRapport()
            print("Rapport de la bibliothèque :")
            for key, value in rapport.items():
                print(f"{key} : {value}")

        elif choix == 13:
            print("Au revoir !")
            break

        else:
            print("Choix invalide. Veuillez réessayer.")

    except Exception as e:
        print(f"Erreur : {e}")