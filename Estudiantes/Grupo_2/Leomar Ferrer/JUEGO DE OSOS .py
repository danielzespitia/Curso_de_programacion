start = input ("estas en un bosque oscuro y encuentras dos objetos unos FOSFOROS y una LINTERNA ¿cual eliges?: ").upper()
 

# NIVEL 1 
if start == "FOSFOROS" :
  print ("Coges el fósforo y lo enciendes 🔥. Por un instante, el bosque se ilumina... ¡y ves un gran oso grizzly! 🐻 El fósforo se apaga.")
  opcion_1 = input (" ¿que quieres hacer? CORRER, LUCHAR o ESCONDERTE:").upper()
  
  if opcion_1 == "CORRER" :
    print("correr es una mala idea el oso te atrapara y te comera, " "FIN DEL JUEGO") 
  elif opcion_1 == "LUCHAR" :
    print("luchar no es una buena opcion el oso es mas grande y mas fuerte que tu", "FIN DEL JUEGO")
  elif opcion_1 == "ESCONDERTE" :
    print("te has escondido detras de un arbusto cercano y no te pudo alcanzar pero sigue merodeando por alli pronto se apagara, el fosforo y quedaras a oscuras")
  else :
    print("se ha apagado el fosforo y el oso te ha encontrado, FIN DEL JUEGO")

if start == "LINTERNA" :
  print("Enciendes la linterna 💡 y ves un camino iluminado. De pronto, oyes algo entre los árboles 🌿.")
  opcion_2 = input ("¿Quieres? SEGUIR el sendero, seguir BUSCANDO o TOMAR nuevo camino :").upper()

  if opcion_2 == "SEGUIR" :
      print("sigues el camino y encuentras una cueva donde se oculta un oso grizzly pero esta dormido ")
  elif opcion_2 == "BUSCANDO" :
       print("sigues buscando para encontrar una salida y esccapar de las garras del oso") 
  elif opcion_2 == "TOMAR" :
        print("has tomado un nuevo camino y has encontrado la salida del bosque y escapado del oso")
  else : 
        print("has logrado escapar del oso y llegas a una nueva aventura en el campamento") 

# NIVEL 2
  start_2 = input("¿que quieres hacer contruir CERCA, TRAMPAS o ARMAS para proteccion del campamento contra los osos? :").upper()
        
  if start_2 == "CERCA" :
          print("has contruido la cerca y te sientes seguro dentro del campamento")
  elif start_2 == "TRAMPAS":
          print("has contruido trampas para atrapar a los osos y proteger el campamento")
  elif start_2 == "ARMAS" :
          print("has contruido arcos y flechas para proteger al campamento de los osos")
  else :
          print("has logrado proteger al campamento de los osos y has ganado la partida")





















