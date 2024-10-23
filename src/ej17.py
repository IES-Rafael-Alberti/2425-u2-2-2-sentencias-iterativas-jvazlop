'''
Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.
'''

def entrada():
    numero_usuario = input("Introduce un número entero positivo: ")
    
    # Verificación para comprobar si el input es un número entero positivo
    if not numero_usuario.isdigit() or int(numero_usuario) <= 0:
        print("Error: Debes ingresar un número entero positivo.")
        return entrada()
    else:
        return int(numero_usuario)

def procesamiento(numero):
    """
    Calcula la suma de los dígitos del número ingresado.
    Devuelve la suma de los dígitos.
    """
    suma_digitos = 0
    
    while numero > 0:
        suma_digitos += numero % 10  # Sumo el último dígito
        numero //= 10  # Elimino el último dígito del número
    
    return suma_digitos

def salida(suma):
    print(f"La suma de los dígitos es: {suma}")

def main():
    # Entrada
    numero = entrada()
    
    # Procesamiento
    suma_digitos = procesamiento(numero)
    
    # Salida
    salida(suma_digitos)

if __name__ == "__main__":
    main()
