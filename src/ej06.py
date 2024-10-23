'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla un 
triángulo rectángulo como el de más abajo, de altura el número introducido.
'''

def entrada():
    """Solicita al usuario un número entero positivo y lo devuelve."""
    numero_usuario = input("Introduce un número entero positivo para la altura del triángulo: ")
    
    # Verificación para comprobar si el input es un número y mayor que 0
    if not numero_usuario.isdigit() or int(numero_usuario) <= 0:
        print("Error: La entrada debe ser un número entero positivo.")
        return entrada()  # Volvemos a pedir el número si el input no es válido
    else:
        return int(numero_usuario)

def procesamiento(altura):

    #Genera un triángulo rectángulo de altura dada.

    for i in range(1, altura + 1):
        print('*' * i)

def main():

    # Entrada
    altura = entrada()
    
    # Procesamiento
    procesamiento(altura)

if __name__ == "__main__":
    main()
