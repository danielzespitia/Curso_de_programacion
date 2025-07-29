compras = []
precios = []
total = 0

while True:
    producto = input("Ingrese un producto (q para salir): ").lower()
    if producto == "q":
       break
   
    else:
        
        precio = float(input(f"Ingrese el precio del producto {producto} : $"))
        compras.append(producto)
        precios.append(precio)
        
print("----------Tu carrito de compras----------")

for producto in compras:
    print(producto)
    
print()
for precio in precios:
    total += precio
    
print(f"Total es ${total:.2f}")











































