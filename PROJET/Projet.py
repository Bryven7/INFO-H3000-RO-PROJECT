import csv

def charger_donnees_csv(nom_fichier):
    donnees = []
    with open(nom_fichier, 'r') as fichier:
        lecteur_csv = csv.reader(fichier)
        for ligne in lecteur_csv:
            priorite, deadline = int(ligne[0]), int(ligne[1])
            temps_usinage = [int(temps) for temps in ligne[2:]]
            donnees.append((priorite, deadline, temps_usinage))
    return donnees


def calculer_makespan(donnees):
    makespan = 0
    temps_machine = [0] * 10  # Initialiser les temps de fin de chaque machine à 0
    x = 0

    for priorite, deadline, temps_usinage in donnees:
        temps_machine[0] = max(temps_machine[0], temps_machine[9]) + temps_usinage[0]  # Temps de fin de la pièce sur la première machine
        x += deadline
        # Calculer le temps de fin de la pièce sur les autres machines
        for j in range(1, 10):
            temps_machine[j] = max(temps_machine[j], temps_machine[j-1]) + temps_usinage[j]
        
        makespan = max(makespan, temps_machine[9] + deadline)  # Mettre à jour le makespan si nécessaire

    print('x =',x)
    return makespan

def calculer_total_weighted_tardiness(donnees):
    total_weighted_tardiness = 0
    temps_machine = [0] * 10  # Initialiser les temps de fin de chaque machine à 0
    
    for priorite, deadline, temps_usinage in donnees:
        temps_machine[0] = max(temps_machine[0], temps_machine[9]) + temps_usinage[0]  # Temps de fin de la pièce sur la première machine
        
        # Calculer le temps de fin de la pièce sur les autres machines
        for j in range(1, 10):
            temps_machine[j] = max(temps_machine[j], temps_machine[j-1]) + temps_usinage[j]
        
        temps_fin_piece = max(temps_machine)  # Temps de fin de la pièce sur la dernière machine

        if temps_fin_piece > deadline :
            tardiness = max(0, temps_fin_piece - deadline) * priorite  # Calcul du retard pondéré
            total_weighted_tardiness += tardiness  # Ajouter le retard pondéré au total
    
    return total_weighted_tardiness


# Calcul du makespan
donnees = charger_donnees_csv("instance.csv")
makespan = calculer_makespan(donnees)
print("Makespan calculé :", makespan)

# Calcul du total weighted tardiness
total_weighted_tardiness = calculer_total_weighted_tardiness(donnees)
print("Total weighted tardiness calculé :", total_weighted_tardiness)


     