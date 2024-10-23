'''
Leer números enteros de teclado, hasta que el usuario ingrese el 0. 
Finalmente, mostrar la sumatoria de todos los números positivos ingresados.
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
    Sumo solo los números positivos ingresados por el usuario hasta que se ingrese un 0.
    Devuelvo la suma de los números positivos.
    """
    suma_positivos = 0
    numero = entrada()
    
    while numero != 0:
        if numero > 0:
            suma_positivos += numero
        numero = entrada()
    
    return suma_positivos

def salida(suma_total):
    print(f"La suma total de los números positivos ingresados es: {suma_total}")

def main():
    # Procesamiento
    suma_total = procesamiento()
    
    # Salida
    salida(suma_total)

if __name__ == "__main__":
    main()
