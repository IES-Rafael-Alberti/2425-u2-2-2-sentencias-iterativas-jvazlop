'''
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
'''

def entrada():
    #Solicita al usuario un número del 1 al 10 para la tabla de multiplicar.
    tabla_usuario = input("¿Qué tabla de multiplicar deseas mostrar (1-10)? ")
    
    # Verificación para comprobar si el input es un número del 1 al 10
    if not tabla_usuario.isdigit() or not (1 <= int(tabla_usuario) <= 10):
        print("Error: Debes ingresar un número entero entre 1 y 10.")
        return entrada()
    else:
        return int(tabla_usuario)

def procesamiento(tabla):
    """
    Genera y muestra la tabla de multiplicar solicitada.    
    No devuelve nada, solo imprime la tabla.
    """
    #Procesamiento
    for i in range(1, 11):  # Del 1 al 10 porque el ultimo no cuenta
        resultado = tabla * i
        
        #Salida
        print(f"{tabla} x {i} = {resultado}")

def main():

    # Entrada
    tabla = entrada()
    
    # Procesamiento y salida
    procesamiento(tabla)

if __name__ == "__main__":
    main()
