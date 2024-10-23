'''
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
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
    Genera una lista con la cuenta atrás desde el número ingresado hasta 0.
    Devuelve una lista con los números de la cuenta atrás.
    """

    cuenta_atras = []
    for i in range(numero, -1, -1):  # Desde el número ingresado hasta 0
        cuenta_atras.append(i)
    return cuenta_atras

def salida(cuenta_atras):

    """
    Muestra por pantalla la cuenta atrás separada por comas.
    """

    print("Cuenta atrás desde el número ingresado:")
    print(", ".join(map(str, cuenta_atras)))
    #Busque haber si habia alguna manera de convertir los numeros que saqué a string y encontre esta funcion.
    

def main():

    # Entrada
    numero = entrada()
    
    # Procesamiento
    cuenta_atras = procesamiento(numero)
    
    # Salida
    salida(cuenta_atras)

if __name__ == "__main__":
    main()
