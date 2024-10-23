'''
Leer números enteros de teclado, hasta que el usuario ingrese el 0.
Finalmente, mostrar la sumatoria de todos los números ingresados.
'''
#Entrada
def entrada():
    numero_usuario = input("Introduce un número entero (0 para terminar): ")
    
    # Verificación para comprobar si el input es un número entero
    if not numero_usuario.lstrip('-').isdigit():
        print("Error: Debes ingresar un número entero.")
        return entrada()
    return int(numero_usuario)

def procesamiento():
    """
    Sumo todos los números ingresados por el usuario hasta que ingrese un 0.
    Devuelvo la suma total.
    """
    suma = 0
    numero = entrada()
    
    while numero != 0:
        suma += numero
        numero = entrada()
    
    return suma

def salida(suma_total):

    print(f"La suma total de los números ingresados es: {suma_total}")

def main():
    # Procesamiento
    suma_total = procesamiento()
    
    # Salida
    salida(suma_total)

if __name__ == "__main__":
    main()
