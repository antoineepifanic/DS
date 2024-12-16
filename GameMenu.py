import tkinter as tk
from PIL import Image, ImageTk
import fonctions

class GameMenu:
    def __init__(self, window):
        self.window = window

        # Canvas directement dans la fenêtre
        self.canvas = tk.Canvas(window, bg='black', width=600, height=600)
        self.canvas.pack(expand=True)  # Centrer le canvas dans la fenêtre
        
        self.create_buttons()
        self.load_logo()
        
    def load_logo(self):
        logo_image = Image.open("ressources/logospaceinvaders.jpg")
        logo_image = logo_image.resize((400, 200))
        self.logo = ImageTk.PhotoImage(logo_image)
        self.canvas.create_image(300, 200, image=self.logo) 
        
    def create_buttons(self):
        # Bouton "Quitter" positionné en haut à droite
        self.quit_button = tk.Button(self.window, text='Quitter', command=self.window.destroy, bg='red', fg='white')
        self.quit_button.place(relx=1.0, x=-10, y=10, anchor="ne")
        # Bouton "Démarrer Partie" positionné au centre en bas
        self.launch_button = tk.Button(self.window, text='Démarrer', command=lambda : fonctions.DémarrerPartie(self))
        self.launch_button.place(relx=0.5, rely=0.9, anchor='center')

# Création de la fenêtre
fenetre = tk.Tk()
fenetre.title('Space Invaders')
fenetre.geometry('800x800')

game_menu = GameMenu(fenetre)
fenetre.mainloop()