import pyxel

class Player2:
    """
    La classe qui définit la raquette de droite
    """

    def __init__(self):
        self.x = pyxel.width - 8
        self.y = pyxel.height / 2


    def move(self) :
        """la fonction qui capte le déplacement"""
        if pyxel.btn(pyxel.KEY_UP) and self.y > 0:
            self.y -= 1
        if pyxel.btn(pyxel.KEY_DOWN) and self.y < pyxel.height:
            self.y += 1

            
    def draw(self) :
        """la fonction qui dessine le vaisseau à l'écran"""
        pyxel.rect(self.x, self.y, 2, 8, 1)