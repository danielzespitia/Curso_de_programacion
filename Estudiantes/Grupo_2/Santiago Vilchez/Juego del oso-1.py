opcion1 = input("Te encuentras en un bosque oscuro y tienes un fósforo y una linterna. ¿Cuál eliges? (fosforo o linterna): ")

if opcion1 == "fosforo":
    print("Agarras el fósforo, se queda encendido un rato y luego se apaga.")
    print("¿Qué haces?")
    opcion2 = input("¿Correr o esconderte? ")

    if opcion2 == "correr":
        print("Corres y llegas a un acantilado de un río.")
        opcion3 = input("¿Saltar, escalar o buscar? ")

        if opcion3 == "saltar":
            print("Te salvas, pero te doblas el tobillo.")
        elif opcion3 == "escalar":
            print("El oso te atrapa y te come.")
        elif opcion3 == "buscar":
            print("Encuentras una cabaña segura y te salvas.")
        else:
            print("No hiciste nada por salvarte. El oso acabó contigo.")

    elif opcion2 == "esconderte":
        print("Te escondes y encuentras una casa.")
        opcion3_2 = input("¿Entrar ,buscar otro lugar o ignorar? ")

        if opcion3_2 == "entrar":
            print("Consigues un palo y te defiendes.")
        elif opcion3_2 == "ignorar":
            print("Te caíste y el oso te atrapó.")
        elif opcion3_2 == "buscar otro lugar":
            print("sigues buscando y encuentras una pequeña aldea donde te refugias y estas a salvo")
        else:
            print("No hiciste nada por tu vida. El oso te comió.")

elif opcion1 == "linterna":
    print("Enciendes la linterna, pero escuchas algo.")
    print("¿Qué haces?")
    opcion4 = input("¿Investigar, huir o buscar arma? ")

    if opcion4 == "investigar":
        print("Vas caminando y te consigues al oso de frente y te hace pedazos.")
    elif opcion4 == "huir":
        print("Comienzas a correr y llegas a una ciudad cercana después de mucho tiempo y te salvas.")
    elif opcion4 == "buscar arma":
        print("encuentras un arma y te enfrentas al oso")
    else:
        print("No hiciste nada y te atrapó el oso. ¡Perdiste!")
else:
    print("Esa no es una opción válida. El oso te encontró antes de que pudieras decidir.")