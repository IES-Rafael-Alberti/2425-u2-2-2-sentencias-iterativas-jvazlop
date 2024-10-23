'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
'''

def entrada():

    numero_usuario = input("Introduce un número entero positivo: ")
    
    # Verificación para comprobar si el input es un número y mayor que 0
    if not numero_usuario.isdigit() or int(numero_usuario) <= 0:
        print("Error: La entrada debe ser un número entero positivo.")
        return entrada()
    else:
        return int(numero_usuario)

def procesamiento(numero):
    """
    Verifica si el número ingresado es primo.
    Un número es primo si solo es divisible por 1 y por sí mismo.
    """
    if numero == 1:
        return False  # 1 no es considerado primo
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def salida(es_primo, numero):

    if es_primo:
        print(f"El número {numero} es primo.")
    else:
        print(f"El número {numero} no es primo.")

def main():

    # Entrada
    numero = entrada()
    
    # Procesamiento
    es_primo = procesamiento(numero)
    
    # Salida
    salida(es_primo, numero)

if __name__ == "__main__":
    main()
