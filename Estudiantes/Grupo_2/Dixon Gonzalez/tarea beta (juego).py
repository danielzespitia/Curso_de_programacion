opcion = input("Estás caminando por un bosque oscuro y encuentras dos objetos... Un fósforo y una linterna. ¿Con cuál te quedas? (escribe 'fosforo' o 'linterna'):")

if opcion.lower() == "fosforo":
    print("Coges el fósforo y lo enciendes. Por un instante, el bosque se ilumina... ¡y ves un gran oso grizzly! El fósforo se apaga. ¿Quieres CORRER o ESCONDERTE detrás de un árbol?")
    decision = input("Deseas 'correr' o 'esconderte': ")
    if decision.lower() == "correr":
        print("Corres lo más rápido que puedes y logras escapar del oso. ¡Estás a salvo!")
    elif decision.lower() == "esconderte":
        print("Te escondes detrás de un árbol. El oso pasa cerca, pero no te ve. ¡Te salvaste!")
    else:
        print("No elegiste una opción válida. El oso te encuentra.")
elif opcion.lower() == "linterna":
    print("Enciendes la linterna y puedes ver el camino claramente. Sigues caminando con seguridad por el bosque.")
else:
    print("No elegiste una opción válida. Te pierdes en el bosque y no encuentras el camino de regreso.")
