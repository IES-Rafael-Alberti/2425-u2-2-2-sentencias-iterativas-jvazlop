'''
Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). Recorrer la frase, carácter a carácter, comparando con la letra buscada. 
Si el carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar.
Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.
'''

def entrada():
    """Solicita al usuario una frase y una letra."""
    frase = input("Introduce una frase: ")
    letra = input("Introduce una letra a buscar: ")
    return frase, letra

def procesamiento(frase, letra):
    """
    Recorre la frase carácter a carácter.
    Si encuentra la letra, indica la posición y finaliza.
    Si no coincide, indica que no hay coincidencia en esa posición.
    """
    for i in range(len(frase)):
        if frase[i] == letra:
            print(f"La letra '{letra}' se encuentra en la posición {i}.")
            return  # Finaliza la ejecución si encuentra la letra
        else:
            print(f"No hay coincidencia en la posición {i}.")

def main():
    # Entrada
    frase, letra = entrada()
    
    # Procesamiento
    procesamiento(frase, letra)

if __name__ == "__main__":
    main()
