import tkinter as tk

# Créer la fenêtre principale
root = tk.Tk()
root.title("Dimi's Game")

# Définir la taille de la fenêtre (largeur x hauteur)
root.geometry("400x300")  # Par exemple, 400 pixels de large et 300 pixels de haut

# Changer la police d'écriture
font_style = ("Helvetica", 16, "bold")  # Nom de la police, taille, style

# Créer un label avec le texte centré
label = tk.Label(root, text="Hello!", font=font_style)
label.pack(expand=True)  # Utiliser expand=True pour centrer

# Lancer la boucle principale
root.mainloop()
