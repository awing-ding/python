import pyxel

class Background:
    """une classe simple qui ne définit que quelques éléments graphique"""
    def draw(self) -> None:
        """dessine la ligne du milieu"""
        __milieu = pyxel.width / 2
        for i in range(pyxel.height):
            if i % 8 == 0:
                pyxel.rect(__milieu, i, 2, 2, 13)