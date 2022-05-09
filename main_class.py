import pyxel
from players import player_1, player_2

class Jeu:
    """
    La classe principale du jeu, elle initialise le module pyxel
    et fait fonctionner les différents éléments
    """


    def __init__(self)  -> None:
        """
        Elle initialise pyxel et les objets nécessaires puis lance le jeu 
        """
        pyxel.init(256, 128, 'Pong', 30)
        self.player_left = player_1.Player1()
        self.player_right = player_2.Player2()
        pyxel.run(self.update, self.draw)


    def update(self)  -> None:
        """
        Elle s'occupe de la modification de l'état du jeu à chaque frame
        """
        self.player_left.move()
        self.player_right.move()


    def draw(self)  -> None:
        """
        Elle s'occupe de l'affichage
        """
        pyxel.cls(0)
        self.player_left.draw()
        self.player_right.draw()