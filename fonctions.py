import tkinter as tk
import fonctions
from joueur import Player

def DémarrerPartie(menu):
    # Effacer le contenu du canvas existant
    menu.canvas.delete("all")
    # Changer la couleur du fond
    menu.canvas.configure(bg='white')
    # Supprimer les boutons du menu
    menu.quit_button.destroy()
    menu.launch_button.destroy()
    
    # Créer le nouveau bouton retour menu
    # Il sera positionné au même endroit que l'ancien bouton quitter
    menu.return_button = tk.Button(menu.window, text='Retour Menu', command=lambda: RetourMenu(menu), bg='red', fg='white')
    menu.return_button.place(relx=1.0, x=-10, y=10, anchor="ne")

    menu.player = Player(menu.canvas)


def RetourMenu(menu):
    # Effacer le canvas
    menu.canvas.delete("all")
    # Remettre le fond noir
    menu.canvas.configure(bg='black')
    # Supprimer le bouton retour
    menu.return_button.destroy()
    # Recharger le logo
    menu.load_logo()
    # Recréer les boutons du menu
    menu.create_buttons()