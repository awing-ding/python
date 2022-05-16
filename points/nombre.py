import pyxel

class Nombres:
    """Défini la matrice qui génerera les nombres"""
    tuple_0 = ( (0, 0, 0, 1, 1, 1, 1, 0, 0, 0),
                (0, 0, 1, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 1, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 1, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 1, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 1, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 1, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 1, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 1, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 1, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 0, 1, 1, 1, 1, 0, 0, 0)
              ) 
    tuple_1 = ( (0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
                (0, 0, 0, 0, 0, 1, 1, 0, 0, 0),
                (0, 0, 0, 0, 1, 0, 1, 0, 0, 0),
                (0, 0, 0, 1, 0, 0, 1, 0, 0, 0),
                (0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
                (0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
                (0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
                (0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
                (0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
                (0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
              ) 
    tuple_2 = ( (0, 0, 1, 1, 1, 1, 1, 1, 0, 0),
                (0, 0, 0, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 0, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 0, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 1, 1, 1, 1, 1, 1, 0, 0),
                (0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
                (0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
                (0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
                (0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
                (0, 0, 1, 1, 1, 1, 1, 1, 0, 0),
              )
    tuple_3 = ( (0, 0, 0, 1, 1, 1, 1, 1, 0, 0),
                (0, 0, 1, 0, 0, 0, 0, 0, 1, 0),
                (0, 0, 0, 0, 0, 0, 0, 0, 1, 0),
                (0, 0, 0, 0, 0, 0, 0, 0, 1, 0),
                (0, 0, 0, 1, 1, 1, 1, 1, 0, 0),
                (0, 0, 0, 0, 0, 0, 0, 0, 1, 0),
                (0, 0, 0, 0, 0, 0, 0, 0, 1, 0),
                (0, 0, 0, 0, 0, 0, 0, 0, 1, 0),
                (0, 0, 1, 0, 0, 0, 0, 0, 1, 0),
                (0, 0, 0, 1, 1, 1, 1, 1, 0, 0),
              )
    tuple_4 = ( (0, 0, 0, 0, 0, 1, 0, 0, 0, 0),
                (0, 0, 0, 0, 1, 0, 0, 0, 0, 0),
                (0, 0, 0, 1, 0, 0, 0, 0, 0, 0),
                (0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
                (0, 1, 0, 0, 0, 0, 0, 0, 0, 0),
                (1, 0, 0, 0, 0, 1, 0, 0, 0, 0),
                (1, 1, 1, 1, 1, 1, 1, 1, 0, 0),
                (0, 0, 0, 0, 0, 1, 0, 0, 0, 0),
                (0, 0, 0, 0, 0, 1, 0, 0, 0, 0),
                (0, 0, 0, 0, 0, 1, 0, 0, 0, 0),
              )
    tuple_5 = ( (0, 0, 1, 1, 1, 1, 1, 1, 0, 0),
                (0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
                (0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
                (0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
                (0, 0, 1, 1, 1, 1, 1, 1, 0, 0),
                (0, 0, 0, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 0, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 0, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 0, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 1, 1, 1, 1, 1, 1, 0, 0),
              )
    tuple_6 = ( (0, 0, 1, 1, 1, 1, 1, 1, 0, 0),
                (0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
                (0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
                (0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
                (0, 0, 1, 1, 1, 1, 1, 1, 0, 0),
                (0, 0, 1, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 1, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 1, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 1, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 0, 1, 1, 1, 1, 0, 0, 0),
              )
    tuple_7 = ( (0, 0, 1, 1, 1, 1, 1, 1, 0, 0),
                (0, 0, 0, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 0, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 0, 0, 0, 1, 1, 1, 0, 0),
                (0, 0, 0, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 0, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 0, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 0, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 0, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 0, 0, 0, 0, 0, 1, 0, 0),
    )
    tuple_8 = ( (0, 0, 0, 1, 1, 1, 1, 0, 0, 0),
                (0, 0, 1, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 1, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 1, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 0, 1, 1, 1, 1, 0, 0, 0),
                (0, 0, 1, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 1, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 1, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 1, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 1, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 0, 1, 1, 1, 1, 0, 0, 0),
              ) 
    tuple_9 = ( (0, 0, 0, 1, 1, 1, 1, 0, 0, 0),
                (0, 0, 1, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 1, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 1, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 1, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 0, 1, 1, 1, 1, 1, 0, 0),
                (0, 0, 0, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 0, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 0, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 1, 1, 1, 1, 1, 1, 0, 0),
              )
    tuple_separateur = ((0, 0, 0, 0, 1, 1, 0, 0, 0, 0),
                        (0, 0, 0, 0, 1, 1, 0, 0, 0, 0),
                        (0, 0, 0, 0, 1, 1, 0, 0, 0, 0),
                        (0, 0, 0, 0, 1, 1, 0, 0, 0, 0),
                        (0, 0, 0, 0, 1, 1, 0, 0, 0, 0),
                        (0, 0, 0, 0, 1, 1, 0, 0, 0, 0),
                        (0, 0, 0, 0, 1, 1, 0, 0, 0, 0),
                        (0, 0, 0, 0, 1, 1, 0, 0, 0, 0),
                        (0, 0, 0, 0, 1, 1, 0, 0, 0, 0),
                        (0, 0, 0, 0, 1, 1, 0, 0, 0, 0),
                       )
               

    def affichage(tuple_nombre, x_depart, y_depart):
        """lit la matrice dans le tuple pour générer une image"""
        pyxel.load('my_resource.pyxres', True, False, False, False)
        for y in range(len(tuple_nombre)) :
            for x in range(len(tuple_nombre[y])) :
                if tuple_nombre[y][x] :
                    pyxel.blt(x_depart + x * 7, y_depart + y * 7, 0, 48, 0, 8, 8)
                else :
                    pyxel.blt(x_depart + x * 7, y_depart + y * 7, 0, 48, 8, 8, 8)