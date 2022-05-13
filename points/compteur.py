from tkinter.messagebox import NO


import pyxel

class Compteur:

    def __init__(self) -> None:
        self.point_gauche = 0
        self.point_droite = 0

    
    def draw(self) -> None:
        point = str(self.point_gauche) + "|" + str(self.point_droite)
        pyxel.text(pyxel.width / 3, 8, point, 7)