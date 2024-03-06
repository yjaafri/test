from moyenne import calculer_moyenne_3_meilleures

nom_fichier = "note.txt"
nom_fichier_sortie = "résultat.txt"

try:
  with open(nom_fichier, 'r') as fichier, open(nom_fichier_sortie,
                                               'w') as sortie:
    for ligne in fichier:
      elements = ligne.split()
      nom = elements[0]
      prenom = elements[1]
      notes = [int(note) for note in elements[2:]] if elements[2:] else []
      moyenne = calculer_moyenne_3_meilleures(notes)
      if moyenne is None:
        sortie.write(f"{nom} {prenom} : Non noté(e)\n")
      else:
        sortie.write(f"{nom} {prenom} : {moyenne:.2f}\n")
except FileNotFoundError:
  print(f"Le fichier {nom_fichier} n'a pas été trouvé.")
except Exception as e:
  print(f"Une erreur est survenue : {e}")
