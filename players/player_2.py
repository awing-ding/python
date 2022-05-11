import pyxel

class Player2:
    """
    La classe qui définit la raquette de droite
    """

    def __init__(self)  -> None:
        self.x = pyxel.width - 8
        self.y = pyxel.height / 2
        self.height = pyxel.height / 6
        self.width = self.height / 8


    def move(self)  -> None:
        """la fonction qui capte le déplacement"""
        if pyxel.btn(pyxel.KEY_UP) and self.y > 0:
            self.y -= 1
        if pyxel.btn(pyxel.KEY_DOWN) and self.y + self.height < pyxel.height:
            self.y += 1

            
    def draw(self)  -> None:
        """la fonction qui dessine le vaisseau à l'écran"""
        pyxel.rect(self.x, self.y, self.width, self.height, 1)