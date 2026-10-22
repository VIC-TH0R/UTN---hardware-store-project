def buscar_herramienta_inventario(inventario, nombre):

    posicion = 0
    for articulo in inventario:
        if articulo['herramienta'] == nombre:
            return posicion
        posicion += 1
    return -1

def actualizar_stock(inventario):
    print("************************************************")
    print("\tACTUALIZAR STOCK DEL INVENTARIO")
    print("************************************************")

    if len(inventario) == 0:
        print("EL INVENTARIO ESTÁ VACÍO. NO HAY HERRAMIENTAS PARA MODIFICAR.")
        print("PRESIONE ENTER PARA CONTINUAR")
        input()
        return

    nombre_buscado = input("INGRESE NOMBRE DE LA HERRAMIENTA: ").strip().upper()
    if len(nombre_buscado) == 0:
        raise ValueError("EL NOMBRE NO PUEDE ESTAR VACIO")

    indice = buscar_herramienta_inventario(inventario, nombre_buscado)
    if indice == -1:
        print("LA HERRAMIENTA NO EXISTE EN EL CATALOGO")
        print("INGRESE ENTER PARA CONTINUAR")
        input()
        return

    print("\t1. VENTA\n\t2. INGRESO DE MERCADERIA")
    opcion = input("INGRESE LA OPCION DESEADA (1-2): ").strip()

    if(opcion != "1" and opcion != "2"):
        print("OPCION INCORRECTA. VOLVIENDO AL MENU PRINCIPAL")
        print("INGRESE ENTER PARA CONTINUAR")
        input()
        return

    unidades = int(input("INGRESE LA CANTIDAD DE LA OPCION: "))
    if unidades <= 0:
        raise ValueError("LA CANTIDAD DEBE SER MAYOR 0")
    
    if opcion == "1":
        if unidades > inventario[indice]['cantidad']:
            raise ValueError("LA VENTA SUPERA EL STOCK DISPONIBLE")
        
        inventario[indice]['cantidad'] -= unidades
        print("VENTA REGISTRADA CON EXITO")

    else:
        inventario[indice]['cantidad'] += unidades
        print("INGRESO DE MERCADERIA REGISTRADO CON EXITO")
    
    print("PRESIONE ENTER PARA CONTINUAR")
    input()

def registrar_producto(inventario):

    print("************************************************")
    print("\tDAR DE ALTA UN PRODUCTO NUEVO")
    print("************************************************")

    nombre = input("INGRESE EL NOMBRE DE LA HERRAMIENTA: ").strip().upper()

    if len(nombre) == 0:
        raise ValueError("ENTRADA INVÁLIDA. EL NOMBRE NO PUEDE ESTAR VACIO")
    else:
        duplicado = buscar_herramienta_inventario(inventario, nombre)
        if duplicado > -1:
            raise ValueError("ARTICULO YA REGISTRADO, INTENTE NUEVAMENTE")
        else:
            stock = int(input("INGRESE EL STOCK DEL PRODUCTO: "))

            if stock < 0:
                raise ValueError("EL STOCK NO PUEDE SER NEGATIVO")
            else:
                inventario.append({'herramienta': nombre, 'cantidad': stock})

def consultar_agotados(inventario):

    print("************************************************")
    print("\tREPORTE DE AGOTADOS")
    print("************************************************")

    if len(inventario) == 0:
        print("EL INVENTARIO ESTÁ VACÍO")
        print("INTENTE NUEVAMENTE CUANDO EL INVENTARIO TENGA HERRAMIENTAS")
        print("INGRESE ENTER PARA CONTINUAR")
        input()
        return

    contador_agotados = 0

    for articulo in inventario:
        if articulo['cantidad'] == 0:
            print(f"HERRAMIENTA: {articulo['herramienta']}")
            contador_agotados += 1

    if contador_agotados == 0:
        print("NO SE ENCONTRARON HERRAMIENTAS CON STOCK IGUAL A 0")
        print("INGRESE ENTER PARA CONTINUAR")
        input()

    elif contador_agotados > 0:
        print(f"SE HAN ENCONTRADO {contador_agotados} HERRAMIENTAS CON STOCK IGUAL A 0")
        print("INGRESE ENTER PARA CONTINUAR")
        input()

def consultar_stock(inventario):

    print("************************************************")
    print("\tCONSULTAR STOCK DE UNA HERRAMIENTA")
    print("************************************************")

    if len(inventario) == 0:
        print("EL INVENTARIO ESTÁ VACÍO.")
        print("INTENTE NUEVAMENTE CUANDO EL INVENTARIO TENGA HERRAMIENTAS")
        print("IGRESE ENTER PARA CONTINUAR ")
        input()
        return

    else:
        nombre_buscado = input("INGRESE NOMBRE DE LA HERRAMIENTA PARA SABER STOCK: ").strip().upper()

        if len(nombre_buscado) == 0:
            raise ValueError("EL NOMBRE NO PUEDE ESTAR VACÍO")
        else:
            encontrado = False
            for articulo in inventario:
                if nombre_buscado == articulo['herramienta']:
                    print("ARTÍCULO ENCONTRADO")
                    print(f"HERRAMIENTA: {articulo['herramienta']} | STOCK: {articulo['cantidad']}")
                    encontrado = True
                    print("INGRESE ENTER PARA CONTINUAR")
                    input()
                    break

            if not encontrado:
                print("EL ARTICULO BUSCADO NO EXISTE EN EL INVENTARIO")
                print("INGRESE ENTER PARA CONTINUAR")
                input()

def mostrar_inventario(inventario):

    print("************************************************")
    print("\tMUESTRA EL INVENTARIO ACTUAL")
    print("************************************************")
    
    if len(inventario) == 0:
        print("EL INVENTARIO ESTÁ VACÍO. AÑADA PRODUCTOS AL INVENTARIO PARA MOSTRAR STOCK")
        input()
        return

    for herramientas in inventario:
        print(f"HERRAMIENTA: {herramientas['herramienta']} | CANTIDAD: {herramientas['cantidad']}")

    print("INGRESE ENTER PARA CONTINUAR")
    input()

def cargar_herramientas(inventario):

    print("************************************************")
    print("\tCARGA DE HERRAMIENTAS\t")
    print("************************************************")
    print("*INGRESE 'SALIR' DENTRO DEL NOMBRE DE LA HERRAMIENTA PARA CANCELAR LA CARGA*")

    while True:
        cantidad = input("INGRESE LA CANTIDAD DE HERRAMIENTAS A CARGAR: ")
        try:
            cantidad = int(cantidad)
            if cantidad <= 0:
                raise ValueError("LA CANTIDAD DEBE SER MAYOR A 0")
            break
        except ValueError as e:
            print("ENTRADA INVÁLIDA, INTENTE NUEVAMENTE")
            print(f"Error {e}")
            input()

    for i in range(cantidad):
        print(f"CARGANDO HERRAMIENTA {i +1}/{cantidad}")
        while True:
            try:
                nombre = input("INGRESE NOMBRE DE LA HERRAMIENTA: ").strip().upper()
                if nombre == "SALIR":
                            print("CARGA INTERRUMPIDA. VOLVIENDO AL MENÚ")
                            input()
                            return
                if nombre == "":
                    raise ValueError("EL NOMBRE NO PUEDE ESTAR VACIO")
                
                duplicado = buscar_herramienta_inventario(inventario, nombre)

                if duplicado > -1:
                    raise ValueError("ARTÍCULO YA REGISTRADO, INTENTE NUEVAMENTE")
                break
            except ValueError as e:
                print("ENTRADA INVÁLIDA, INTENTE NUEVAMENTE")
                print(f"Error {e}")
                input()

        while True:
            try:
                stock = input("INGRESE EL STOCK DEL PRODUCTO: ")
                stock = int(stock)
                if stock < 0:
                    raise ValueError("LA CANTIDAD DEBE SER MAYOR O IGUAL A 0")
                break
            except ValueError as e:
                print("ENTRADA INVÁLIDA, INTENTE NUEVAMENTE")
                print(f"ERROR {e}")
                input()

        inventario.append({'herramienta': nombre, 'cantidad': stock})
        print(f"{nombre} REGISTRADO CON ÉXITO")

    print("PRESIONE ENTER PARA CONTINUAR")
    input()

def imprimir_menu():

    print("=====================================")
    print("SELECCIONE UNA OPCION PARA CONTINUAR")
    print("=====================================")
    print("OPCION [1]: CARGAR HERRAMIENTAS")
    print("OPCION [2]: MOSTRAR INVENTARIO")
    print("OPCION [3]: CONSULTAR STOCK")
    print("OPCION [4]: CONSULTAR AGOTADOS")
    print("OPCION [5]: REGISTRAR PRODUCTO")
    print("OPCION [6]: ACTUALIZAR STOCK")
    print("OPCION [7]: SALIR")
    print("=====================================")

def main():
    inventario = []

    while True:

        imprimir_menu()
        opcion = input("---->[ ]<----\033[7D") #\033[7D mueve el cursor 7 espacios atrás
        print()                                #para que se muestre la entrada del usuario
                                                #entre los corchetes
        try:

            opcion = int(opcion)

            if opcion == 1:
                cargar_herramientas(inventario)
            elif opcion == 2:
                mostrar_inventario(inventario)
            elif opcion == 3:
                try:
                    consultar_stock(inventario)
                except ValueError as e:
                    print("ENTRADA INVÁLIDA, INTENTE NUEVAMENTE")
                    print(f"ERROR: {e}")
                    input()
            elif opcion == 4:
                consultar_agotados(inventario)
            elif opcion == 5:
                try:
                    registrar_producto(inventario)
                    print("PRODUCTO CARGADO CON ÉXITO")
                    print("PRESIONE ENTER PARA CONTINUAR")
                    input()

                except ValueError as e:
                    print("ENTRADA INVÁLIDA, INTENTE NUEVAMENTE")
                    print(f"ERROR: {e}")
                    input()

            elif opcion == 6:
                try:
                    actualizar_stock(inventario)
                except ValueError as e:
                    print("ENTRADA INVÁLIDA, INTENTE NUEVAMENTE")
                    print(f"ERROR: {e}")
                    input()
            elif opcion == 7:
                break
            else:
                raise ValueError("Número fuera de rango (1-7)")

        except ValueError as e:
            print("La opción seleccionada no es correcta. Intente nuevamente")
            print(f"Error: {e}")
            input()         #La función de este input es para pausar la ejecución sin
                            #tener que llamar a os.system("pause"), ya que es un comando muy pesado
main()