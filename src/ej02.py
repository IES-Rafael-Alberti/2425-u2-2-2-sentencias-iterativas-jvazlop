'''
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
'''

def entrada():
    """Solicita al usuario su edad, verifica que sea un número mayor que 0 y lo devuelve."""
    edad_Usuario= input("Introduce tu edad: ")
    
    # Verificación para comprobar si el input es un número y mayor que 0
    if not edad_Usuario.isdigit():
        print("Error: La entrada debe ser un número entero.")
        return entrada()
    elif int(edad_Usuario) <= 1:
        print("Error: La edad debe ser mayor que 0.")
        return entrada()
    else:
        return int(edad_Usuario)


def procesamiento(edad):
    """
    Genera un bucle `while` para contar los años cumplidos desde 1 hasta la edad ingresada.
    Devuelve una lista con los años desde 1 hasta la edad.
    """
    anios_cumplidos = []
    contador = 1
    while contador <= edad:
        anios_cumplidos.append(contador)
        contador += 1
    return anios_cumplidos

def salida(anios_cumplidos):
    print("Has cumplido los siguientes años:")
    for anio in anios_cumplidos:
        print(anio)

def main():
    
    # Entrada
    edad = entrada()
    
    # Procesamiento
    anios_cumplidos = procesamiento(edad)
    
    # Salida
    salida(anios_cumplidos)

if __name__ == "__main__":
    main()
