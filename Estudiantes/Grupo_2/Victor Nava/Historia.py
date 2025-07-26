#juego de la cueva



print ("estas en un bosque oscuro y te encuentras dos objetos, un fosforo y una linterna, con cual te quedas?")
hola= input ("cual te quedas?")
if hola == "fosforo":
    print(f"te quedas con el fosforo y lo enciendes por un instante, el bosque se ilumina y ves un gran oso grizzly! el fosforo se apaga. ¿quieres correr o esconderte detras de un arbol?")
    hola1=input("que haras?")
    if hola1 == "correr":
        print("sales corriendo pero el oso te alcanza, puedes luchar, hacerte el muerto o aceptar tu destino")
        hola3=input("que haras?")
        if hola3 == "luchar" :
            print("luchas con el oso")
        elif hola3 == "hacerte el muerto":
            print("te haces el muerto y el oso te ignora")
        else:
            print(" aceptas tu destino y mueres")
    elif hola1 == "esconderte":
        print(" te escondes detras de un arbol y el oso te pierde de vista, quieres seguir explorando, darte la vuelta o descansar")
        hola4=input("que haras?")
        if hola4 == "seguir explorando":
            print("sigues explorando el bosque y encuentras la guarida del oso")
        elif hola4 == "darte la vuelta":
            print("te das la vuelta y abandonas el bosque oscuro")
        else:
            print("descansas durmiendo al pie del arbol")


elif hola == "linterna":
    print(f"te quedas con la linterna y la enciendes, ves un camino iluminado, de pronto, oyes algo entre los arboles. ¿quieres seguir el camino o buscar entre los arboles lo que hizo el ruido?")
    hola2=input("que haras?")
    if hola2 == "seguir":
        print("sigues el camino y sales del bosque, pero te encuentras acribillado por unos bandidos y te desafian a un duelo a muerte con cuchillos, que haras? peleas con ellos, huyes al bosque o te entregas como esclavo")
        hola5=input("que haras?")
        if hola5 == "peleas con ellos":
            print("peleas con ellos y sales victorioso")
        elif hola5 == "huyes al bosque":
            print("huyes al bosque y te encuentras de frente un no-muerto el cual te come vivo")
        else:
            print("te entregas como esclavo y te torturan")
    elif hola2 == "buscar":
        print("buscas lo que hizo el ruido y te encuentras un oso bebe, puedes matarlo para hacerte un abrigo, buscar a su madre o ignorarlo e irte")
        hola6=input("que haras?")
        if hola6 == "matarlo para hacerte un abrigo":
            print("lo matas pero el abrigo no te queda")
        elif hola6 == "buscar a su madre":
            print("buscas a la madre del oso bebe la cual te agradece por devolverle a su hija y se vuelven tus acompañantes")
        else:
            print("ignoras al bebe oso")

else:
    print("no escoges ninguno, te quedas a oscuras")











