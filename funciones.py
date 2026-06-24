

def menu():
    print("1.Mostrar Productos.")
    print("2.Agregar Producto.")
    print("3.Buscar Producto.")
    print("4.Editar Producto.")
    print("5.Eliminar Producto.")
    print("6.Salir.")

def mostrar_productos(inventario):
    print("Lista de productos.")
    if not inventario:
        print("El inventario esta vacio.")
        return
    for i,prod in enumerate(inventario):
        print(f"{i + 1}. Código: {prod["codigo"]}/nombre: {prod["nombre"]}/precio: ${prod["precio"]}/stock: {prod["stock"]}")


def agregar_producto(inventario):
    print("Agregando producto.")
    ps_correcto = False

    add_codigo = input("Ingrese el código a asignar del producto: ").lower()
    for prod in inventario:
        if prod["codigo"] == add_codigo:
            print("Código ya utilizado, por favor escoja otro.")
            return
    add_nombre = input("Ingrese el nombre del producto: ")

    while ps_correcto == False:

        try:
            add_precio = int(input("Ingrese el monto del producto: "))
            add_stock = int(input("Ingrese el stock del producto: "))
        except ValueError:
            print("El valor ingresado no es valido, debe ser un número positivo.")
        else:
            ps_correcto = True


    add_producto = {
        "codigo": add_codigo, 
        "nombre": add_nombre,
        "precio": add_precio,
        "stock": add_stock
    }
    inventario.append(add_producto)

def buscar_producto(inventario):
    print("Buscando producto.")
    opb_select = False
    print("1. Buscar por código.")
    print("2. Buscar por nombre.")

    while opb_select == False:
        try:
            opb = int(input("Ingrese la opción: "))
        except ValueError:
            print("El dato ingresado no es valido.")
        else:
            if opb in [1,2]:
                opb_select = True
            else:
                print("Opción invalida.")

    if opb == 1:
        print("Buscando por código.")
        busqueda_codigo = input("Ingrese el código a buscar: ").lower()
        for prod in inventario:
            if prod["codigo"] == busqueda_codigo:
                print(f"Código: {prod["codigo"]}/ Nombre: {prod["nombre"].capitalize()}")

    elif opb == 2:
        print("Busqueda por nombre.")
        busqueda_nombre = input("Ingrese el nombre del producto: ").lower()
        for prod in inventario:
            if prod["nombre"] == busqueda_nombre:
                print(f"Código: {prod["codigo"]}/ Nombre: {prod["nombre"]}")

def editar_producto(inventario):
    print("Editando.")

    edit_codigo = input("Ingresa el código del producto a editar: ")
    for prod in inventario:
        if prod["codigo"] == edit_codigo:
            print(f"Producto encontrado. {prod["nombre"].capitalize()}")
            print("Deje en blanco en caso de que no quiera realizar cambios en ese campo.")

            new_codigo = input(f"Ingrese el nuevo código ({prod["codigo"].capitalize()})").lower()
            if new_codigo != "":
                prod["codigo"] = new_codigo

            new_nombre = input(f"Ingrese nuevo nombre de ({prod["nombre"].capitalize()})").lower()
            if new_nombre != "":
                prod["nombre"] = new_nombre

            while True:
                new_precio_str = input(f"Ingrese nuevo precio (${prod["precio"]}): ")
                if new_precio_str == "":
                    break
                try: 
                    prod["precio"] = int(new_precio_str)
                    break
                except ValueError:
                    print("Error: El precio debe ser un número entero.")
                
            while True:
                new_stock_str = input(f"Ingrese nuevo stock (${prod["stock"]}): ")
                if new_stock_str == "":
                    break
                try: 
                    prod["stock"] = int(new_stock_str)
                    break
                except ValueError:
                    print("Error: El stock debe ser un número entero.")
            print("Producto actualizado con exito!.")
    print("No se encontro un código.")

def eliminar_producto(inventario):
    print("Eliminando producto.")
    del_producto_codigo =  input("Ingrese el código del producto a eliminar: ").lower()
    for prod in inventario:
        if prod["codigo"] == del_producto_codigo:
            print(f"Estás seguro de eliminar el producto ({prod["nombre"]})?")
            confirm = input("Ingrese 'si' para confirmar: ").lower()

            if confirm == "si":
                inventario.remove(prod)
                print("Producto eliminado con exito.")
            else:
                print("Operación cancelada.")
            return
        
def comenzar_app(inventario):
    salir = False

    while salir == False:
        menu()
        try:
            opt = int(input("Ingrese la opción a elegir: "))
        except ValueError:
            print("El valor ingresado no es valido.")
        else:
            if opt == 1:
                mostrar_productos(inventario)
            elif opt == 2:
                agregar_producto(inventario)
            elif opt == 3:
                buscar_producto(inventario)
            elif opt == 4:
                editar_producto(inventario)
            elif opt == 5:
                eliminar_producto(inventario)
            elif opt == 6:
                print("Gracias por utilizar la app!!!")
                salir = True
