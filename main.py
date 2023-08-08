from productos import *
import os

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