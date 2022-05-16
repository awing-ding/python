import pyxel
from players import player_1, player_2
from ball import ball
from points import compteur
from background import background

"""par convention, le joueur de gauche est le joueur 1 est le joueur de droite le joueur 2 le joueur de gauche"""
_stop_victoire = False

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
        self.background = background.Background()
        self.player_left = player_1.Player1()
        self.player_right = player_2.Player2()
        self.ball = ball.Ball()
        self.compteur = compteur.Compteur()
        self.stop_victoire = _stop_victoire
        pyxel.run(self.update, self.draw)

    
    def point(self) -> None:
        """teste si un joueur gagne un point et l'attribue"""
        test = self.ball.point()
        if test == 1 :
            self.compteur.point_gauche += 1
        elif test == -1:
            self.compteur.point_droite += 1

    def victoire(self) -> None:
        """teste si un joueur a gagné"""
        if self.compteur.point_gauche == 10 or self.compteur.point_droite == 10:
            self.stop_victoire = True
            pyxel.init(128, 128, 'VICTOIRE !')
            if self.compteur.point_gauche == 10:
                pyxel.text(28, 28, 'Le joueur de gauche a gagné !', 7)
            if self.compteur.point_droite == 10:
                pyxel.text(28, 28, 'Le joueur de droite a gagné!', 7)
        _stop_victoire = self.stop_victoire
    
    def decorateur_victoire(fonction):
        
        def validateur_de_victoire(fonction):
            if not _stop_victoire:
                return fonction
                                
        return validateur_de_victoire



    @decorateur_victoire       
    def update(self)  -> None:
        """
        Elle s'occupe de la modification de l'état du jeu à chaque frame
        """
        self.player_left.move()
        self.player_right.move()
        self.ball.move(self.player_left.x, self.player_left.y, self.player_left.width, self.player_right.x, self.player_right.y)
        self.point()
        self.ball.debug_activation()

    @decorateur_victoire
    def draw(self)  -> None:
        """
        Elle s'occupe de l'affichage
        """
        pyxel.cls(0)
        self.compteur.draw()
        self.player_left.draw()
        self.player_right.draw()
        self.ball.draw(self.player_left.x, self.player_left.y, self.player_left.width, self.player_right.x, self.player_right.y)
        self.background.draw()