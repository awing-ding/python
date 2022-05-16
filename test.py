import pyxel
from points import nombre

pyxel.init(1024,512)
#pyxel.rect(0, 0, 5, 5, 1)
pyxel.load('my_resource.pyxres', True, False, False, False)
pyxel.blt(100, 100, 0, 0, 0, 8, 8)
nombre.Nombres.affichage(nombre.Nombres.tuple_5, 300, 300)
pyxel.flip()
pyxel.show()