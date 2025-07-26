print("Eres un Elio cualquiera intentando programar un juego basado en texto")
print("Estuviste toda la noche escribiendo codigos, pero cuando el profesor lo revisa ¡Descubres que esta todo mal!")
print("Tienes 2 opciones, RENDIRTE o INTENTAR de nuevo")
decision1 = input ("¿Que haras? ¿RENDIRTE o INTENTAR de nuevo?> ").lower()
if decision1 == "rendirte":
    print("\nDecidiste rendirte y dejarlo todo, ahora que haras? Solo tienes dos opciones.")
    decision2 = input ("IRTE del pais o MORIR de hambre> ").lower()
    if decision2 == "irte":
        print("\nTe vas hacia estados unidos y te deportan por presuntamente pertenecer al tren de Aragua.")
        print("GAME OVER")
    elif decision2 == "morir":
        print("\nDeprimido, decides quedarte acostado en tu cama, sin esperar nada.")
        print("Milagrosamente, consigues un trabajo en Fiorela.")
        print("Trabajas ahi toda tu vida, y mueres de viejo, es un final un poco agridulce")
        print("WIN")
    else: 
        print("Respuesta no reconocida, intenta de nuevo")
elif decision1 == "intentar":
    print("\nDecidiste intentarlo de nuevo, ahora tienes que esforzarte")
    print("Ahora debes escoger entre SEGUIR el curso o BUSCAR trabajo en el centro vendiendo pantaletas")
    decision2 = input("¿Que eliges? ¿SEGUIR el curso o BUSCAR trabajo en el centro?> ").lower()
    if decision2 == "seguir":
        print("\nContinuas con el curso, es muy complicado, pero lo logras")
        print("Encuentras un trabajo como web designer")
        decision3 = input("Decides TOMAR el trabajo, RECHAZAR el trabajo o SEGUIR buscando trabajo> ").lower()
        if decision3 == "tomar":
            print("\nTe da una arrechera con un codigo que te salio mal, y mueres por una arrechera")
            print("Buen intento, pero no lograste ganar ¡Intentalo de nuevo!")
            print("GAME OVER")
        elif decision3 == "rechazar":
            print("\nRechazas el trabajo, y terminas siendo un vagabundo en la plaza rafael urdaneta y mueres en una guarimba por un impacto de bala.")
            print("GAME OVER")
        else:
            print("Decidiste seguir buscando trabajo, encuentras trabajo en traki, te explotan laboralmente y mueres por mucho trabajo")
            print("GAME OVER")    
else:    
    print("Respuesta no reconocida, intenta de nuevo")