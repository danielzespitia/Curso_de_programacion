start = print("estas perdido en el bosque y para guiarte solo tienes un fosforo y una linterna")
opcion_1 = input(" cual escojes : FOSFORO o LINTERNA : ").lower()
if opcion_1 == "fosforo":
    print("iluminas con tu fosforo y al hacerlo un oso nota tu presencia ")
    opcion_1_1= input(" \n que haces CORRES O ESCONDERSE \n : ").lower()
    if opcion_1_1 == "corres":
        print("corres y pierdes al oso y te salvas")
        print(" al hacerlo ves un camino a la ciudad que haras ? ")
        otra =input("\n IR ALLA , QUEDARTE EN EL BOSQUE : ").lower()
        if otra == "ir alla":
            print("al ir a la ciudad llegas a tu casa y descansas, pero sientes que deberias ir al bosque.ganaste ")
        elif otra == "quedarte en el bosque":
            print("al quedarte en el bosque conectas con la naturaleza e incluso te haces amigo del oso, has ganado ")
        else:
            print("no hagas eso ahora has perdido")
    elif opcion_1_1 == "esconderse":
        print("te escondes pero el oso te encuentra y te saluda amistosamente, fin del juego")
    else:
        print("no hagas eso ahora has perdido ")


if opcion_1 == "linterna":
    print("\n al usarla ves la salida al bosque y al salir ves dos caminos ,uno te lleva a la ciudad y el otro a una cueva\n")
    opcion_1_2 = input("cual tomas el de la CUEVA o CIUDAD ? :").lower()
    if opcion_1_2 == "cueva":
        print("al ir a la cueva y ver dentro te encuentras con un oso que haces  ")
        otra_2 =input("\n HABLAS CON EL O LO ATACAS :  ").lower()
        if otra_2 =="hablas con el":
            print("al hablar con el te das cuenta que habla español y es muy pana, has ganado un amigo.")
        elif otra_2 == "atacar":
            print("al atacarlo lo lastimas y este se enoja contigo y te demanda , felicidades has perdido el juicio (literal y figurativamente lol ) ")
    if opcion_1_2 == "ciudad":
        print(" vas a la ciudad y te encuentras al oso , parece que trabaja en polar o algo asi . este te invita una cerveza y te haces su amigo. has ganado el juego y una cerveza :D ")
    else: 
        print("ahora has perdido por no saber escribir.")
else:
    print("\n no hablo taka taka, pierdes por tu mala ortografia. \n ")