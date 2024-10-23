'''
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
'''

def entrada():
    """Solicita al usuario que ingrese la contraseña."""
    return input("Introduce la contraseña: ")

def procesamiento(contrasena_guardada):
    """
    Compara la contraseña ingresada por el usuario con la contraseña guardada.
    Continúa solicitando hasta que la contraseña sea correcta.
    """
    contrasena_usuario = entrada()  # Solicita la contraseña al usuario
    while contrasena_usuario != contrasena_guardada:
        print("La contraseña es incorrecta. Inténtalo de nuevo.")
        contrasena_usuario = entrada()
    print("La contraseña es correcta.")

def main():

    # Contraseña almacenada
    contrasena_guardada = "contraseña"
    
    # Procesamiento
    procesamiento(contrasena_guardada)

if __name__ == "__main__":
    main()
