def normalizar_texto(texto):
    """
    Convierte el texto a mayúsculas y reemplaza caracteres acentuados
    por sus equivalentes sin acento para una comparación flexible.
    """
    texto = texto.upper()
    texto = texto.replace('Á', 'A')
    texto = texto.replace('É', 'E')
    texto = texto.replace('Í', 'I')
    texto = texto.replace('Ó', 'O')
    texto = texto.replace('Ú', 'U')
    texto = texto.replace('Ü', 'U') # Para la diéresis si alguna vez se usara
    return texto

def jugar_aventura():
    print("Estás caminando por un bosque oscuro y encuentras dos objetos: un fósforo y una linterna. ¿Con cuál te quedas?")

    # Aplica normalizar_texto a cada entrada del usuario
    primera_decision = normalizar_texto(input("¿FÓSFORO o LINTERNA? "))

    if primera_decision == "FOSFORO": # Ahora comparamos con la versión sin acento
        print("\nCoges el fósforo y lo enciendes. Por un instante, el bosque se ilumina... ¡y ves un gran oso grizzly! El fósforo se apaga.")
        segunda_decision_fosforo = normalizar_texto(input("¿Quieres CORRER o ESCONDERTE detrás de un árbol? "))

        if segunda_decision_fosforo == "CORRER":
            print("\nCorres tan rápido como puedes. El oso te persigue por un momento, pero logras perderlo. Te encuentras con un río caudaloso.")
            tercera_decision_correr = normalizar_texto(input("¿Quieres CRUZAR el río, RODEARLO o CONSTRUIR una balsa? "))

            if tercera_decision_correr == "CRUZAR":
                print("\nIntentas cruzar el río, pero la corriente es demasiado fuerte y te arrastra. Fin del juego.")
            elif tercera_decision_correr == "RODEAR":
                print("\nDecides rodear el río. Después de un largo camino, encuentras un claro con una cabaña abandonada. Parece seguro.")
                cuarta_decision_rodear = normalizar_texto(input("¿Quieres ENTRAR en la cabaña, IGNORARLA y seguir, o BUSCAR comida cerca? "))
                if cuarta_decision_rodear == "ENTRAR":
                    print("\nEntras en la cabaña. Está oscura y polvorienta, pero encuentras un mapa viejo. Continúas tu aventura con más información.")
                    quinta_decision_mapa = normalizar_texto(input("El mapa muestra un PUEBLO cercano, unas RUINAS antiguas o una MONTAÑA imponente. ¿A dónde quieres ir? "))
                    if quinta_decision_mapa == "PUEBLO":
                        print("\nSigues el camino hacia el pueblo. Finalmente llegas a un lugar seguro y lleno de gente. ¡Has sobrevivido! Fin del juego.")
                    elif quinta_decision_mapa == "RUINAS":
                        print("\nTe diriges a las ruinas. Allí descubres un tesoro escondido, pero también despiertas a un antiguo guardián. Luchas valientemente. Fin del juego (resultado variable).")
                    elif quinta_decision_mapa == "MONTANA": # Cambiado a MONTANA sin acento
                        print("\nDecides escalar la montaña. El camino es duro, pero desde la cima ves el vasto paisaje y encuentras una señal de ayuda. Eres rescatado. ¡Has sobrevivido! Fin del juego.")
                    else:
                        print("Opción no válida. Intenta de nuevo.")
                elif cuarta_decision_rodear == "IGNORARLA":
                    print("\nDecides ignorar la cabaña y sigues caminando. La noche cae y el frío te consume. Fin del juego.")
                elif cuarta_decision_rodear == "BUSCAR":
                    print("\nBuscas comida cerca de la cabaña. Encuentras algunas bayas, pero algunas son venenosas y te enfermas gravemente. Fin del juego.")
                else:
                    print("Opción no válida. Intenta de nuevo.")

            elif tercera_decision_correr == "CONSTRUIR":
                print("\nReúnes ramas y hojas para construir una balsa rudimentaria. Logras cruzar el río con éxito y sigues tu camino.")
                cuarta_decision_balsa = normalizar_texto(input("Una extraña niebla se acerca. ¿Quieres ADENTRARTE, ESPERAR a que se disipe o BUSCAR refugio? "))
                if cuarta_decision_balsa == "ADENTRARTE":
                    print("\nTe adentras en la niebla. Pierdes el sentido de la orientación y te caes por un barranco. Fin del juego.")
                elif cuarta_decision_balsa == "ESPERAR":
                    print("\nEsperas pacientemente a que la niebla se disipe. Cuando lo hace, el sol ilumina un sendero claro. Lo sigues y encuentras una aldea amigable. ¡Has sobrevivido! Fin del juego.")
                elif cuarta_decision_balsa == "BUSCAR":
                    print("\nBuscas refugio y encuentras una cueva. Dentro, te espera una criatura desconocida. Lucha por tu vida. Fin del juego (resultado variable).")
                else:
                    print("Opción no válida. Intenta de nuevo.")

            else:
                print("Opción no válida. Intenta de nuevo.")

        elif segunda_decision_fosforo == "ESCONDERTE":
            print("\nTe escondes rápidamente detrás de un árbol. El oso pasa de largo sin verte. Suspiras de alivio, pero ahora estás solo y perdido.")
            tercera_decision_esconderte = normalizar_texto(input("Escuchas un aullido distante. ¿Quieres SEGUIR el sonido, IGNORARLO y caminar en dirección opuesta, o TREPAR a un árbol para ver mejor? "))

            if tercera_decision_esconderte == "SEGUIR":
                print("\nSigues el aullido. Te lleva a una manada de lobos. Te atacan. Fin del juego.")
            elif tercera_decision_esconderte == "IGNORARLO":
                print("\nDecides ignorar el aullido y caminas en dirección opuesta. La oscuridad te envuelve y te sientes cada vez más frío. Finalmente, te desorientas por completo y no encuentras la salida. Fin del juego.")
            elif tercera_decision_esconderte == "TREPAR":
                print("\nTrepas a un árbol. Desde las alturas, ves una luz a lo lejos. Parece ser un campamento.")
                cuarta_decision_trepar = normalizar_texto(input("¿Quieres BAJAR y dirigirte al campamento, QUEDARTE en el árbol hasta el amanecer o BUSCAR otro camino? "))
                if cuarta_decision_trepar == "BAJAR":
                    print("\nBajas del árbol y te diriges al campamento. Descubres que es un grupo de exploradores amigables. Te ofrecen ayuda y te guían de regreso a la civilización. ¡Has sobrevivido! Fin del juego.")
                elif cuarta_decision_trepar == "QUEDARTE":
                    print("\nDecides quedarte en el árbol hasta el amanecer. El frío de la noche te hace sufrir, pero al amanecer puedes ver un camino claro. Lo sigues y encuentras un pueblo. ¡Has sobrevivido! Fin del juego.")
                elif cuarta_decision_trepar == "BUSCAR":
                    print("\nBuscas otro camino desde el árbol. Ves un pequeño sendero que parece llevar a una cueva. Bajas y te adentras en ella. Dentro encuentras un tesoro, pero también quedas atrapado por un derrumbe. Fin del juego.")
                else:
                    print("Opción no válida. Intenta de nuevo.")
            else:
                print("Opción no válida. Intenta de nuevo.")

        else:
            print("Opción no válida. Intenta de nuevo.")

    elif primera_decision == "LINTERNA":
        print("\nEnciendes la linterna y ves un camino iluminado. De pronto, oyes algo entre los árboles.")
        segunda_decision_linterna = normalizar_texto(input("¿Quieres SEGUIR el camino o BUSCAR entre los árboles lo que hizo el ruido? "))

        if segunda_decision_linterna == "SEGUIR":
            print("\nSigues el camino iluminado. Te lleva a una antigua mansión abandonada.")
            tercera_decision_seguir = normalizar_texto(input("¿Quieres ENTRAR en la mansión, RODEARLA o ESCONDERTE y observar? ")) # Cambiado a RODEARLA sin acento

            if tercera_decision_seguir == "ENTRAR":
                print("\nEntras en la mansión. Está llena de telarañas y muebles viejos. De repente, una puerta se cierra de golpe detrás de ti.")
                cuarta_decision_entrar = normalizar_texto(input("¿Quieres BUSCAR una salida, GRITAR pidiendo ayuda o EXPLORAR las habitaciones? "))
                if cuarta_decision_entrar == "BUSCAR":
                    print("\nBuscas desesperadamente una salida y encuentras un pasadizo secreto que te lleva al exterior. ¡Has escapado! Fin del juego.")
                elif cuarta_decision_entrar == "GRITAR":
                    print("\nGritas pidiendo ayuda, pero solo consigues atraer a una presencia fantasmal. Fin del juego.")
                elif cuarta_decision_entrar == "EXPLORAR":
                    print("\nExploras las habitaciones y encuentras un diario antiguo que revela la historia de la mansión. Aprendes un oscuro secreto y te sientes perseguido. Fin del juego (resultado variable).")
                else:
                    print("Opción no válida. Intenta de nuevo.")
            elif tercera_decision_seguir == "RODEARLA":
                print("\nDecides rodear la mansión. Encuentras un jardín descuidado con un pozo misterioso. Sientes una extraña atracción.")
                cuarta_decision_rodear_mansion = normalizar_texto(input("¿Quieres ASOMARTE al pozo, LANZAR una piedra para escuchar el eco o IGNORARLO y seguir tu camino? "))
                if cuarta_decision_rodear_mansion == "ASOMARTE":
                    print("\nTe asomas al pozo y una fuerza invisible te arrastra hacia abajo. Fin del juego.")
                elif cuarta_decision_rodear_mansion == "LANZAR":
                    print("\nLanzas una piedra al pozo. Escuchas un eco prolongado y luego un sonido metálico. Curioso, encuentras una pequeña caja fuerte al fondo del pozo. Dentro hay joyas y un mensaje que te guía a un lugar seguro. ¡Has encontrado un tesoro y sobrevivido! Fin del juego.")
                elif cuarta_decision_rodear_mansion == "IGNORARLO":
                    print("\nDecides ignorar el pozo y sigues tu camino. Eventualmente, llegas a una carretera y encuentras ayuda. ¡Has sobrevivido! Fin del juego.")
                else:
                    print("Opción no válida. Intenta de nuevo.")
            elif tercera_decision_seguir == "ESCONDERTE":
                print("\nTe escondes entre los arbustos y observas la mansión. Ves una figura oscura entrando por la puerta principal. Decides no arriesgarte y te alejas sigilosamente, buscando un camino más seguro.")
                cuarta_decision_esconderte_mansion = normalizar_texto(input("A lo lejos ves una luz intermitente. ¿Quieres ACERCARTE a ella, EVITARLA y seguir por el bosque o VOLVER sobre tus pasos? "))
                if cuarta_decision_esconderte_mansion == "ACERCARTE":
                    print("\nTe acercas a la luz y descubres que es una trampa de cazadores. Quedas atrapado. Fin del juego.")
                elif cuarta_decision_esconderte_mansion == "EVITARLA":
                    print("\nEvitas la luz y sigues por el bosque. Después de un tiempo, encuentras un sendero señalizado que te lleva a un pueblo. ¡Has sobrevivido! Fin del juego.")
                elif cuarta_decision_esconderte_mansion == "VOLVER":
                    print("\nIntentas volver sobre tus pasos, pero te desorientas por completo en la oscuridad. Fin del juego.")
                else:
                    print("Opción no válida. Intenta de nuevo.")
            else:
                print("Opción no válida. Intenta de nuevo.")

        elif segunda_decision_linterna == "BUSCAR":
            print("\nTe adentras entre los árboles para buscar lo que hizo el ruido. La linterna ilumina un pequeño nido de aves, pero de repente, el suelo bajo tus pies se desploma.")
            tercera_decision_buscar = normalizar_texto(input("¿Quieres INTENTAR AGARRARTE a una rama, CAER y ver a dónde llegas o GRITAR por ayuda? "))

            if tercera_decision_buscar == "INTENTAR AGARRARTE":
                print("\nIntentas agarrarte a una rama, pero se rompe. Caes a un agujero oscuro. Fin del juego.")
            elif tercera_decision_buscar == "CAER":
                print("\nCaes por un túnel subterráneo. Aterrizas suavemente en una caverna llena de cristales brillantes. Parece un lugar mágico y peligroso.")
                cuarta_decision_caverna = normalizar_texto(input("¿Quieres EXPLORAR la caverna, BUSCAR una salida o TOCAR los cristales? "))
                if cuarta_decision_caverna == "EXPLORAR":
                    print("\nExploras la caverna y descubres una antigua civilización subterránea. Te acogen y aprendes sus secretos. ¡Has descubierto un nuevo mundo! Fin del juego.")
                elif cuarta_decision_caverna == "BUSCAR":
                    print("\nBuscas una salida y después de un tiempo encuentras un pasadizo oculto que te lleva de regreso a la superficie. ¡Has escapado! Fin del juego.")
                elif cuarta_decision_caverna == "TOCAR":
                    print("\nTocas los cristales. Emiten una luz cegadora que te desorienta. Cuando recuperas la visión, la caverna está vacía y estás solo. Fin del juego.")
                else:
                    print("Opción no válida. Intenta de nuevo.")
            elif tercera_decision_buscar == "GRITAR":
                print("\nGritas por ayuda, pero nadie te escucha. Caes al agujero oscuro. Fin del juego.")
            else:
                print("Opción no válida. Intenta de nuevo.")

        else:
            print("Opción no válida. Intenta de nuevo.")

    else:
        print("Opción no válida. Intenta de nuevo.")

    print("\nGracias por jugar a la aventura. ¡Hasta la próxima!")

# Iniciar el juego
jugar_aventura()