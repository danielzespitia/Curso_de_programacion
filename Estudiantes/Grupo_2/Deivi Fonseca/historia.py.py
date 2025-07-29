print("decide y gana")
   #juego de aventura y toma de decisiones para salir del bosque a salvo.
   #juego comienza conun personaje que hizo una excursion, por algunos motivos de separo del resto de compañeros y se perdio en el bosque
   #tiene que salir del boste antes de morir por los animales salvajes y los peligros del bosque eso es su mision")
    
print("--- Decide y Sobrevive ---")
print("Te has separado de tu grupo de compañeros en un bosque muy grande y peligroso.")
print("Tu misión es salir del bosque antes de morir por los animales salvajes y los peligros.")

    
print("Tienes algunas ideas para salir del bosque:")
opcion1 = input("¿Quieres subir a un árbol para tener mejor visión? (si/no): ").lower()

if opcion1 == "si":
    print("Lo haces, y logras tener una mejor visión y una mejor noción de dónde puedes estar.")
    print("Después de eso, decides caminar hacia una dirección que escogiste.")
    print("Caminas durante algunos minutos y logras llegar a un arroyo y tienes que tomar una decisión.")

    
    print("Has llegado a un arroyo.")
    opcion2 = input("¿Seguir la corriente del río (1), pasar al otro lado del río (2) o acampar en una zona alta que viste en el camino (3)?: ")

    if opcion2 == "1":
        print("Decides seguir la corriente del río. No llegas a nada, oscurece y no puedes hacer nada. Un animal salvaje te ataca y mueres.")
        print("Perdiste")
            
        
    elif opcion2 == "2":
        print("Intentas pasar al otro lado del río. La corriente es más fuerte de lo que pensabas y debido a las rocas, troncos, etc. mueres por los golpes.")
        print("Perdiste")
            
            
    elif opcion2 == "3":
        print("Buscas la zona alta que viste. Después de una breve escalada, encuentras un lugar seguro para acampar por la noche.")
        print("Con las herramientas que tienes en tu bolso, logras hacer un pequeño refugio.")
        print("Terminas de hacer tu refugio y debes tomar otra decisión.")

        print("Estás a salvo en tu refugio, pero el hambre aprieta.")
        opcion3 = input("¿Salir a buscar comida o quedarte y aguantar hasta el próximo día? (salir/quedarte): ").lower()

        if opcion3 == "salir":
            print("Sales a buscar comida. Por el miedo y la oscuridad, olvidas el camino de regreso. Caminas sin rumbo y te encuentras un animal que te ataca y mueres.")
            print("Perdiste")
                

        elif opcion3 == "quedarte":
            print("Esperas al día siguiente y por la mañana, buscas comida tranquilamente.")
            print("Después de comer, sales a explorar la zona.")
            print("Después de caminar por un tiempo, te encuentras a un oso y tienes que decidir qué hacer.")

            print("\n¡Un oso! ¿Qué haces?")
            opcion4 = input("¿Esconderte (1), correr (2) o subir a un árbol (3)?: ")

            if opcion4 == "1":
                print("Rápidamente te colocas detrás de árboles y arbustos. Logras confundir al oso y puedes huir.")
                print("Después de ese encuentro, sabes por dónde no debes ir. Terminas de explorar la zona y regresas al refugio.")
                print("Cuando llegas al refugio, te pones a pensar en qué sería lo mejor: esperar un rescate o intentar salir del bosque por tu cuenta.")

                print("Liego te llega una gran duda ¿esperas ayuda o te arriesgas a salir solo?")
                opcion5 = input("¿Esperar un rescate o intentar salir solo del bosque?: ")

                if opcion5 == "esperar":
                    print("Mientras esperas un rescate, puedes aprender más sobre la zona, conseguir más recursos y mejorar tu refugio.")
                    print("Además, puedes recolectar materiales para hacer señales y que puedan encontrarte.")
                    print("Efectivamente, al día siguiente se escucha un sonido... ¡es un helicóptero de rescate!")

                    print("El helicóptero está cerca. Es tu oportunidad")
                    opcion6 = input("¿Hacer una señal de humo o gritar, silbar, hacer ruido?: ")

                    if opcion6 == "1":
                        print("Con los materiales que recogiste, logras hacer una gran señal de humo. El helicóptero te ve y logras sobrevivir.")
                        print("FELICIDADES GANASTE EL JUEGO")
                            

                    elif opcion6 == "2":
                        print("Al ser un bosque grande y muy denso, no logras hacer ruido suficiente para que los rescatistas te escuchen.")
                        print("Pierdes esa gran oportunidad de salir de ese lugar y mentalmente te derrumbas.")
                        print("Al cabo de unos días, no soportarás más y morirás por algún peligro del bosque.")
                        print("Perdiste")
                            
                        
                    else:
                        print("nOpción no válida. Debes escoger entre '1' o '2'.")
                        print("Por tu indecisión, el helicóptero se aleja y mueres solo en el bosque.")
                        print("Perdiste")
                            

                elif opcion5 == "2":
                    print("Decides reunir todas las raciones y salir tú solo del bosque. Al plazo de unos días estarás bien por las raciones y la experiencia.")
                    print("Pero al ser un bosque tan grande, no logras encontrar el camino a casa.")
                    print("Se acabarán las raciones, comenzarán las lluvias y no tendrás refugio. Más los animales salvajes del bosque. Pasarán días y morirás.")
                    print("Perdiste")
                        
                    
                else:
                    print("Opción no válida. Debes escoger entre '1' o '2'.")
                    print("Tu indecisión te lleva a un final incierto, y terminas muriendo a los peligros del bosque.")
                    print("Perdiste")
                        

            elif opcion4 == "2":
                print("Corres, pero no es suficiente. El oso te alcanza y te mata.")
                print("Perdiste")
                    
                
            elif opcion4 == "3":
                print("El oso sabe trepar árboles. Del miedo te lanzas, te rompes una pierna, no puedes escapar y el oso te mata.")
                print("Perdiste")
                    
                
            else:
                print("\nOpción no válida. Debes escoger entre '1', '2' o '3'.")
                print("Por tu indecisión, el oso te ataca y mueres.")
                print("Perdiste")
                    

        else:
            print("Opción no válida. Debes escoger obligatoriamente 'salir' o 'quedarte'.")
            print("La indecisión te consume y mueres de hambre o por un peligro nocturno.")
            print("Perdiste")
                

    else:
        print("Opción no válida. Debes escoger entre '1', '2' o '3'.")
        print("Tu falta de decisión te deja expuesto y mueres por no avanzar.")
        print("Perdiste")
            

elif opcion1 == "no":
    print("Decides no subir al árbol y buscas otra alternativa. Pierdes mucho tiempo, se hace de noche, y mientras caminas en la oscuridad caes a un barranco y mueres.")
    print("Perdiste")
        

else:
    print("Opción no válida. Por favor, responde 'si' o 'no'.")
    print("La indecisión te paraliza y los peligros del bosque te encuentran.")
    print("Perdiste")


    