import tkinter as tk

def calculer_salaire():
    """
    Cette fonction récupère les valeurs saisies dans les champs d'entrée et effectue le calcul du salaire.
    Elle met à jour les labels d'erreur et de résultat en fonction des valeurs entrées par l'utilisateur.
    """
    
    # Récupérer les valeurs saisies dans les champs de saisie
    # Les méthodes .get() sont utilisées pour récupérer les valeurs actuelles des champs d'entrée
    jours_travailles = champ_jours.get()
    heures_executees = champ_heures.get()
    taux_horaire = champ_taux.get()

    # Vérifier si tous les champs sont remplis
    # Les conditions suivantes vérifient que chaque champ est rempli et que la valeur ne correspond pas aux placeholders
    if not jours_travailles or not heures_executees or not taux_horaire or \
    jours_travailles == placeholders[0] or heures_executees == placeholders[1] or taux_horaire == placeholders[2]:
        # Afficher le message d'erreur en rouge
        # La méthode .config est utilisée pour mettre à jour la configuration du label d'erreur
        etiquette_erreur.config(text="Veuillez saisir tous les champs", fg="red")
        etiquette_resultat.config(text="0.00€") # Display 0.00€ in the result label if any field is not filled
    else:
        # Si tous les champs sont correctement remplis, convertir les valeurs en int ou float
        jours_travailles = float(jours_travailles)
        heures_executees = int(heures_executees)
        taux_horaire = float(taux_horaire)

        # Calculer le salaire en multipliant les jours travaillés, les heures exécutées et le taux horaire
        salaire = jours_travailles * heures_executees * taux_horaire

        # Afficher le salaire dans l'étiquette de résultat
        # {:.2f} dans la méthode .format signifie qu'on veut deux chiffres après la virgule
        etiquette_resultat.config(text="{:.2f} €".format(salaire))
        
        # Réinitialiser le message d'erreur et le mettre en gris
        etiquette_erreur.config(text="Merci d'avoir utilisé ce programme", fg="grey")

# Function to set placeholder
def set_placeholder(event, entry, placeholder):
    """
    Cette fonction est appelée lorsqu'un champ d'entrée obtient le focus.
    Elle vérifie si le contenu du champ correspond au placeholder et le remplace par une chaîne vide,
    en mettant également la couleur du texte en noir.
    """
    if entry.get() == placeholder:
        entry.delete(0, tk.END)  # Supprimer le contenu actuel du champ d'entrée
        entry.config(fg='black')  # Définir la couleur du texte sur noir

def unset_placeholder(event, entry, placeholder):
    """
    Cette fonction est appelée lorsqu'un champ d'entrée perd le focus.
    Elle vérifie si le champ est vide et remplace le champ par le placeholder,
    en mettant également la couleur du texte en gris.
    """
    if entry.get() == '':
        entry.insert(0, placeholder)  # Insérer le placeholder dans le champ d'entrée
        entry.config(fg='grey')  # Définir la couleur du texte sur gris


# Créer une fenêtre Tkinter
fenetre = tk.Tk()
fenetre.geometry("720x450")  # Mettre à jour la taille de la fenêtre
fenetre.title("Calcul ton salaire")

# Titre
titre = tk.Label(fenetre, text="Calcul ton salaire", font=("Arial", 16, "bold"))
titre.pack(pady=25)  # Ajouter de l'espace entre le titre et le tableau

# Tableau
tableau_frame = tk.Frame(fenetre)
tableau_frame.pack(pady=25) # Ajouter de l'espace entre le tableau et le bouton

# Fields placeholders (Texte à afficher dans les champs d'entrée)
placeholders = ["Nombre de jours travaillés", "Nombre d'heures exécutées par jour", "Taux horaire"]

# Field entries (Champs d'entrée)
champs = [tk.Entry(tableau_frame, width=40) for _ in range(3)]  # Crée une entrée plus large
champ_jours, champ_heures, champ_taux = champs  # Associe les champs d'entrée aux variables correspondantes

for i in range(3):
    intitule = tk.Label(tableau_frame, text=placeholders[i] + " :", width=35, anchor="w")
    intitule.grid(row=i, column=0, padx=20, pady=5)

    # Insérer le placeholder initial dans le champ d'entrée
    champs[i].insert(0, placeholders[i])
    champs[i].config(fg='grey')  # Définir la couleur du texte sur gris
    champs[i].bind('<FocusIn>', lambda event, entry=champs[i], placeholder=placeholders[i]: set_placeholder(event, entry, placeholder))
    champs[i].bind('<FocusOut>', lambda event, entry=champs[i], placeholder=placeholders[i]: unset_placeholder(event, entry, placeholder))
    champs[i].grid(row=i, column=1, padx=20, pady=5)  # Ajouter de l'espace à gauche et à droite

# Bouton de calcul
bouton_calculer = tk.Button(fenetre, text="Calculer", command=calculer_salaire)
bouton_calculer.pack(pady=35)  # Ajouter de l'espace après le bouton

# Étiquette de résultat
etiquette_resultat = tk.Label(fenetre, text="", font=("Arial", 20), fg="darkgreen")
etiquette_resultat.pack(pady=5)  # Ajouter de l'espace en dessous de l'étiquette de résultat

# Étiquette d'erreur
etiquette_erreur = tk.Label(fenetre, text="Veuillez saisir tous les champs", font=("Arial", 16), fg="grey")
etiquette_erreur.pack(pady=5)  # Ajouter de l'espace en dessous de l'étiquette d'erreur

# Boucle principale Tkinter
fenetre.mainloop()