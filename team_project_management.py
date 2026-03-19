# 1. Création de la Liste d'Équipes
def creer_equipe():
    equipes = []
    nbr = int(input("Entrez  le nombre d'équipes à inclure dans lacompétition : "))
    for i in range(nbr):
        print(f"OK! donnez les informations d'équipe {i+1} : ")
        nom = input('Nom : ')
        creativ = float(input("Note de créativité : "))
        collab = float(input("Note de collaboration : "))
        present = float(input("Note de présentation : "))

        equipe = {
            'nom' : nom,
            'créativité' : creativ,
            'collaboration' : collab,
            'présentation' : present
        }
        equipes.append(equipe)
    return equipes
# 2. Calcul de la Moyenne des Équipes 
def calcule_moyenne(equipes):
    for equipe in equipes:
        moyenne = round( (equipe['créativité'] + equipe['collaboration'] + equipe['présentation'])/3 ,2)
        equipe.update({'moyenne' : moyenne})


# 3. Recherche de l'Équipe avec la Meilleure Moyenne
def meilleur_equipe(equipes):
    meilleur = equipes[0]
    for equipe in equipes:
        if meilleur['moyenne'] < equipe['moyenne']:
            meilleur = equipe
    print(f"La meilleur d'équipe est {meilleur['nom']} avec la moyenne est {meilleur['moyenne']}")
    return equipe
# 4. Affichage des Résultats 
# 5. Équipe avec la Moins Bonne Moyenne 
def pire_equipe(equipes):
    pire = equipes[0]
    for equipe in equipes:
        if pire['moyenne'] > equipe['moyenne']:
            pire = equipe
    print(f"le pire d'équipe est {pire['nom']} avec la moyenne est {pire['moyenne']}")
    return equipe
# 6. Moyenne Générale de la Compétition 
def moyenne_generale(equipes):
    somme = 0
    for equipe in equipes:
        somme += equipe['moyenne']
    moyenne_generale = somme / len(equipes)
    print(f"la moyenne de toutes les moyennes des équipes {moyenne_generale}")
    return moyenne_generale
# 7. Écart entre la Meilleure et la Pire Équipe 
def ecrat(equipes):
    #Trouver la meilleur moyenne : 
    meilleur_moy = equipes[0]['moyenne']
    for equipe in equipes:
        if meilleur_moy < equipe['moyenne']:
            meilleur_moy = equipe['moyenne']
            
    #Trouver la pire moyenne : 
    pire_moy = equipes[0]['moyenne']
    for equipe in equipes:
        if pire_moy > equipe['moyenne']:
            pire_moy = equipe['moyenne']
    ecart = round((meilleur_moy - pire_moy) ,2)
    print(f"La meilleur moyenne est {meilleur_moy}")
    print(f"La pire moyenne est {pire_moy}")
    print(f"l'écart entre la meilleure moyenne et la pire moyenne est {ecart}")
    return ecart
def statistiques(equipes):
    somme_creativ = 0
    somme_collab = 0
    somme_present = 0
    for equipe in equipes:
        somme_creativ +=equipe['créativité']
        somme_collab +=equipe['collaboration']
        somme_present +=equipe['présentation']
    craetiv_moy = round((somme_creativ / len(equipes)) ,2)
    collab_moy = round((somme_collab  / len(equipes)) ,2)
    present_moy = round((somme_present / len(equipes)) ,2)
    print(f"La moyenne generale de la catégorie Créativité est {craetiv_moy}")
    print(f"La moyenne generale de la catégorie Collaboration est {collab_moy}")
    print(f"La moyenne generale de la catégorie Présentation est {present_moy}")
    print(f"la plus haute moyenne globale est {max(craetiv_moy,collab_moy,present_moy)}")

def mention():
    for equipe in equipes:
        if equipe['moyenne']>16:
                mention = "Excellente"
        elif equipe["moyenne"]>=14 and equipe['moyenne']<16:
                mention = "Très bien"
        elif equipe["moyenne"]>=12 and equipe['moyenne']<14:
                mention = "Bien"
        elif equipe["moyenne"]>=10 and equipe['moyenne']<12:
                mention = "Passable"
        else:
                mention = "Insuffisant"
    print(f"Equipe : {equipe['nom']} | Moyenne : {equipe['moyenne']} | Mention : {mention}" )

# programme principal
equipes = creer_equipe()
calcule_moyenne(equipes)
print("=================================================")
meilleur_equipe(equipes)
print("=================================================")
pire_equipe(equipes)
print("=================================================")
moyenne_generale(equipes)
print("=================================================")
ecrat(equipes)
print("=================================================")
statistiques(equipes)
print("=================================================")
mention()




