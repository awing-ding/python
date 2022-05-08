import pyxel

class Player1:
    """
    La classe qui définit la raquette gauche.
    """

    def __init__(self):
        self.x = 8
        self.y = pyxel.height / 2


    def move(self) :
        """la fonction qui capte le déplacement"""
        if pyxel.btn(pyxel.KEY_Z) and self.y > 0:
            self.y -= 1
        if pyxel.btn(pyxel.KEY_S) and self.y < pyxel.height:
            self.y += 1


    def draw(self) :
        """la fonction qui dessine le vaisseau à l'écran"""
        pyxel.rect(self.x, self.y, 2, 16, 1)