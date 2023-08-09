from productos import Producto
import os


def cargarInv(nombreArchivo):
    lista_productos = []
    with open(nombreArchivo, "r") as archivo:
        lineas = archivo.readlines()

    for linea in lineas:
        partes = linea.strip().split(" ")
        if len(partes) == 2 and partes[0] == "crear_producto":
            sub_partes = partes[1].split(";")
            if len(sub_partes) == 4:
                nombre, cantidad, precio_unitario, ubicacion = sub_partes
                producto = Producto(
                    nombre, int(cantidad), float(precio_unitario), ubicacion
                )
                lista_productos.append(producto)

    return lista_productos


def elegirArchivo():
    while True:
        nombreArchivo = str(input("Escribe el nombre o ruta del archivo para cargar: "))
        if nombreArchivo.endswith(".inv"):
            if os.path.exists(nombreArchivo):  # Verificar si el archivo existe
                print("\n*-*-*-*-*-Archivo cargado exitosamente.*-*-*-*-*-")
                return nombreArchivo
            else:
                print("El archivo no existe.")
        else:
            print("El archivo debe tener la extensión .inv.")


def elegirArchivoMovs():
    while True:
        nombreArchivo = str(input("Escribe el nombre o ruta del archivo para cargar: "))
        if nombreArchivo.endswith(".mov"):
            if os.path.exists(nombreArchivo):  # Verificar si el archivo existe
                print("\n*-*-*-*-*-Instrucciones cargadas exitosamente.*-*-*-*-*-\n")
                return nombreArchivo
            else:
                print("El archivo no existe.")
        else:
            print("El archivo debe tener la extensión .mov.")


def informeInv(productos):
    with open("informe_inventario.txt", "w") as archivo_salida:
        archivo_salida.write("Informe de Inventario:\n")
        archivo_salida.write("\n")
        archivo_salida.write(
            "Producto        Cantidad          Precio Unitario         Valor Total            Ubicacion\n"
        )
        archivo_salida.write(
            "-------------------------------------------------------------------------------------------\n"
        )

        for producto in productos:
            valor_total = producto.cantidad * producto.precio_unitario
            valorFormateado = f"{valor_total:.2f}"
            linea = f"{producto.nombre.ljust(15)} {str(producto.cantidad).ljust(20)} ${str(producto.precio_unitario).ljust(20)}  ${str(valorFormateado).ljust(20)}  {producto.ubicacion}\n"
            archivo_salida.write(linea)

        print("Informe de inventario generado exitosamente.")


def actualizar_stock(productos, archivo_actualizar):
    try:
        with open(archivo_actualizar, "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(";")

                if len(datos) == 3 and datos[0].startswith("agregar_stock"):
                    nombre = datos[0].split()[1]
                    cantidad = int(datos[1])
                    ubicacion = datos[2]
                    for producto in productos:
                        if (
                            producto.nombre == nombre
                            and producto.ubicacion == ubicacion
                        ):
                            producto.cantidad += cantidad
                            print(
                                f"Se agregaron {cantidad} unidades de {nombre} en {ubicacion}."
                            )
                            break
                    else:
                        print(f"No se encontró el producto {nombre} en {ubicacion}.")

                if len(datos) == 3 and datos[0].startswith("vender_producto"):
                    nombre = datos[0].split()[1]
                    cantidad = int(datos[1])
                    ubicacion = datos[2]
                    for producto in productos:
                        if (
                            producto.nombre == nombre
                            and producto.ubicacion == ubicacion
                        ):
                            if producto.cantidad >= cantidad:
                                producto.cantidad -= cantidad
                                print(
                                    f"Venta de {cantidad} unidades de {nombre} en {ubicacion} realizada."
                                )
                            else:
                                print(
                                    f"No hay suficiente stock de {nombre} en {ubicacion} para vender {cantidad}."
                                )
                            break
                    else:
                        print(f"No se encontró el producto {nombre} en {ubicacion}.")

    except FileNotFoundError:
        print("El archivo no existe.")


def menuPrincipal():
    print(
        """\n==================================================================
        Practica 1 - Lenguajes formales de Programacion 
==================================================================
        # Sistema de Inventario:\n
        
        1.- Cargar Inventario inicial
        2.- Cargar Instrucciones de movimiento
        3.- Crear Informe de Inventario
        0.- Salir
\n...................................................................\n"""
    )
    option = int(input("Ingrese una opcion: "))
    return option


if __name__ == "__main__":
    nuevos_productos = []
    while True:
        option = menuPrincipal()
        try:
            if option == 1:
                print("\n============CARGA DE ARCHIVO==============\n")
                nombreArchivo = elegirArchivo()
                if nombreArchivo:
                    nuevos_productos = cargarInv(nombreArchivo)
                input("\nPresione enter para continuar...")
            elif option == 2:
                if len(nuevos_productos) > 0:
                    print("\n============CARGA DE ARCHIVO MOVIMIENTOS==============\n")
                    nombreArchivoMovs = elegirArchivoMovs()
                    if nombreArchivoMovs:
                        actualizar_stock(nuevos_productos, nombreArchivoMovs)
                else:
                    print("No hay productos para realizar movimentos.")
            elif option == 3:
                if len(nuevos_productos) > 0:
                    informeInv(nuevos_productos)
                    os.system("informe_inventario.txt")
                else:
                    print("\nNo hay productos para generar el informe.")
            elif option == 0:
                break
            else:
                print("Opcion incorrecta")
        except ValueError:
            print("Opcion incorrecta")
    exit
