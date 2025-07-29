print("\n\n Pajaman en la cueva🤑")

print("\n Eres Pajaman \n\n estas caminando viendo de todo menos el camino y . . . ")


decicion = int(input("\n Caes por un vacio que parece interminable . . . \n . . . caiste . . . \n recobras la concencia y tienes que lograr salir de alli \n tiene que escojer entre \n\n 1. escalar 2. buscar entre la oscuridad 3. esperar . . ."))

if decicion <= 1:
    print(" escoges escalar")
    print("intentas escalar entre las pequeñas rocas . . .")
    print("te caes de las pequeñas rocas, y caes en un lugar diferente, en pocas palabras estas muerto ahora ✨")

elif decicion <= 2:
        print("escoges buscar entre la oscuridad")
        print("ves pocas cosas y mientras exploras ves una luz")
        print("vas hacia la luz y cuando llegas te desorientas, pero hay dos caminos")
        decicionesv2 = input("cual camino escoges \n derecha o izquierda?")
        print(f"escogiste la opcion {decicionesv2}")
        if decicionesv2 <= "derecha":
            print("\n el camino derecho tiene poca luz, en el camino te da por correr, y te caes en un pozo con MUCHA agua y te mueres")
        elif decicionesv2 <= "izquierda":
            print("el camino izquierdo es pequeño, pero logras salir de alli \n felicidades eres libre ahora ✨🎉")
        
        else :
            print("intentas hacerte el listo? TE MUERES POR TRAMPOSO")

elif decicion <= 3:
    print("eliges esperar \n te cansas de esperar y empiezas a hablar solo")
    decicionv3 = input("te preguntas que debes hacer \n rendirte o buscar ayuda?")
    print(f"escogiste la opcion {decicionv3}")
    if decicionv3 == "rendirte":
            print("\n te rindes y te suicidas, felicidades eres un agente suicida 😁")
    elif decicionv3 == "buscar ayuda":
            print("no encuentras nada pero por el aburrimiento decides por fin mirar arriba y ves una liana por la que subes")
            print("\n Nuevo logro desbloqueado APRENDESTE A PENSAR 😑")

    else :
            print("intentas hacerte el listo? TE MUERES POR TRAMPOSO")
    

    
else :
            print("intentas hacerte el listo? TE MUERES POR TRAMPOSO")


















