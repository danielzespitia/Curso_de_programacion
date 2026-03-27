edad = int(input("¿Cuál es tu edad? "))

print(f"\nBienvenido al programa, tu edad es {edad} años.")

# Nivel 1

if edad == 18:
    print("¡Felicidades! Acabas de alcanzar la mayoría de edad.")
    
    apertura_cuenta = input("\n¿Deseas abrir una cuenta bancaria? (si/no) ").lower()
    
    # Nivel 2
    if apertura_cuenta == "si":
        print("¡Cuenta bancaria abierta exitosamente!")
        
        banco = input("\n¿En qué banco deseas abrir tu cuenta? ").upper()
        
        # Nivel 3
        if (banco == "BANCO MERCANTIL" or banco == "MERCANTIL") or (banco == "BANCO MERCANTIL VENEZUELA" or banco == "MERCANTIL VENEZUELA"):
            print("Has elegido Banco Mercantil, excelente elección.")
            
            
        elif banco == "BANCO PROVINCIAL":
            print("Has elegido Banco Provincial, excelente elección.")
            
        elif banco == "BANESCO":
            print("Has elegido Banesco, excelente elección.")
            
        elif banco == "BANCO DEL CARIBE" or banco == "BANCARIBE":
            print("Has elegido Banco del Caribe, excelente elección.")
            
        else:
            print("Banco no reconocido, por favor elige una opción válida.")
        
    elif apertura_cuenta == "no":
        print("Entendido, no se abrirá una cuenta bancaria.")
    
    else:
        print("Respuesta no válida.")

elif edad > 18 and edad < 60:
    print("Eres mayor de edad.")

elif edad >= 60 and edad <= 100:
    print("Eres un adulto mayor.")
    
elif edad < 18 and edad >= 0:
    print("Eres menor de edad.")
    
else:
    print("Error.")