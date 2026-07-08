productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
 '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
 'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
 'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
 'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
 '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
 '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
 'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
    }

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
 'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
 'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]
    }

def stock_marca(marca):
    suma_stock = 0
    for modelo in productos:
        if productos[modelo][0].lower() == marca.lower():
            pc = modelo
            for x in stock:
                if x == pc:
                    suma_stock += stock[x][1]
    print(f"El stock es: {suma_stock}")

def búsqueda_precio(p_min,p_max):
    resultados = []
    for x in stock:
        precio = stock[x][0]
        if p_min <= precio <= p_max and stock[x][1] > 0:
            modelo = x
            for modelos in productos:
                if modelos == modelo:
                    p = f"{productos[modelos][0]}--{modelos}"
                    resultados.append(p)
        else:
            print("No hay notebooks en ese rango de precios.")
    print(f"Los notebooks entre los precios consultas son: {resultados}")

def actualizar_precio(modelo, p):
    for modelos in stock:
        if modelos.lower() == modelo.lower():
            stock[modelos][0] = p
            return True
        else:
            return False

while True:
    print("*** MENU PRINCIPAL ***\n",
        "1. Stock marca.\n",
        "2. Búsqueda por precio.\n",
        "3. Actualizar precio.\n",
        "4. Salir.\n",
    )
    opcion = input("Ingrese opción: ")
    if opcion == "1":
        marca = input("Ingrese marca a consultar: ")
        stock_marca(marca)
    elif opcion == "2":
        try:
            p_min = int(input("Ingrese precio mínimo: "))
            p_max = int(input("Ingrese precio máximo: "))
            búsqueda_precio(p_min,p_max)
        except ValueError:
            print("Debe ingresar valores enteros!!")
    elif opcion == "3":
        while True:
            modelo = input("Ingrese modelo a actualizar: ")
            try:
                p = int(input("Ingrese precio nuevo: "))
                resultado = actualizar_precio(modelo, p)
                if resultado == True:
                    print("Precio actualizado!!")
                else:
                    print("El modelo no existe!!")
            except ValueError:
                print("Ingrese un numero Entero")
            repetir = input("Desea actualizar otro precio (s/n)?:")

            if repetir.lower() == "si" or repetir.lower() == "s":
                continue
            else:
                break
    elif opcion == "4":
        print("Programa finalizado.")
        break
    else:
        print("Debe seleccionar una opción válida!!")