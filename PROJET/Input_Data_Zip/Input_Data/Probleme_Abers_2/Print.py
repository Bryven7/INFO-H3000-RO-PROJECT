import pickle

# Chemin vers votre fichier .pickle
chemin_fichier = "Input_Data_Zip/Input_Data/Probleme_Abers_2/bilat_pairs_Abers_pb2.pickle"

# Ouvrir le fichier .pickle en mode lecture binaire (rb)
with open(chemin_fichier, 'rb') as fichier:
    # Charger les données à partir du fichier .pickle
    obj = pickle.load(fichier)

# Ouvrir un fichier texte en mode écriture (w+ pour création s'il n'existe pas)
with open("Input_Data_Zip/Input_Data/Probleme_Abers_2/bilat_pairs_Abers_pb2.txt", "w+") as fichier_resultat:
    # Écrire chaque ligne dans le fichier texte
    for row in obj:
        fichier_resultat.write(str(row) + "\n")
