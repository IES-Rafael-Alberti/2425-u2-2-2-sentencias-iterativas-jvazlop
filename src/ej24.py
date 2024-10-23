'''
Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, 
finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.
'''

def es_primo(numero):
    """Determina si un número es primo o no."""
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def entrada():
    numeros = []
    numero = -1

    while numero != 0:
        numero = int(input("Ingrese un número mayor que 1 (0 para terminar): "))
        if numero > 1:  # Solo agregamos números mayores que 1
            numeros.append(numero)

    return numeros

def procesamiento(numeros):
    contador_primos = 0
    for numero in numeros:
        if es_primo(numero):
            contador_primos += 1
    return contador_primos

def salida(contador_primos):
    print(f"Se ingresaron {contador_primos} números primos.")

def main():
    # Entrada
    numeros = entrada()
    
    # Procesamiento
    contador_primos = procesamiento(numeros)
    
    # Salida
    salida(contador_primos)

if __name__ == "__main__":
    main()
