opcion = input("Estás caminando por un bosque oscuro y encuentras dos objetos... Un fósforo y una linterna. ¿Cual decides tomar? 'FÓSFORO' o 'LINTERNA'):")
print()
  # PRIMER NIVEL
print()
if opcion.lower() == "fosforo":
    print()
    print("Coges el fósforo y lo enciendes. Por un instante, el bosque se ilumina... ¡y ves un gran oso grizzly! El fósforo se apaga.")
    print()
  # SEGUNDO NIVEL
    print()
    decision = input("Deseas 'CORRER' o 'ESCONDERTE':")
    print()
    if decision.lower() == "correr":
        print()
        print("corriste lo mas rapido que pudiste y te lesionaste, pero venia el oso a 1500 caballos de fuerza y no sabias que hacer.")
        print()
        # TERCER NIVEL
        print()
        decision = input("¿Quieres 'CONTINUAR' escapando del oso super sayayin o quieres morir?:")
        print()
        if decision.lower() == "continuar":
         print()
         print("Sigues corriendo todo miedoso de la nada el oso te tira un chancletazo y te decapita.. GAME OVER.")
         print()
         # CUARTO NIVEL
         print()        
    if decision.lower() == "esconderte":
        print()
        print("Te escondeis detras de una mata el oso te encuentra te da un abrazo pero por su gran peso mueres aplastado por el oso.. GAME OVER")
        print()
        # QUINTO NIVEL
        print()
elif opcion.lower() == "linterna":
    print()
    print("Enciendes la linterna y ves un camino iluminado. De pronto, oyes algo entre los árboles")
    print()
        # SEXTO NIVEL
    decision = input("Deseas 'SEGUIR' o 'BUSCAR':")
    print()
    if decision.lower() == "buscar":
     print()
     print("Estuviste buscando bastante rato y resulto ser que entraste en la base militar de los gringozuela y te aniquilaron por pasau... GAME OVER")
     print()
     # SÉPTIMO NIVEL
    elif decision.lower() == "seguir":
     print()
     print("Sigues el camino y encuentras un lugar seguro para dormir. ¡¡¡¡ESTAS A SALVO FELICIDADES!!!!") 
     print()
     decision = input("¿Quieres 'BUSCAR' verdad brollero no quieres seguir durmiendo en el bosque?:")
     print()
     decision = input ("¿¿ESTAS SEGURO?? 'SI' o 'SI':")
     print()
     print("Te acercas al ruido y descubres que era una patrulla policial que estaba buscando al mismo oso que te habias encontrado anteriormente, te llevan a la ciudad para que te recuperaras una semana de estar en el hospital, resulta que al salir se encuentra con que todas las personas son osos... FINAL BUENO FELICIDADES TE GANASTE UNA PALETA.")
else:
        print("No elegiste la opcion correcta. El oso te encuentra.")