def start_game():
    """
    Función principal para ejecutar el juego de aventura.
    Contiene toda la lógica y la historia del juego.
    """
    # --- NIVEL 1 ---

    print("\n" + "="*50)
    print("⚔️  LA CUEVA DEL DRAGÓN 🐉")
    print("="*50 + "\n")
    print("🧑‍🎤 Eres Sir Valerius, un valiente caballero. Te encuentras en la entrada de una cueva oscura y ominosa. 🕳️")
    print("💨 El hedor a azufre emana de la oscuridad. Tu misión es derrotar al dragón que aterroriza estas tierras. 🐲")
    print("🔦 Llevas contigo una ANTORCHA para iluminar tu camino y tu fiel ESPADA para el combate. 🗡️\n")
    

    decision1 = input("¿Qué preparas primero? ¿La ANTORCHA 🔦 o la ESPADA 🗡️? > ").lower()

    if decision1 == "antorcha":
        # --- NIVEL 2 (Ruta de la Antorcha) ---

        print("\n🔥 Enciendes la antorcha. Las llamas danzan y revelan dos caminos que se adentran en la cueva. 🔥\n")
        print("⬅️ Uno va hacia la IZQUIERDA, es estrecho y húmedo.\n➡️ El otro va a la DERECHA, es ancho y parece más transitado.\n")
        decision2 = input("¿Qué camino tomas? ¿IZQUIERDA ⬅️ o DERECHA ➡️? > ").lower()

        if decision2 == "izquierda":
            # --- NIVEL 3 (Ruta de la Izquierda) ---

            print("\n🚶‍♂️ El camino de la izquierda es angosto. El sonido de goteo de agua resuena en las paredes. 💧\n")
            print("🌊 Llegas a una pequeña cámara con un arroyo subterráneo de agua cristalina.\n")
            print("😓 Te sientes sediento, pero no sabes si el agua es segura.\n")
            decision3 = input("¿Qué haces? ¿BEBER del arroyo 🥤, SEGUIR el arroyo 🚶‍♂️ o CRUZAR el arroyo 🏃‍♂️? > ").lower()

            if decision3 == "beber":
                # --- NIVEL 4 ---

                print("\n✨ El agua es mágica y refrescante. Sientes cómo tus fuerzas se renuevan. ¡Te sientes más fuerte! 💪✨\n")
                print("👀 Con tu nueva vitalidad, notas una grieta oculta detrás de una pequeña cascada. 🌫️\n")
                decision4 = input("¿Decides ENTRAR por la grieta 🕳️ o IGNORARLA 🚶 y seguir adelante? > ").lower()
                
                if decision4 == "entrar":
                    # --- NIVEL 5 ---

                    print("\n🕳️ La grieta te lleva a un atajo secreto. ¡Has llegado directamente a la guarida del dragón! 🐉\n")
                    print("😴 La bestia duerme sobre una montaña de oro. Es tu oportunidad. 🪙\n")
                    decision5 = input("¿Cómo atacas? ¿APUNTAS a la cabeza 🧠, al ALA 🪽 o a la cola 🦎? > ").lower()
                    
                    if decision5 == "cabeza":
                        # --- NIVEL 6 (Final) ---
                        print("\n🗡️ Con un grito de guerra, clavas tu espada en el cráneo del dragón. La bestia se desploma sin vida. 🐲\n")
                        print("🎉🏆 ¡HAS GANADO! Has salvado el reino. Tu nombre será recordado como una leyenda. ��🎉\n")
                    elif decision5 == "ala":
                        print("\nIntentas cortar su ala 🪽, pero la piel es demasiado dura. El dragón se despierta furioso y te incinera con su aliento de fuego. 🔥🐉\n")
                        print("☠️💀 FIN DEL JUEGO. Tu aventura termina aquí. 💀☠️\n")
                    elif decision5 == "cola":
                        print("\nTu ataque a la cola 🦎 solo enfurece al dragón. Con un rápido movimiento, te golpea y te lanza contra la pared. 🧱\n")
                        print("☠️💀 FIN DEL JUEGO. La oscuridad te consume. 💀☠️\n")
                    else:
                        print("😵 Respuesta no válida. El dragón se despierta por tu indecisión y te devora. FIN DEL JUEGO. 🐉💀\n")
                
                elif decision4 == "ignorarla":
                    print("\nDecides que es muy arriesgado. Continúas tu camino, pero te pierdes en los túneles interminables. 🕳️🚶‍♂️\n")
                    print("☠️💀 FIN DEL JUEGO. Vagas por la cueva hasta que tus fuerzas te abandonan. 💀☠️\n")
                else:
                    print("😱 Respuesta no válida. Mientras dudas, una criatura de las sombras te ataca. FIN DEL JUEGO. 👾💀\n")

            elif decision3 == "seguir":
                print("\n🚶‍♂️ Sigues el arroyo y te lleva a un lago subterráneo. En el centro, ves un tesoro, pero está custodiado por serpientes acuáticas. 🐍💎\n")
                print("☠️💀 FIN DEL JUEGO. Las serpientes te rodean y te arrastran a las profundidades. 💀☠️\n")
            elif decision3 == "cruzar":
                print("\n🏃‍♂️ Intentas cruzar, pero resbalas en una roca. Tu antorcha cae al agua y se apaga. Estás en completa oscuridad. 🌑\n")
                print("☠️💀 FIN DEL JUEGO. No puedes encontrar la salida y te conviertes en parte de la cueva. 💀☠️\n")
            else:
                print("😵 Respuesta no válida. Mientras piensas, el suelo cede bajo tus pies. FIN DEL JUEGO. 🕳️💀\n")

        elif decision2 == "derecha":
            # --- NIVEL 3 (Ruta de la Derecha) ---

            print("\n➡️ El camino de la derecha huele a azufre. A lo lejos, ves un brillo rojizo. 🔥\n")
            print("🥚 Te acercas y descubres que el brillo proviene de los huevos del dragón, que irradian calor. 🥚\n")
            decision3 = input("¿Qué haces? ¿DESTRUYES los huevos 🥚 para provocar al dragón 🐉 o los USAS como cebo 🎣? > ").lower()
            
            if decision3 == "destruyes":
                print("\n🗡️ Con tu espada, rompes los huevos. Un rugido ensordecedor sacude la cueva. ¡El dragón viene hacia ti! 🐉\n")
                print("☠️💀 FIN DEL JUEGO. La madre dragón aparece y no muestra piedad. 💀☠️\n")
            elif decision3 == "usas":
                print("\n🤲 Tomas un huevo con cuidado. Planeas usarlo para atraer al dragón a una trampa. 🪤\n")
                print("🐣 Mientras buscas el lugar perfecto, el huevo eclosiona en tus manos. Un bebé dragón te mira. 🐲\n")
                print("👩‍👦 La madre dragón llega, pero al ver a su cría a salvo contigo, se calma. Te considera un aliado. 🤝\n")
                print("🎉🏆 ¡HAS GANADO! No mataste al dragón, pero forjaste una paz legendaria. 🏆🎉\n")
            else:
                print("😵 Respuesta no válida. El calor de los huevos te hace tropezar y caes en una fosa. FIN DEL JUEGO. 🕳️💀\n")
        else:
            print("😵 Respuesta no válida. Te pierdes en la entrada. FIN DEL JUEGO. 🕳️💀\n")

    elif decision1 == "espada":
        # --- NIVEL 2 (Ruta de la Espada) ---

        print("\n🗡️ Desenvainas tu espada. El acero brilla débilmente. Avanzas a ciegas en la oscuridad. 🌑\n")
        print("💨 Sientes una corriente de aire y escuchas un gruñido lejano. 🐲\n")
        decision2 = input("¿Decides AVANZAR hacia el sonido 🏃‍♂️ o ESPERAR en silencio 🤫? > ").lower()
        
        if decision2 == "avanzar":

            print("\n🏃‍♂️ Avanzas con valentía. El gruñido se hace más fuerte. De repente, te encuentras cara a cara con el dragón. 🐉\n")
            print("👀 La bestia te mira fijamente, sorprendida por tu audacia. 😮\n")
            decision3 = input("¿Qué haces? ¿ATACAS de frente 🗡️, intentas DIALOGAR 🗣️ o te RETIRAS lentamente 🚶‍♂️? > ").lower()
            
            if decision3 == "atacas":
                print("\n🗡️ Cargas contra el dragón, pero en la oscuridad no ves un pozo de lava justo frente a ti. 🌋\n")
                print("☠️💀 FIN DEL JUEGO. Tu carga valiente te lleva a un final ardiente. 💀☠️\n")
            elif decision3 == "dialogar":
                print("\n🗣️ ¡Sorprendentemente, el dragón te responde en una lengua antigua! Te dice que solo protege un artefacto sagrado. 🗿\n")
                print("🤝 Llegan a un acuerdo: tú lo dejas en paz y él deja de aterrorizar la superficie. 🌍\n")
                print("🎉🏆 ¡HAS GANADO! La diplomacia fue tu mejor arma. 🏆🎉\n")
            elif decision3 == "retiras":
                print("\n🚶‍♂️ Intentas retroceder, pero el dragón lo interpreta como un signo de debilidad y te ataca. 🐉\n")
                print("☠️💀 FIN DEL JUEGO. No se puede huir de un dragón en su propia guarida. 💀☠️\n")
            else:
                print("😵 Respuesta no válida. Tu indecisión es tu fin. FIN DEL JUEGO. 🐉💀\n")

        elif decision2 == "esperar":
            print("\n🤫 Esperas en la oscuridad, agudizando tus sentidos. Oyes unos pasos pesados que se alejan. 🐾\n")
            print("🐉 Parece que el dragón ha salido de caza. Es tu oportunidad para explorar su guarida. 🏰\n")
            print("💎 Encuentras un tesoro inimaginable y un mapa secreto que revela las debilidades de todos los dragones. 🗺️\n")
            print("🎉🏆 ¡HAS GANADO! No mataste al dragón hoy, pero obtuviste el conocimiento para proteger el reino para siempre. 🏆🎉\n")
        else:
            print("😵 Respuesta no válida. Te quedas quieto demasiado tiempo y los murciélagos de la cueva te confunden con una estatua. FIN DEL JUEGO. 🦇💀\n")
    else:
        print("😵 Respuesta no válida. Tropiezas en la entrada de la cueva y decides que ser caballero no es para ti. FIN DEL JUEGO. 🕳️💀\n")

# Iniciar el programa
if __name__ == "__main__":
    start_game()