'''
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
'''

def entrada():
    frase = input("Introduce una frase: ")
    letra = input("Introduce una letra: ")
    
    #Aseguramos que solo se ingrese una letra
    while len(letra) != 1:
        print("Error: Debes introducir solo una letra.")
        letra = input("Introduce una letra: ")
    
    return frase, letra

def procesamiento(frase, letra):

    #Cuenta cuántas veces aparece la letra en la frase.

    contador = 0
    for caracter in frase:
        if caracter == letra:
            contador += 1
    return contador

def salida(contador, letra):

    print(f"La letra '{letra}' aparece {contador} veces en la frase.")

def main():
    # Entrada
    frase, letra = entrada()
    
    # Procesamiento
    contador = procesamiento(frase, letra)
    
    # Salida
    salida(contador, letra)

if __name__ == "__main__":
    main()
