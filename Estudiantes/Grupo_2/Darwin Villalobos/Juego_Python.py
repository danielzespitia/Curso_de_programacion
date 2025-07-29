print("NAVE ESPACIAL PERDIDA\n")

nivel1 = input("Estas situado en el hangar de la nave y observas dos pasillos: uno completamente oscuro y otro con un poco de iluminacion.\n¿Quieres ir por el PASILLO OSCURO o el PASILLO ILUMINADO?\n").lower()

if nivel1 == "pasillo iluminado":
    print("\nVas por el pasillo iluminado y encuentras una puerta con un panel numerico a su derecha(al parecer debes introducir una contraseña).")
    nivel2 = input("¿Quieres INTENTAR abrir la puerta, VOLVER atras o INSPECCIONAR el pasillo un poco mas?").lower()

    if nivel2 == "intentar":
        print("\nIntentas abrir la puerta, pero necesitas un codigo, el cual debes escribir en el PAD numerico. La puerta suelta un pitido y permanece cerrada.")
        nivel3 = input("¿Quieres PROBAR a introducir otro codigo o EXPLORAR el area en busca de pistas?").lower()

        if nivel3 == "probar":
            print("\nEl panel se bloquea debido a la cantidad de intentos fallidos. No puedes seguir por ahi.")
            print("Juego perdido")
        elif nivel3 == "explorar":
            print("\nEncuentras una nota con un numero, que dice: 7342. La ingresas en el PAD numerico y...¡LO TIENES! La puerta se abre.")
            nivel4 = input("Dentro hay dos caminos: una ESCALERA hacia arriba y un ASCENSOR viejo, en mal estado.\n¿Cual usaras? Se precavido...").lower()

            if nivel4 == "escalera":
                print("\nSubes con cuidado. Llegas a la cabina de mando.")
                nivel5 = input("¿Quieres ENVIAR una señal de auxilio o EXPLORAR el panel de control?").lower()

                if nivel5 == "enviar":
                    print("Logras enviar una señal de auxilio. Una nave espacial aliada viene a rescatarte. FIN DEL JUEGO")
                elif nivel5 == "explorar":
                    print("Encuentras que el sistema esta dañado. Pierdes demasiado tiempo y te quedas atrapado.")
                    print("Juego perdido")
                else:
                    print("Opcion no valida.")
            elif nivel4 == "ascensor":
                print("El ascensor se detiene entre pisos y quedas atrapado. Juego perdido")
            else:
                print("Opcion no valida.")
        else:
            print("Opcion no valida.")

    elif nivel2 == "volver":
        print("\nRegresas al hangar, pero lamentablemente la compuerta se ha cerrado detras de ti.")
        print("No puedes continuar. Juego perdido")
    elif nivel2 == "explorar":
        print("\nEncuentras una compuerta de mantenimiento.")
        nivel3_1 = input("¿Quieres ABRIRLA o IGNORARLA?").lower()

        if nivel3_1== "abrir":
            print("Te arrastras por una tuberia y llegas al sistema electrico de la nave!!.")
            nivel4_1 = input("¿Quieres REINICIAR el sistema o BUSCAR salidas alternas? Decidete rapido!!").lower()

            if nivel4_1 == "reiniciar":
                print("Reactivas parte de la nave, incluyendo el panel numerico anterior.")
                print("Puedes volver y avanzar. FIN DEL JUEGO")
            elif nivel4_1 == "buscar":
                print("Encuentras una salida alternativa. Escapas al espacio y para tu gran suerte te rescata otra nave.")
                print("FIN DEL JUEGO")
            else:
                print("Opcion no valida.")
        elif nivel3_1 == "ignorar":
            print("Tonto... perdiste una oportunidad de escape. Te quedas atrapado. Juego perdido")
        else:
            print("Opcion no valida.")
    else:
        print("Opcion no valida.")

elif nivel1 == "pasillo oscuro":
    print("\nCaminas por el pasillo oscuro. Escuchas ruidos muy locos y extraños... y tambien algo se mueve cerca.")
    nivel2 = input("¿Quieres ENCENDER tu linterna, CORRER hacia adelante o REGRESAR?").lower()

    if nivel2 == "encender":
        print("\nIluminas el pasillo y ves una figura extraña (como un fantasma) huyendo de ti.")
        nivel3 = input("¿Quieres SEGUIRLA o ENTRAR por una puerta lateral?").lower()

        if nivel3 == "seguirla":
            print("Resulta que la figura te lleva a una trampa. Juego perdido")
        elif nivel3 == "entrar":
            print("Procedes a ingresar y dentro encuentras un terminal de comunicacion de la nave.")
            nivel4 = input("¿Quieres ENVIAR MENSAJE o REVISAR ARCHIVOS?").lower()

            if nivel4 == "enviar":
                print("La señal de auxilio es enviada. Te salvan horas despues. FIN DEL JUEGO")
            elif nivel4 == "revisar":
                print("Los archivos que viste te revelan la ubicacion exacta de la capsula de escape.")
                nivel5 = input("¿Quieres IR a la capsula o QUEDARTE en el terminal?").lower()

                if nivel5 == "ir":
                    print("Encuentras la capsula en la ubicacion tal cual y escapas justo a tiempo. FIN DEL JUEGO")
                elif nivel5 == "quedarte":
                    print("La energia se agota y quedas atrapado. Juego perdido")
                else:
                    print("Opcion no valida.")
            else:
                print("Opcion no valida.")
        else:
            print("Opcion no valida.")

    elif nivel2 == "correr":
        print("Tropiezas y te das un fuerte golpe en la cabeza. Haz perdido el juego")

    elif nivel2 == "regresar":
        print("Te regresas al hangar, pero la compuerta se cierra y quedas totalmente atrapado. Haz perdido")
    else:
        print("Opcion no valida.")
else:
    print("Opcion no valida.")
