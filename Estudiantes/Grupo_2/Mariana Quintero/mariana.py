opcion = input("estas caminando por un bosque oscuro y encuentras dos objetos: un *Fosforo* O una *linterna* con cual te quedas?").lower()
print()
if opcion == "linterna":
  print("la linterna esta encendida")
print()
opcion = input("quieres *seguir* el camino o *buscar* entre los arboles lo que hizo el ruido?")
print()
if opcion == "buscar":
 print("buscaste donde estaba ese misterioso ruido,pero escuchaste el mismo sonido detras de ti")
opcion = input("deseas *CORRER* o *VOLTEAR*")
print()
if opcion.lower == "correr":
     print("corriste lo mas rapido que pudiste, sin emabrgo, sentias que cada vez estabas mas cerca, mientras corrias te tropezaste con una piedra y te desmayaste")
opcion = input("despertaste mareado y lo unico que tienes a tu alrededor es una casa abandonada, deseas entrar? *si* *no*")
print()
if opcion == "si":
      print("entraste a la casa abandonada, observaste que todo estaba hecho pedazos y muy tenebroso")
opcion = input("quieres pasar la noche en la casa abandonada? *pasar la noche* *dejar la casa*")
if opcion == "pasar la noche":
    print("te quedaste dormido hasta que luego volviste a escuchar el mismo sonido que te perseguia")
    print("no debiste quedarte en la casa, quien habitaba alli era un oso tenebroso y muerto de hambre, terminaste devorado XD")
    print()


if opcion == "FOSFORO":
    print("lograste encender un fosforo")
    opcion1 = input ("¿deseas esperar que deje de llover para encender los otros fosforos? *SI* *NO*")
    if opcion1 == "NO":
     print("solo te quedan 2 fosforos")
    elif opcion1 == "SI":
        print("esperaste demasiado, el frio de la lluvia y la oscuridad te consumieron a tal grado que moriste de hipotermia")
    else:
      print("habia mucha lluvia y no pudiste prender ningun fosforo, un tenebroso oso grizly te devora por completo en la oscuridad.")
    opcion = input("fin de juego,deseas volver a jugar? *VOLVER A JUGAR* *SALIR DEL JUEGO*")    





