import pyxel
from players import player_1, player_2
from ball import ball

"""par convention, le joueur de gauche est le joueur 1 est le joueur de droite le joueur 2 le joueur de gauche"""

class Jeu:
    """
    La classe principale du jeu, elle initialise le module pyxel
    et fait fonctionner les différents éléments
    """


    def __init__(self)  -> None:
        """
        Elle initialise pyxel et les objets nécessaires puis lance le jeu 
        """
        pyxel.init(1024, 512, 'Pong', 30)
        self.player_left = player_1.Player1()
        self.player_right = player_2.Player2()
        self.ball = ball.Ball()
        self.point_joueur1 = 0
        self.point_joueur2 = 0
        pyxel.run(self.update, self.draw)


    def update(self)  -> None:
        """
        Elle s'occupe de la modification de l'état du jeu à chaque frame
        """
        self.player_left.move()
        self.player_right.move()
        self.ball.move(self.player_left.x, self.player_left.y, self.player_left.width, self.player_right.x, self.player_right.y)
        self.ball.point()


    def draw(self)  -> None:
        """
        Elle s'occupe de l'affichage
        """
        pyxel.cls(0)
        self.player_left.draw()
        self.player_right.draw()
        self.ball.draw()
    
    def point(self) -> None:
        """teste si un joueur gagne un point et l'attribue"""
        test = self.ball.point()
        if test == 1 :
            self.point_joueur2 += 1
        elif test == -1:
            self.point_joueur1 += 1
    