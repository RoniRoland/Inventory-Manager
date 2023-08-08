from productos import Producto
import os
lista_productos = []

# Funcion que verifica si el archivo existe o no, se utilizo la libreria OS
def elegirArchivo():
    # Leemos la ruta/nombre del archivo a leer por consola
    archivo = str(input("Escribe el nombre o ruta del archivo para cargar: "))
    while not os.path.isfile(archivo):  # Comprobamos que el archivo existe
        print("\nERROR: No se encontró el archivo\n")
        # Volvemos a leer la ruta/nombre del archivo
        archivo = str(
            input("Escribe el nombre o ruta del archivo para cargar: "))
    else:
        return archivo  # Si el archivo existe, devuelve la ruta/nombre

def cargarInv(lista):
    archivo = elegirArchivo()
    # Se verifica si el archivo no esta vacio para que se prosiga con la lectura
    if archivo != None:
        fichero = open(archivo, 'r')
        
    for linea in fichero:
        partes = linea.strip().split(';')
        if len(partes) == 4:
            nombre = partes[0]
            cantidad = int(partes[1])
            precio_unitario = float(partes[2])
            ubicacion = partes[3]
            
            producto = Producto(nombre, cantidad, precio_unitario, ubicacion)
            lista.append(producto)









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
    while True:
        try:
            option = int(input("Ingrese una opcion: "))
            if option == 1:
                print('\n============CARGA DE ARCHIVO==============\n')
                cargarInv(lista_productos)
                print(
                    "\n********************ARCHIVO CARGADO EXITOSAMENTE*****************\n")
                input('\nPresione enter para continuar...')
                menuPrincipal()
                break
            elif option == 2:
                break
            elif option == 3:
                break
            elif option == 0:
                break
            else:
                print("Opcion incorrecta")
        except ValueError:
            print("Opcion incorrecta")
    exit


print(
    """\n============= LENGUAJES FORMALES DE PROGRAMACION A- ====================
                        201212891
                    Edgar Rolando Ramirez Lopez
========================================================================\n"""
)
input("\n      Presione cualquier tecla para continuar...       ")
menuPrincipal()