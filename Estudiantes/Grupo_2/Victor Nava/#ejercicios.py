#juego de la cueva

objeto1 = ("fosforo")
objeto2 = ("linterna")
accion1 = ("correr")
accion2 = ("esconderte")
accion3 = ("seguir")
accion4 = ("buscar")

print ("estas en un bosque oscuro y te encuentras dos objetos, un fosforo y una linterna, con cual te quedas?")
input ("cual te quedas?")
if objeto1:
    print(f"te quedas con el {objeto1} y lo enciendes por un instante, el bosque se ilumina y ves un gran oso grizzly! el fosforo se apaga. ¿quieres correr o esconderte detras de un arbol?")
    input("que haras?")
    if accion1:
        print("sales corriendo")
    elif accion2:
        print(" te escondes detras de un arbol")

elif objeto2:
    print(f"te quedas con la {objeto2} y la enciendes, ves un camino iluminado, de pronto, oyes algo entre los arboles. ¿quieres seguir el camino o buscar entre los arboles lo que hizo el ruido?")
    input("que haras?")
    if accion3:
        print("sigues el camino")
    elif accion4:
        print("buscas lo que hizo el ruido")












