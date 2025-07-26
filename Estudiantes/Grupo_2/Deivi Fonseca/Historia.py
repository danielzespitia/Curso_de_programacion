
# juego de aventura y toma de decisiones para salir del bosque a salvo.
# el juego comienza conun personaje que hizo una excursion, por algunos motivos de separo del resto de compañeros y se perdio en el bosque
# tiene que salir del boste antes de morir por los animales salvajes y los peligros del bosque eso es su mision

print("decide y sobrevive")
print("te haz separado de tu grupo de compañeros en un bosque muy grande y peligroso")
print("tienes algunas ideas para salir del bosque")
print("¿quieres subir a un arbol para tener mejor vision? si/no")
opcion = input ("si o no:")
if opcion.lower () == "si":
    print("Lo haces, y logras tener una mejor visión y tienes una mejor noción de dónde puedes estar.")
    print("luego de eso decides caminar hacia una direccion que escogiste")
    print("caminas durante algunos minutos y logras llegar a un arroyo y tienes que tomar una desicion")
elif opcion.lower () == "no":
    print("Decides no subir al árbol y buscas otra alternativa pero depues de un tiempo no logras nada pierdes mucho tiempo se hace de noche, y mientras caminas en la oscuridad caes a un barranco y mueres")
else:
    print("Opción no válida. Por favor, responde 'si' o 'no'.")

opcion2 = input ("¿seguir la corriente del rio{1}, pasar al otro lado del rio{2} o acampar en una zona alta que viste en el camino{3}:")
if opcion2 == "1":
    print("Decides seguir la corriente del río y no llegas a nada y oscurece y no puedes hacer nada y un animal salvaje te ataca y mueres")
   
elif opcion2 == "2":
    print("Intentas pasar al otro lado del río. La corriente es más fuerte de lo que pensabas y debido a las rocas, troncos etc mueres debido a los golpes.")
    
elif opcion2 == "3":
    print("Buscas la zona alta que viste. Después de una breve escalada, encuentras un lugar seguro para acampar por la noche.")
    print("con las herramientas que tienes en tu bolso logras hacer un pequeño refugio")
    print("terminas de hacer tu refugio y debes de tomar otra decision")

else:
    print("No existe ninguna repuesta intenta de nuevo.")
opcion3 = input("salir a buscar comida o quedarte y aguantar hasta el proximo dia. salir/quedarte: ")
if opcion3.lower () == "salir":
    print("sales a buscar comida y por el miedo olvidas el camino de regreso caminas sin rumbo y te encuentras un animal y te ataca y mueres")

elif opcion3.lower () == "quedarte":
    print("esperas al dia siguiente y por la mañana buscas comida tranquilamente")
    print("luego de comer sales a explorar la zona")
    print("depues de caminar por un tiempo te encuentras a un oso y tienes que decidir que hacer")

else:
    print("debes escoger obligatoriamente una de las dos opciones")

opcion4 = input("esconderte, correr o subir a un arbol:")
if opcion4.lower () == "esconderte":
    print("rapidamente te colocas detras de arboles y arbustos logras confundir a  el oso y puedes huir")
    print("luego de ese encuentro sabes por donde no debes ir, terminas de explorar la zona y regresas al refugio")
    print("cuando llegas al refugio te pones a pensar en que seria lo mejor, esperar un rescate o tu solo intentar salir del bosque ")
elif opcion4.lower () == "correr":
    print("corres pero no es sufisiente y el oso te alcanza y te mata")
elif opcion4.lower () == "subir a un arbol":
    print("el oso sabe trepar arboles, del miedo te lanzas te rompes una pierna no puedes escapar y el oso te mata")
else:
    print("opcion invalida")

opcion5 = input("esperar un rescate o tu solo salir del bosque:")
if opcion5.lower () == "salir solo del bosque" :
    print("decides reunir todas las raciones y salir tu solo del bosque, al plazo de unos dias estaras bien por las raciones y la experiencia")
    print("pero al ser un bosque tan grande no logras encontrar el camino a casa")
    print("se acabaran las raciones. comenzaran las lluvias y no tendras refugio mas los animales salvajes del bosque pasaran dias y moriras")
elif opcion5.lower () == "esperar un rescate" :
    print("mientras esperas un rescate puedes saber mas sobre de la zona, tener mas recursos y un buen refugio")
    print("ademas puedes recolecctar materiales para hacer señales y puedan encotrarte")
    print("efectivamente, al dia siguiente se escucha un sonido es un helicoptero de rescate")
else:
    print("solo hay dos opciones disponibles")
opcion6 = input("hacer una señal de humo o gritar, silvar hacer ruido:")
if opcion6.lower () == "hacer una señal" :
    print("con los materiales que revogiste logras hacer fuego y con el humo el helicoptero te ve y logras sobrevivir")
    print("FELICIDADES GANASTE EL JUEGO")
elif opcion6.lower () == "hacer ruido" :
    print("al ser un gran bosque y muy denso no logras hacer ruido sufisiente para que los rescatistas te escuchen")
    print("pierdes esa gran oportunidad de salir de ese lugar y mentalmente te derrubas")
    print("y al cabo de unos dias no soportaras y moriras por algun peligro del bosque")
else:
    print("la opcion no existe")