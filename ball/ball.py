import pyxel
import random

class Ball:
    """"La classe de la balle"""


    def __init__(self) -> None:
        self.x = pyxel.width / 2
        self.y = pyxel.height / 2
        self.vitesse_x = 3
        self.vitesse_y = random.randint(1, 5)
        self.radius = pyxel.height / 48
        self.diameter = self.radius * 2

    def move(self, joueur1_x, joueur1_y, joueur1_width, joueur2_x, joueur2_y) -> None:
        """calcule le déplacement de la balle"""
        self.x = self.x + self.vitesse_x
        self.y = self.y + self.vitesse_y
        self.colision_player(joueur1_x, joueur1_y, joueur1_width, joueur2_x, joueur2_y)
        self.colision()
    
    def draw(self) -> None:
        """affiche la balle à l'écran"""
        pyxel.circ(self.x, self.y, self.radius, 7)
    

    def colision_player(self, joueur1_x, joueur1_y, joueur1_width, joueur2_x, joueur2_y) -> None:
        """teste si la balle a touché un élément"""
        if self.x <= (joueur1_x + joueur1_width):
            if self.y <= joueur1_y + pyxel.height / 6 and self.y >= joueur1_y + self.diameter:
                self.vitesse_verticale_colision(joueur1_y)
                self.vitesse_horizontale_colision()
        elif (self.x + self.radius * 2) >= joueur2_x :
            if self.y <= joueur2_y + pyxel.height / 6 and self.y >= joueur2_y + self.diameter:
                self.vitesse_verticale_colision(joueur2_y)
                self.vitesse_horizontale_colision()


    def vitesse_verticale_colision(self, joueur_y) -> None:
        """calcule la vitesse_y après la colision"""
        if self.vitesse_y >= 0:
            self.vitesse_y = self.vitesse_y + (abs(self.y - joueur_y + pyxel.height / 3)/96)
        else: 
            self.vitesse_y = self.vitesse_y - (abs(self.y - joueur_y + pyxel.height / 3)/96)

    def vitesse_horizontale_colision(self) -> None:
        """calcule la vitesse_x après la colision"""
        self.vitesse_x = self.vitesse_x * -1
    
    def colision(self) -> None:
        """défini si la balle touche un bord de l'écran et agit en conséquence"""
        if self.y <= 0 or (self.y + self.diameter) >= pyxel.height:
            self.vitesse_y = self.vitesse_y * -1
    
    def point(self) -> int:
        """défini si un joueur gagne 1 points, renvoie 1 si il s'agit du joueur 
        de droite, -1 si il s'agit du joueur de gauche"""
        if self.x <= 0:
            self.reset_position_point()
            return -1
        elif self.x + self.diameter >= pyxel.width:
            self.reset_position_point()
            return 1
    
    def reset_position_point(self) -> None:
        """remet la balle au centre si un joueur a un point"""
        self.x = pyxel.width/2
        self.vitesse_x = (self.vitesse_x * -1) +1
        self.vitesse_y = (self.vitesse_y * -1 ) / 5
