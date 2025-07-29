import time

def jugar_juego():
    print("Estavas en una fiesta y te raptaron y de repronto apareses en un lugar extraño.")
    print("Y sigues caminando para poder escapar del lugar y de repente todo se oscurese👤 y encuentras tres  objetos: un *llave*🕯️ , *linterna*🔦 o una *escopeta*.")
    print("¿Con cual te quedas? (Escribe  'llave','linterna','escopeta'.)")

    eleccion_inicial = input().lower()

    if eleccion_inicial == "llave":
        print("\nCoges la llave y encuentras por la oscuridad una serradura. Por un instante, el lugar  se ilumina... y ves un espanto!.")
        time.sleep(2)
        print("Quieres *CORRER* o *ESCONDERTE* detras de una silla?")
        eleccion_llave = input().lower()

        if eleccion_llave== "correr":
            print("\nCorres tan rapido como puedes, y elespanto ya no esta. Felicidades,y encuentras una salida ,pudiste salir ! ")
        elif eleccion_llave == "esconderte":
            print("\nTe escondes detras de una silla vieja y el espanto te encontro ")
        else:
            print("\nDecision no valida. El espanto te encuentra. Fin del juego. ")

    elif eleccion_inicial == "linterna":
        print("\nEnciendes la linterna 🔦 y ves un camino iluminado. De pronto, oyes que algo se cayo.")
        time.sleep(2)
        print("Quieres *SEGUIR* el camino o *BUSCAR* que fue lo que hizo ruido?")
        eleccion_linterna = input().lower()

        if eleccion_linterna == "seguir":
            print("\nSigues el camino iluminado🔦. Aunque algo se cayo, confias en tu linterna. Felicidades, encuentras una llave! ")
            print("\nY con tu linterna y la llave,pudiste conseguir la salida felicidades")
 
        elif eleccion_linterna == "buscar":
            print("\nDecides buscar el origen del ruido y te encuentras con el espanto! ")
        else:
            print("\nDecision no valida. Te quedas inmovil por el espanto. Fin del juego. ")


    if eleccion_inicial == "escopeta":
        print("\nCoges la escopeta y encuentras por la oscuridad un espanto ,!ATRAS TULLO HAY UNA mesa!.")
        time.sleep(2)
        print("Quieres *buscar* o *disparar* detras de la mesa?")
        eleccion_escopeta = input().lower()

        if eleccion_escopeta == "buscar":
            print("\nencuentras balas y lo matas  y encuentras la llave ensima del espanto  ! ")
            print("Has ganado")

        elif eleccion_escopeta == "disparar":
            print("\nno tienes balas   ")
            print("EL ESPANTO TE ENCUENTRA FIN DELJUEGO")
       
    else:
        print("\nEleccion no valida. Te quedas sin balas y te encuentras con elespanto. Fin del juego. ")

    print("\n--- Fin del juego ---")

# Para jugar, llama a la funcion:
jugar_juego()