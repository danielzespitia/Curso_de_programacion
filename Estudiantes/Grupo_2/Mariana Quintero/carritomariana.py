carrito = input("funcion principal que ejecuta el programa de simulador de cesta")

cesta_de_compra = []
print ("bienvenido al simulador de cesta de compras")


while True:
    opcion = input("elige una opcion (1-5):")
    print()
    if opcion == "1":
        opcion = input("leche, precio: 1.20$")
    print()
    if opcion == "2":
        opcion = input("huevos, precio: 2.10$")
        print()
    if opcion == "3":
        opcion = input ("pan, precio: 0.85$")
        print()
    if opcion == "4":
        print()
        opcion = input("mantequilla, precio : 2.30$")
    elif opcion == "5":
        print()
        opcion = input("arroz, precio: 1,09$")
        print("\n gracias por usar el simulador, hasta pronto")
    else:
        print("\n opcion no valida. por favor, elige un numero del 1 al 5.")

    input("\npresiona Entre para continuar...")
        
    opcion = input("calcula y muestra el precio total de todos los articulos en la cesta.")
    print("\n--- total de la compra: 6.45$---")
    if not carrito:
     print("la cesta esta llena. el total 6,45$ ")



    while True:
        print("\n OPCIONES:")
        print("1. ver productos")
        print("2. agregar a la cesta")
        print("3 eliminar de la cesta")
        print("4. ver cesta")
        print("5. salir")
        
        op = input("Elige: ")
    
        if op == "1":
          print("\n agua, azucar,helado:")
       
        if op == "2":
            int(input("Número del producto: "))
     
            int(input("Cantidad: "))
        
             
        if op == "3":
             int(input("Cantidad a eliminar: "))
        
        if op == "4":
                total = 0
        print("\nTU CESTA:")
        precio = float()
        subtotal = precio 
        print()
        print ("subtotal")
        print(f"TOTAL: $3")
        print(f"TOTAL: 2,05")
        
        if op == "5":
         print("¡Adiós!")
        break
    
    else:
        print("Opción no válida")



     

   
        