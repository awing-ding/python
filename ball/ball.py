import pyxel

class Ball:
    """"La classe de la balle"""


    def __init__(self) -> None:
        self.x = pyxel.width / 2
        self.y = pyxel.height / 2
        self.vitesse_x = 1
        self.vitesse_y = 1


    def move(self) -> None:
        """calcule le déplacement de la balle"""
        pass
    
    def draw(self) -> None:
        """affiche la balle à l'écran"""
        pyxel.circ(self.x, self.y, 4.0, 2)
    

    def collision(self, joueur1_x, joueur1_y, joueur2_x, joueur2_y) -> None:
        """teste si la balle a touché un élément"""
        if self.x <= (joueur1_x + 2):
            if self.y <= joueur1_y + 16 and self.y >= joueur1_y + 4:
                pass
        elif (self.x + 4) >= joueur2_x :
            if self.y <= joueur1_y + 16 and self.y >= joueur2_y + 4:
                pass