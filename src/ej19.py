'''
Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. 
A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error. 
El menú se debe volver a mostrar luego de ejecutada cada opción, 
permitiendo volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.
'''

def mostrar_menu():
    print("\n--- Menú de Opciones ---")
    print("1 - Comenzar programa")
    print("2 - Imprimir listado")
    print("3 - Finalizar programa")

def opcion_1():
   print("Has elegido la opción 1: Comenzar programa.")

def opcion_2():
    print("Has elegido la opción 2: Imprimir listado.")

def main():
    continuar = True

    while continuar:
        mostrar_menu()
        seleccion = input("Selecciona una opción (1, 2 o 3): ")

        if seleccion == "1":
            opcion_1()
        elif seleccion == "2":
            opcion_2()
        elif seleccion == "3":
            print("Finalizando el programa. Hasta luego!")
            continuar = False 
        else:
            print("Error: Opción no válida. Por favor, elige 1, 2 o 3.")

if __name__ == "__main__":
    main()
