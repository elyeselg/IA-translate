import tkinter as tk
from tkinter import ttk
from googletrans import Translator

def traduire_texte():
    texte_a_traduire = texte_entree.get()
    langue_cible = langue_cible_entree.get()

    # Créer une instance du traducteur
    traducteur = Translator()

    # Traduire le texte
    traduction = traducteur.translate(texte_a_traduire, dest=langue_cible)

    texte_traduit.configure(text=traduction.text)

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Traducteur")
fenetre.geometry("800x500")

# Personnalisation du theme 
style = ttk.Style()
style.theme_use("clam")

# Créer les widgets avec un style personnalisé
frame = ttk.Frame(fenetre)
frame.pack(padx=10, pady=10)

label_texte = ttk.Label(frame, text="Texte à traduire:")
label_texte.grid(row=0, column=0, padx=5, pady=5, sticky="w")

texte_entree = ttk.Entry(frame, width=40)
texte_entree.grid(row=0, column=1, padx=5, pady=5)

label_langue_cible = ttk.Label(frame, text="Langue cible:")
label_langue_cible.grid(row=1, column=0, padx=5, pady=5, sticky="w")

langue_cible_entree = ttk.Entry(frame, width=10)
langue_cible_entree.grid(row=1, column=1, padx=5, pady=5)

bouton_traduire = ttk.Button(frame, text="Traduire", command=traduire_texte)
bouton_traduire.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

texte_traduit = ttk.Label(frame, text="", wraplength=300, foreground="blue")
texte_traduit.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Lancer la boucle principale de l'interface graphique
fenetre.mainloop()
