'''
Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. 
Por cada número, informar cuántos dígitos pares y cuántos impares tiene. Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.
'''

def entrada():
    """Solicita al usuario números enteros positivos y devuelve una lista de ellos."""
    numeros = []
    numero = None  # Inicializa el número
    while numero != 0:  # Condición para continuar el bucle
        numero = int(input("Ingrese un número entero positivo (0 para terminar): "))
        if numero < 0:
            print("El número debe ser positivo. Intente nuevamente.")
        elif numero > 0:
            numeros.append(numero)  # Agrega el número a la lista
    return numeros

def contar_digitos(numero):
    #Cuenta los dígitos pares e impares en un número.

    pares = 0
    impares = 0
    while numero > 0:
        digito = numero % 10  # Obtiene el último dígito
        if digito % 2 == 0:
            pares += 1  # Incrementa el contador de pares
        else:
            impares += 1  # Incrementa el contador de impares
        numero //= 10  # Elimina el último dígito del número
    return pares, impares

def procesamiento(numeros):
    """
    Procesa los números y cuenta los dígitos pares e impares.
    Devuelvo el total de dígitos pares e impares leídos en total.
    """
    total_pares = 0
    total_impares = 0
    for numero in numeros:
        pares, impares = contar_digitos(numero)
        print(f"Número: {numero} - Dígitos pares: {pares}, Dígitos impares: {impares}")
        total_pares += pares
        total_impares += impares
    return total_pares, total_impares

def salida(total_pares, total_impares):
    print(f"\nTotal de dígitos pares leídos: {total_pares}")
    print(f"Total de dígitos impares leídos: {total_impares}")

def main():
    # Entrada
    numeros = entrada()
    
    # Procesamiento
    total_pares, total_impares = procesamiento(numeros)
    
    # Salida
    salida(total_pares, total_impares)

if __name__ == "__main__":
    main()
