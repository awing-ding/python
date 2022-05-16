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
        self.debug = False

    def move(self, joueur1_x, joueur1_y, joueur1_width, joueur2_x, joueur2_y) -> None:
        """calcule le déplacement de la balle"""
        self.x = self.x + self.vitesse_x
        self.y = self.y + self.vitesse_y
        self.colision_player(joueur1_x, joueur1_y, joueur1_width, joueur2_x, joueur2_y)
        self.colision()
    
    def draw(self, joueur1_x, joueur1_y, joueur1_width, joueur2_x, joueur2_y) -> None:
        """affiche la balle à l'écran"""
        pyxel.circ(self.x, self.y, self.radius, 7)
        if self.debug:
            pyxel.rectb(self.x - self.radius, self.y - self.radius, self.diameter, self.diameter, 1)
            pyxel.rectb(joueur1_x, joueur1_y - self.radius, joueur1_width, pyxel.height / 6 + self.radius, 2)
            pyxel.rectb(joueur2_x, joueur2_y - self.radius, joueur1_width, pyxel.height / 6 + self.radius, 2)
    

    def colision_player(self, joueur1_x, joueur1_y, joueur1_width, joueur2_x, joueur2_y) -> None:
        """teste si la balle a touché un élément"""
        if self.x - self.radius <= (joueur1_x + joueur1_width):
            if self.y <= joueur1_y + pyxel.height / 6 and self.y >= joueur1_y - self.radius:
                self.vitesse_verticale_colision(joueur1_y)
                self.vitesse_horizontale_colision()
                self.vitesse_x = self.vitesse_x * 1.5
                self.vitesse_y = self.vitesse_y * 1.5
        elif (self.x + self.radius) >= joueur2_x :
            if self.y <= joueur2_y + pyxel.height / 6 and self.y >= joueur2_y - self.radius:
                self.vitesse_verticale_colision(joueur2_y)
                self.vitesse_horizontale_colision()
                self.vitesse_x = self.vitesse_x * 1.5
                self.vitesse_y = self.vitesse_y * 1.5


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
        if self.y - self.radius <= 0 or (self.y + self.radius) >= pyxel.height:
            self.vitesse_y = self.vitesse_y * -1
    
    def point(self) -> int:
        """défini si un joueur gagne 1 points, renvoie 1 si il s'agit du joueur 
        de droite, -1 si il s'agit du joueur de gauche"""
        if self.x - self.radius <= 0:
            self.reset_position_point()
            return -1
        elif self.x + self.radius >= pyxel.width:
            self.reset_position_point()
            return 1
    
    def reset_position_point(self) -> None:
        """remet la balle au centre si un joueur a un point"""
        self.x = pyxel.width/2
        self.vitesse_x = (self.vitesse_x * -1) / self.vitesse_x
        self.vitesse_y = random.randint(1, 5)


    def debug_activation(self) -> None:
        """active le debug mode"""
        if pyxel.btn(pyxel.KEY_D):
            if self.debug :
                self.debug = False
            else :
                self.debug = True