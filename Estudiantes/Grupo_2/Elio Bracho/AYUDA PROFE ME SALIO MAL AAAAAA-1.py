print("Eres un Elio cualquiera intentando programar un juego basado en texto")
print("Estuviste toda la noche escribiendo codigos, pero cuando el profesor lo revisa ¡Descubres que esta todo mal!")
print("Tienes 2 opciones, RENDIRTE o INTENTAR de nuevo")
decision1 = input ("¿Que haras? ¿RENDIRTE o INTENTAR?> ").lower()
if decision1 == "rendirte":
    print("\nDecidiste rendirte y dejarlo todo, ahora que haras? Solo tienes dos opciones.")
    decision2 = input ("IRTE del pais o MORIR> ").lower()
    if decision2 == "irte":
        print("\nTe vas hacia estados unidos y te deportan por presuntamente pertenecer al tren de Aragua.")
        print("GAME OVER")
    elif decision2 == "morir":
        print("\nDeprimido, decides quedarte acostado en tu cama, sin esperar nada.")
        print("Milagrosamente, consigues un trabajo en Fiorela.")
        print("Trabajas ahi toda tu vida, y mueres de viejo, es un final un poco agridulce")
        print("WIN")
    else: 
        print("\nRespuesta no reconocida, intenta de nuevo")
elif decision1 == "intentar":
    print("\nDecidiste intentarlo de nuevo, ahora tienes que esforzarte")
    print("Ahora debes escoger entre SEGUIR el curso o BUSCAR trabajo en el centro vendiendo pantaletas")
    decision2 = input("¿Que eliges? ¿SEGUIR o BUSCAR?> ").lower()
    if decision2 == "seguir":
        print("\nContinuas con el curso, es muy complicado, pero lo logras")
        print("Encuentras un trabajo como web designer")
        decision3 = input("Decides TOMAR, RECHAZAR o SEGUIR buscando trabajo> ").lower()
        if decision3 == "tomar":
            print("\nTe da una arrechera con un codigo que te salio mal, y mueres por una arrechera")
            print("Buen intento, pero no lograste ganar ¡Intentalo de nuevo!")
            print("GAME OVER")
        elif decision3 == "rechazar":
            print("\nRechazas el trabajo, y terminas siendo un vagabundo en la plaza rafael urdaneta y mueres en una guarimba por un impacto de bala.")
            print("GAME OVER")
        else:
            print("\nDecidiste seguir buscando trabajo, encuentras trabajo en traki, te explotan laboralmente y mueres por mucho trabajo")
            print("GAME OVER")    
    elif decision2 == "buscar":
        print("\nEmpiezas a trabajar en el centro, eres el mejor vendedor de pantaletas en la historia del centro, te conocen como el pantaletuo")
        print("te ofrecen la oportunidad de abrir un negocio de pantaletas")
        print("Dejarias de ser trabajador, para ser el dueño de tu propio negocio")
        decision3 = input ("Decides ACEPTAR o RECHAZAR> ").lower()
        if decision3 == "aceptar":
            print("\nEmpiezas con tu negocio de pantaletas.")
            print("Parece que te ira muy bien, tiene mucho futuro el negocio.")
            print("Logras vivir una vida comoda")
            print("FELICIDADES, TIENES UN FUTURO")
        elif decision3 == "rechazar":
            print("Vives toda una vida vendiendo pantaletas en un puestico en el centro")
            print("No vives mal, pero tampoco tienes una vida lujosa")
            print("Sigues trabajando ahi hasta morir por dengue")
            print("no se si ganaste o no, es tu decision")
        else:
            print("Respuesta no reconocida, intenta de nuevo")
    else:
        print("Respuesta no reconocida, intenta de nuevo")
else:    
    print("Respuesta no reconocida, intenta de nuevo")