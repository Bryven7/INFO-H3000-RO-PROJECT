import csv

# Charger les données depuis le fichier instance.csv
def charger_instance(nom_fichier):
    pieces = []
    with open(nom_fichier, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            pieces.append([int(x) for x in row])
    return pieces

# Calculer le "Total weighted tardiness" d'une séquence de pièces
def total_weighted_tardiness(sequence, pieces):
    total_tardiness = 0
    for idx, piece_id in enumerate(sequence):
        piece = pieces[piece_id]
        priority, deadline = piece[0], piece[1]
        duration = sum(piece[2:])  # Durée totale pour usiner la pièce sur toutes les machines
        finish_time = sum([sum(pieces[p][2:]) for p in sequence[:idx+1]])  # Heure de fin de la pièce
        tardiness = max(0, finish_time - deadline)  # Calcul du retard (s'il y en a)
        total_tardiness += tardiness * priority
    return total_tardiness

# Générer toutes les permutations possibles des pièces
def generer_permutations(pieces):
    n = len(pieces)
    indices = list(range(n))
    permutations = [[indices[j] for j in perm] for perm in permute(indices)]
    return permutations

# Fonction pour générer des permutations
def permute(a):
    if len(a) == 1:
        yield [a[0]]
    else:
        for i in range(len(a)):
            rest = a[:i] + a[i+1:]
            for p in permute(rest):
                yield [a[i]] + p

# Algorithme heuristique pour trouver une approximation de la frontière Pareto optimale
def heuristique_flowshop(pieces):
    solutions = []  # Liste pour stocker les solutions trouvées
    all_permutations = generer_permutations(pieces)
    best_makespan = float('inf')  # Initialisation du meilleur Makespan trouvé
    best_tardiness = float('inf')  # Initialisation de la meilleure tardiness trouvée
    
    for perm in all_permutations:
        makespan = sum([sum(pieces[p][2:]) for p in perm])  # Calcul du Makespan pour cette permutation
        tardiness = total_weighted_tardiness(perm, pieces)  # Calcul de la tardiness
        
        # Vérifier si cette solution est sur la frontière Pareto
        if makespan <= best_makespan and tardiness <= best_tardiness:
            solutions.append(perm)
            best_makespan = min(best_makespan, makespan)
            best_tardiness = min(best_tardiness, tardiness)
    
    return solutions

# Fonction principale pour exécuter l'algorithme
def main():
    nom_fichier = 'instance.csv'  # Nom du fichier avec les données des pièces
    pieces = charger_instance(nom_fichier)  # Charger les pièces depuis le fichier
    
    # Appliquer l'algorithme heuristique
    solutions = heuristique_flowshop(pieces)
    
    # Écrire les solutions dans un fichier CSV
    with open('resultat.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for sol in solutions:
            writer.writerow(sol)

if __name__ == "__main__":
    main()
