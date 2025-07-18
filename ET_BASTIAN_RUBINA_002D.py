productos = {
    "8475HD": ["HP", 15.6, "8GB", "DD", "1T", "Intel Core i5", "Nvidia GTX1050"],
    "2175HD": ["lenovo", 14, "4GB", "SSD", "512GB", "Intel Core i5", "Nvidia GTX1050"],
    "JjfFHD": ["Asus", 14, "16GB", "SSD", "256GB", "Intel Core i7", "Nvidia RTX2080Ti"],
    "fgdxFHD": ["HP", 15.6, "8GB", "DD", "1T", "Intel Core i3", "integrada"],
    "GF75HD": ["Asus", 15.6, "8GB", "DD", "1T", "Intel Core i7", "Nvidia GTX1050"],
    "123FHD": ["lenovo", 14, "6GB", "DD", "1T", "AMD Ryzen 5", "integrada"],
    "342FHD": ["lenovo", 15.6, "8GB", "DD", "1T", "AMD Ryzen 7", "Nvidia GTX1050"],
    "UWU131HD": ["Dell", 15.6, "8GB", "DD", "1T", "AMD Ryzen 3", "Nvidia GTX1050"],
}

stock = 1
    {"8475HD": [387990,10], "2175HD": [327990,4], "JjfFHD": [424990,1],
    "fgdxFHD": [664990,21], "123FHD": [290890,32], "342FHD": [444990,7],
    "GF75HD": [749990,2], "UWU131HD": [349990,1], "FS1230HD": [249990,0], ...
}

def stock_marca(marca):
    total_stock = 0
    for modelo, info in productos.items():
        if info[0].lower() == marca.lower():
            total_stock += stock.get(modelo, [0.0])[1]
    print(f"el stock es:{total_stock}")

def busqueda_precio(p_min, p_max):
    resultados = []
    for modelo, (precio, cant_stock) in stock.items():
        if p_min <= precio <= p_max and cant_stock > 0:
            marca = productos [modelos][0]
            resultados.append(f"{marca}--{modelo}")
        if resultados:
            resultados.sort()
            print(f"los notebooks entre los precios consultados son: {resultados}")
        else
            print("no hay notebooks en ese rango de precios.")

def actualizar_precio(modelo, nuevo_precio):
    if modelo in sotck:
        stock[modelo][0] = nuevo_precio
        return True
    else:
        return False

while True:
print("\n*** MENU PRINCIPAL ***")
print(" 1. Stock marca.")
print(" 2. Búsqueda por precio.")
print(" 3. Actualizar precio.")
print("4. Salir.")

opcion = input("ingrese opcion: ")
if opcion == "1":
    marca = input("ingrese marca a consultar:")
    stock_marca(marca)

elif opcion == "2":
    while True:
        try:
            p_min = int(input("ingrese precio minimo: "))
            p_max = int(input("ingrese precio maximo: "))
            break
        except ValueEror:
            print("debe ingresar valores enteros")
    busqueda_precio(p_min, p_max)
elif opcion == "3":
    while True:
        modelo = input("Ingrese modelo a actualizar: ")
        try:
            nuevo_precio = int(input("Ingrese precio nuevo: "))
        except ValueError:
            print("Debe ingresar un precio válido.")
            continue
        exito = actualizar_precio(modelo, nuevo_precio)
        if exito:
            print("Precio actualizado!!")
        else:
            print("El modelo no existe!!")
        otra = input("Desea actualizar otro precio (s/n)?: ").lower()
        if otra != "s":
            break
        elif opcion == "4":
            print("Programa finalizado.")
            break

        else:
            print("Debe seleccionar una opción válida!!")
menu()


        
        
        
        
        
        
