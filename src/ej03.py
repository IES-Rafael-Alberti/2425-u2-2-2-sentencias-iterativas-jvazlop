'''
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
'''

def entrada():
    """Solicita al usuario un número entero positivo y lo devuelve."""
    numero_usuario = input("Introduce un número entero positivo: ")
    
    # Verificación para comprobar si el input es un número y mayor que 0
    if not numero_usuario.isdigit():
        print("Error: La entrada debe ser un número entero positivo.")
        return entrada()
    elif int(numero_usuario) <= 0:
        print("Error: El número debe ser positivo.")
        return entrada()
    else:
        return int(numero_usuario)

def procesamiento(numero):
    """
    Genera una lista de números impares desde 1 hasta el número ingresado.
    Devuelve una lista con los números impares.
    """
    impares = []
    for i in range(1, numero + 1):
        if i % 2 != 0:  # Comprobamos si el número es impar
            impares.append(i)
    return impares

def salida(numeros_impares):
    """Muestra por pantalla todos los números impares separados por comas."""
    print("Números impares desde 1 hasta el número ingresado:")
    print(", ".join(map(str, numeros_impares)))

def main():
    # Entrada
    numero = entrada()
    
    # Procesamiento
    numeros_impares = procesamiento(numero)
    
    # Salida
    salida(numeros_impares)

if __name__ == "__main__":
    main()
