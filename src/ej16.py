'''
Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. 
Informar cuál fue el mayor número ingresado.
'''
#Entrada
def entrada():
    numero_usuario = input("Introduce un número entero positivo (0 para terminar): ")
    
    # Verificación para comprobar si el input es un número entero
    if not numero_usuario.lstrip('-').isdigit():
        print("Error: Debes ingresar un número entero positivo.")
        return entrada()
    return int(numero_usuario)

def procesamiento():
    """
    Leo números enteros positivos hasta que el usuario ingresa 0 y determina 
    cuál fue el mayor número ingresado. 
    Devuelvo el mayor número ingresado.
    """
    mayor_numero = None
    numero = entrada()

    while numero != 0:
        if numero > 0:
            if mayor_numero is None or numero > mayor_numero:
                mayor_numero = numero
        numero = entrada()
    
    return mayor_numero

def salida(mayor_numero):
    if mayor_numero is not None:
        print(f"El mayor número positivo ingresado es: {mayor_numero}")
    else:
        print("No se ingresaron números positivos.")

def main():
    # Procesamiento
    mayor_numero = procesamiento()
    
    # Salida
    salida(mayor_numero)

if __name__ == "__main__":
    main()
