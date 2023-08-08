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