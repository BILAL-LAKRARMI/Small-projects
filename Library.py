# Liste des livres
livres = [
    {
        "id": 1,
        "titre": "Apprendre Python",
        "auteur": "Jean Dupont",
        "categorie": "Programmation",
        "prix": 120,
        "stock": 10,
        "emprunts": 5
    },
    {
        "id": 2,
        "titre": "Les Bases de Données",
        "auteur": "Marie Martin",
        "categorie": "Informatique",
        "prix": 150,
        "stock": 7,
        "emprunts": 3
    },
    {
        "id": 3,
        "titre": "Algorithmes Simples",
        "auteur": "Ali Benali",
        "categorie": "Programmation",
        "prix": 90,
        "stock": 12,
        "emprunts": 8
    },
    {
        "id": 4,
        "titre": "Réseaux Informatiques",
        "auteur": "Sophie Laurent",
        "categorie": "Réseaux",
        "prix": 200,
        "stock": 5,
        "emprunts": 2
    },
    {
        "id": 5,
        "titre": "Introduction à l'IA",
        "auteur": "Karim El Idrissi",
        "categorie": "Intelligence Artificielle",
        "prix": 180,
        "stock": 9,
        "emprunts": 6
    }
]
# 2 Afficher tous les livres avec une boucle.
for livre in livres:
    print(f"Id :{livre['id']} | titre :{livre['titre']} | auteur :{livre['auteur']} | categorie : {livre['categorie']} | prix :{livre['prix']} | stock :{livre['stock']} | emprunts :{livre['emprunts']}")

# 3 Créer une fonction d’affichage formaté d’un livre.
def afficher(livre):
    print(f"Id: {livre['id']}")
    print(f"Titre: {livre['titre']}")
    print(f"Auteur: {livre['auteur']}")
    print(f"Categorie: {livre['categorie']}")
    print(f"Prix: {livre['prix']}")
    print(f"Stock: {livre['stock']}")
    print(f"Emprunts: {livre['emprunts']}")
    print(f"="*30)

# 4 Écrire une fonction ajouter_livre().
# 5 Vérifier que l’id est unique avant ajout.
# 6 Ajouter un livre via saisie utilisateur
def ajouter_livre():
    id = int(input(f"Donnez id pour Vérifier si l'id existe déjà : "))
    for livre in livres:
        if livre['id'] == id:
            print(f"Errour ! cet Id existe déjà")
            return
    # Ajouter livre si l'Id est unique
    print(f"----Ajouter le livre----")
    id = int(input(f"Id: "))
    titre = input(f"Titre: ")
    auteur = input(f"Auteur: ")
    categorie = input(f"Categorie: ")
    prix = float(input(f"Prix: "))
    stock = int(input(f"Stock: "))
    emprunts = int(input(f"Emprunts: "))

    nouveau_livre = {
        'id': id,
        'titre': titre,
        'auteur': auteur,
        'categorie': categorie,
        'prix': prix,
        'stock': stock,
        'emprunts': emprunts
    }

    livres.append(nouveau_livre)

# 7 Rechercher un livre par id.

def rechercher_id():
    id = int(input(f"Entrez id pour rechercher un livre : "))
    for livre in livres:
        if livre['id'] == id:
            print(f"----Voila les information d'un livre {livre['titre']}---")
            print(f"Auteur: {livre['auteur']}")
            print(f"Categorie: {livre['categorie']}")
            print(f"Prix: {livre['prix']}")
            print(f"Stock: {livre['stock']}")
            print(f"Emprunts: {livre['emprunts']}")
            print(f"="*30)
            return
    print(f"Livre non trouvé !!! ")

# 8 Rechercher un livre par titre partiel.

def rechercher_titre():
    titre = input(f"Entrez titre pour rechercher un livre : ")
    for livre in livres:
        if livre['titre'].lower() == titre.lower():
            print(f"----Voila les information d'un livre {livre['titre']}---")
            print(f"Id: {livre['id']}")
            print(f"Auteur: {livre['auteur']}")
            print(f"Categorie: {livre['categorie']}")
            print(f"Prix: {livre['prix']}")
            print(f"Stock: {livre['stock']}")
            print(f"Emprunts: {livre['emprunts']}")
            print(f"="*30)
            return
    print(f"Livre non trouvé !!! ")

# 9 Afficher les livres d’une catégorie.

def rechercher_categorie():
    categorie = input(f"Entrez categorie pour rechercher un livre : ")
    for livre in livres:
        if livre['categorie'].lower() == categorie.lower():
            print(f"----Voila les information d'un livre {livre['categorie']}---")
            print(f"Id: {livre['id']}")
            print(f"Titre: {livre['titre']}")
            print(f"Auteur: {livre['auteur']}")
            print(f"Prix: {livre['prix']}")
            print(f"Stock: {livre['stock']}")
            print(f"Emprunts: {livre['emprunts']}")
            print(f"="*30)
            return
    print(f"Livre non trouvé !!! ")

# 10 Modifier le prix d’un livre.

def modifier_prix():
    titre = input(f"Entrez titre pour rechercher un livre : ")
    nouveau_prix = float(input(f"Donnez la nouvel prix pour modifier le prix d'un livre {titre} : "))
    for livre in livres:
        if livre['titre'].lower() == titre.lower():
            choix = input(f"Voulez-vous vraiment modifier le prix ? oui/non : ")
            if choix.lower() == 'oui':
                livre['prix'] = nouveau_prix
                print(f"="*30)
                print(f"Le prix a été modifier avec succès")
            else:
                print(f"Modification annulé")
            return
    print(f"Livre {titre} non trouvé !!!")

# 11 Mettre à jour le stock.

def modifier_stock():
    titre = input(f"Entrez titre pour rechercher un livre : ")
    nouveau_stock = int(input(f"Donnez la nouvel stock pour modifier le stock d'un livre {titre} : "))
    for livre in livres:
        if livre['titre'].lower() == titre.lower():
            livre['stock'] = nouveau_stock
            print(f"Le stock a été modifier avec succès")
            return
    print(f"Livre {titre} non trouvé !!!")

# 12 Augmenter le nombre d’emprunts.

def augmenter_emprunts():
    titre = input(f"Entrez titre pour rechercher un livre : ")
    nouveau_emprunts = int(input(f"Donnez l'emprunts pour augmenter le livre {titre} : "))
    for livre in livres:
        if livre['titre'].lower() == titre.lower():
            livre['emprunts'] += nouveau_emprunts
            print(f"Le emprunts a été augmenter avec succuès")
            return
    print(f"Livre {titre} non trouvé !!!")
    
# 13 Supprimer un livre par id.
def supprimer_id():
    id = int(input(f"Donnez Id pour supprimer le livre : "))
    for livre in livres:
        if livre['id'] == id:
            choix = input(f"Voulez-vous vraiment supprimer un livre {livre['titre']} ? oui/non : ")
            if choix.lower() == 'oui':
                livres.remove(livre)
                print(f"Le livre a été asupprimer avec succuès")
            else:
                print(f"Supprission annulée")
            return
    print(f"Livre {id} non trouvé !!!")

# 14 Supprimer les livres avec stock nul.
def supprimer_stock_nul():
    for livre in livres:
        if livre['stock'] == 0:
            livres.remove(livre)
            print(f"Le livre ont stock nul a été supprimer avec succès")
            return

# 15 Calculer la valeur totale du stock.
def totale_stock():
    total = 0
    for livre in livres:
        total += livre['stock']
    print(f"Valeur totale du stock : {total}")

# 16 Trouver le livre le plus emprunté.
def plus_emprunt():
    livre_plus = max(livres, key = lambda x: x['emprunts'])
    print(f"----Le livre le plus emprunté----")
    print(f"Id: {livre_plus['id']}")
    print(f"Titre: {livre_plus['titre']}")
    print(f"Auteur: {livre_plus['auteur']}")
    print(f"Prix: {livre_plus['prix']}")
    print(f"Stock: {livre_plus['stock']}")
    print(f"Emprunts: {livre_plus['emprunts']}")
    print(f"="*30)

# 17 Calculer le prix moyen.
def prix_moyen():
    somme = 0
    for livre in livres:
        somme += livre['prix']
        moyenne = somme / len(livres)
    print(f"Prix moyen est : {moyenne}")

def menu():
    while True:
        print("\n=== MENU ===")
        print("1. Afficher tous les livres")
        print("2. Ajouter un livre")
        print("3. Rechercher un livre par ID")
        print("4. Rechercher un livre par titre")
        print("5. Rechercher un livre par catégorie")
        print("6. Modifier le prix d’un livre")
        print("7. Modifier le stock d’un livre")
        print("8. Augmenter le nombre d’emprunts")
        print("9. Supprimer un livre par ID")
        print("10. Supprimer les livres avec stock nul")
        print("11. Calculer la valeur totale du stock")
        print("12. Trouver le livre le plus emprunté")
        print("13. Calculer le prix moyen")
        print("0. Quitter")
        
        choix = input("Donnez votre choix: ")
        
        if choix == "1":
            for livre in livres:
                afficher(livre)
        elif choix == "2":
            ajouter_livre()
        elif choix == "3":
            rechercher_id()
        elif choix == "4":
            rechercher_titre()
        elif choix == "5":
            rechercher_categorie()
        elif choix == "6":
            modifier_prix()
        elif choix == "7":
            modifier_stock()
        elif choix == "8":
            augmenter_emprunts()
        elif choix == "9":
            supprimer_id()
        elif choix == "10":
            supprimer_stock_nul()
        elif choix == "11":
            totale_stock()
        elif choix == "12":
            plus_emprunt()
        elif choix == "13":
            prix_moyen()
        elif choix == "0":
            print("Merci, au revoir !")
            break
        else:
            print("Choix invalide, réessayez !")

# Lancer le menu
menu()



    


    







        

