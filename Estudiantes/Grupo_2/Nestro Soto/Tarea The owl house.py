print ("\n\n\n\n")
print ("The Owl House")
print ("Te has perdido en el bosque y no recuerdas como llegaste hasta ahi.")
print ("Caminas un poco y te encuentras con una casa abandonada, parece que nadie ha vivido ahi en años.")
print("Esta oscureciendo y no tienes como volver a casa,¿Quieres entrar?")
respuesta= input ("Si o No:").lower ()
if respuesta == "si": 
    print("Has decidido entrar en la casa.")
    print("Al entrar, te das cuenta de que nadie ha vivido aqui en años.")
    print("El lugar esta lleno de telarañas y polvo, pero igual decides entrar para pasar la noche.")
    print ("Mientras exploras, te das cuenta de que hay camaras en varios lugares de la casa.")
    print("De repente, escuchas a alguien hablando y la camara voltea hacia ti.")
    print("Escuchas una voz que dice: Bueno, ahora eres parte del show.")
    print("Tu respondes: ¿Que show?")
    print("La voz responde: Basicamente tienes que sobrevivir que mates a un participante en especifico.")
    print ("Tu preguntas: ¿Y si no lo hago?")
    print ("La voz responde: Entonces el te matara a ti.")
    print ("Piensas en si quieres seguir o salir corriendo de la casa.")
elif respuesta =="no": 
    print ("Has decidido no entrar en la casa.")
    print("Sigues caminando por el bosque, pero debido al cansancio y la oscuridad, caes a un precipicio.")
    print("Mueres al instante.")
else:
    print ("Respuesta no valida, por favor escribe 'si ' o 'no'.")
    
respuesta2 = input("Quieres seguir o salir corriendo?:").lower ()
if respuesta2 == "seguir"or respuesta2 == "quiero seguir":
     print ("Decides seguir adelante.")
     print ("Le preguntas a la voz: ¿A quien tengo que matar?")
     print ("La voz responde: A un hombre con una motocierra y una mascara de cerdo, pronto lo encontraras.")
     print ("Decides seguir y explorar la casa en busca de algo con lo que puedas defenderte.")
     print ("Vas caminando, y con el tiempo te das cuenta de que la casa es mas grande de lo que pensabas, y que parece un laberinto.")
     print ("Te preguntas: ¿Quien es el dueño de esta casa? ¿Como llegue al bosque? Al decir eso te llega a la mente un recuerdo borroso de como llegaste ahi.")
     print ("Recuerdas que estabas en un bar, tomaste de mas y antes de irte a casa, un desconocido te ofrecio llevarte a casa.")
     print("Recuerdas que te subiste a su camioneta, y debido al alcohol no recuerdas nada mas.")
     print ("Sigues por la casa y encuentras un estante con unos trozos de vidrio rotos, como si alguien los hubiera puesto ahi a proposito.")
     print ("Al mismo tiempo que ves los vidrios, escuchas gente acercandose y piensas en agarrarlos para defenderte.")
elif respuesta2 == "salir corriendo" or respuesta2 == "Correr":
     print ("Decides correr y salir de la casa.")
     print ("Mientras corres, escuchas la voz que dice: Respuesta incorrecta, moriras.")
     print ("Al llegar a la puerta, te encuentras con un hombre con una motosierra y una mascara de cerdo.")
     print ("El hombre te degolla y te mata al instante.")
     print ("Has muerto.") 
     print ("Fin del juego")
else:
     print ("Respuesta no valida, por favor escribe 'seguir'o 'salir corriendo'.").lower()
respuesta3 = input("Quieres agarrar los vidrios o no? (Si o No):").lower()
if respuesta3 == "si" or respuesta3 == "sí":
    print ("Decides agarrar los vidrio y te escondes")
    print("Ya escondido, escuchas que las personas que se acercan son participantes como tu, y que estan buscando al hombre con la motosierra.")
    print ("Estas personas te ven y se muestran agresivas, asi que decides defenderte con los pedazos de vidrio.")
    print("Logras defenderte de ellos, asi que sigues tu camino por la casa.")
    print ("Sigues caminando y encuentras un estante con unos objetos, entre ellos un botiquin de primeros auxilios, una linterna y un cuchillo.")
elif respuesta3  == "no" or respuesta3 == "no agarrar los vidrios":
     print ("Decides no agarrar los vidrios y las personas que se acercan son participantes como tu, te atacan y mueres.")
     print ("Has muerto.")
else: 
     print ( "Respuesta no valida, por favor escribe 'si'o 'no'.")
respuesta4 = input("Quieres agarrar el botiquin, la linterna o el cuchillo? (Botiquin, Literna o Cuchillo):").lower()
if respuesta4 == "botiquin":
     print ("Decides agarrar el botiquin y te lo guardas.)")
elif respuesta4 == "linterna":
     print ("Decides agarrar la linterna y te la guardas.")
elif respuesta4 == "cuchillo":
     print ("Decides agarrar el cuchillo y te lo guardas.")
else:
     print ("Respuesta no valida, por favor escribe 'botiquin', 'linterna' o 'cuchillo'.")
print ("Guardas el objeto que elegiste y sigues explorando la casa.")
print ("Mientras exploras, escuchas ruidos extraños y te das cuenta de que el hombre con la motosierra esta haciendo ruidos de cerdo entre los pasillos.")
print ("Decides seguir explorando, pero con cuidado de no encontrarte con el hombre.")
print ("Sigues avanzando y encuentras varias habitaciones, una cocina, un comedor y una sala de estar.")
respuesta5 = input ("Quieres entrar a la cocina, al comedor o a la sala de estar? (Cocina, Comedor o Sala de estar):").lower()
if respuesta5 == "cocina":
    print ("Decides entrar a la cocina.")
    print ("Revisas en los cajones y no encuentras nada util, pero en la nevera encuentras algo de comida.")
    print ("Te guardas la comida y decides seguir explorando la casa.")
elif respuesta5 == "comedor":
     print ("Te asomas para ver el comedor, y notas huellas de sangre en el suelo.")
     print("Ves que el hombre con la motosierra esta en el comedor y decides no entrar.")
elif respuesta5  == "sala de estar":
     print("Decides entrar a la sala de estar.")
     print("Revisas los muebles y encuentras una llave antigua escondida debajo de un cojin.")
     print("Te guardas la llave y decides seguir explorando la casa.")
else:
     print("Respuesta no valida, por favor escribe 'cocina', 'comedor' o 'sala de estar'.")
print("Sigues explorando y decides intentar atacar al hombre con la motosierra.")
print ("Te preparas para el enfrentamiento y te acercas sigilosamente hacia el comedor.")
print ("Logras sorprender al hombre con la motosierra y comienzas a pelear con el.")
print ("El hombre es fuerte y agresivo, pero logras defenderte con el trozo de vidrio que agarraste antes.")
print ("Le apuñalas el brazo y logras desarmarlo.")
print ("El hombre cae al suelo y te das cuenta de que tiene una herida grave.")
respuesta6 = input("Quieres matarlo con la motosierra, darle el golpe de gracia con un golpe o dejarlo vivir y hablar con el para averiguar mas y aliarse? (Matarlo con la motosierra, Dar golpe, Dejarlo vivir y hablar):").lower ()
if respuesta6 == ("matarlo con la motosierra") or respuesta6 == ("motosierrra"):
    print ("Decides matarlo con la motosierra.") 
    print ("Lo degollas y Ganas el enfrentamiento.")
    print ("La voz te felicita y te dice que has ganado el juego.")
    print ("Te dice que puedes salir y irte a casa.")
elif respuesta6 == ("dar golpe") or respuesta6 == ("dar golpe de gracia"):
    print ("Decides darle el golpe de gracia con un golpe.")
    print ("El hombre cae inconsciente y lo dejas tirado en el suelo.")
    print ("La voz te dice: Aun no has ganado, el juego, matalo o no saldras de aqui.")
    print ("Decides matarlo")
    print ("Le dices a la voz que lo has matado y quieres irte de aqui.")
    print ("La voz te dice que has ganado el juego y puedes salir.")
elif respuesta6 == ("dejarlo vivir y hablar") or respuesta6 == ("hablar"):
    print ("Decides dejarlo vivir y hablar con el.") 
    print ("El hombre se levanta y no puedes entablar una conversacion con el.")
    print ("Te golpea y te deja gravemente herido.")
    print ("El hombre te mata y se pone feliz por haberte matado. diciendo que esta feliz de que hayas muerto.")
    print ("Has muerto.")
else:
     print ("Respuesta no valida, por favor escribe 'matarlo con la motosierra', 'dar golpe' o 'dejarlo vivir y hablar'.")
print ("Decides enfrentarte a la voz misteriosa, pero antes de hacerlo, pierdes el conocimiento")
print ("Felicidades por completar el juego.")
print ("Gracias por jugar.")
print ("FIN")