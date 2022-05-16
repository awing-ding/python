import pyxel
from nombre import Nombres

class Compteur:
    """la classe qui gère le comptage et l'affichage des points"""

    def __init__(self) -> None:
        self.point_gauche = 0
        self.point_droite = 0
        self.x = pyxel.width / 3
        self.y = 8

    
    def draw(self) -> None:
        """affiche le nombre de point à l'écran"""
        str_point = self.point_to_string()       
        for i in range(str_point):
            try: #teste si le caractère obtenu est un nombre, si non, affiche un séparateur
                number_point = int(str_point[i])
            except ValueError:
                Nombres.affichage(Nombres.tuple_separateur, self.x, self.y)

            if number_point == 0: #affiche l'image correspondand au nombre
                Nombres.affichage(Nombres.tuple_0, self.x, self.y)
            elif number_point == 1:
                Nombres.affichage(Nombres.tuple_1, self.x, self.y)
            elif number_point == 2:
                Nombres.affichage(Nombres.tuple_2, self.x, self.y)
            elif number_point == 3:
                Nombres.affichage(Nombres.tuple_3, self.x, self.y)
            elif number_point == 4:
                Nombres.affichage(Nombres.tuple_4, self.x, self.y)
            elif number_point == 5:
                Nombres.affichage(Nombres.tuple_5, self.x, self.y)
            elif number_point == 6:
                Nombres.affichage(Nombres.tuple_6, self.x, self.y)
            elif number_point == 7:
                Nombres.affichage(Nombres.tuple_7, self.x, self.y)
            elif number_point == 8:
                Nombres.affichage(Nombres.tuple_8, self.x, self.y)
            elif number_point == 9:
                Nombres.affichage(Nombres.tuple_9, self.x, self.y)

            self.x = self.x + 70 #incrémente de 70 (la largeur d'une image) à chaque fois qu'une image est affiché
    
    def point_to_string(self) -> str:
        """converti le nombre de point en un string caracteristique"""
        str_point = str(self.point_gauche) + "|" + str(self.point_droite)
        return str_point

