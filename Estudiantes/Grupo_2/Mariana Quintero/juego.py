opcion = input("estas caminando por un bosque oscuro y encuentras dos objetos: un *FOSFORO* O una *LINTERNA* con cual te quedas?")
print()
if opcion == "LINTERNA":
    print("la linterna esta encendida")
opcion = input("quieres *SEGUIR* el camino o *BUSCAR* entre los arboles lo que hizo el ruido?")
print()
if opcion == "BUSCAR":
    print("buscaste donde estaba ese misterioso ruido,pero escuchaste el mismo sonido detras de ti")
opcion = input("deseas *CORRER* o *VOLTEAR*")
print()
if opcion == "CORRER":
    print("corriste lo mas rapido que pudiste, sin emabrgo, sentias que cada vez estabas mas cerca, mientras corrias te tropezaste con una piedra y te desmayaste")
opcion = input("despertaste mareado y lo unico que tienes a tu alrededor es una casa abandonada, deseas entrar? *SI* *NO*")
print()
if opcion == "SI":
    print("entraste a la casa abandonada, observaste que todo estaba hecho pedazos y muy tenebroso")
opcion = input("quieres pasar la noche en la casa abandonada? *PASAR LA NOCHE* *DEJAR LA CASA*")
if opcion == "PASAR LA NOCHE":
    print("te quedaste dormido hasta que luego volviste a escuchar el mismo sonido que te perseguia")
else:
    print("no debiste quedarte en la casa, quien habitaba alli era un oso tenebroso y muerto de hambre, terminaste devorado XD")
    print()

if opcion == "FOSFORO":
    print("lograste encender un fosfoto")
elif opcion == "FOSFORO":
    print("justo te quedan 3 fosforos")
else:
    print("habia mucha lluvia y no pudiste prender ningun fosforo, un tenebroso oso grizly te devora por completo en la ocuridad.")
opcion = input("fin de juego,deseas volver a jugar? *VOLVER A JUGAR* *SALIR DEL JUEGO*")    





