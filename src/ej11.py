'''
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
'''

def entrada():
    return input("Introduce una palabra: ")

def procesamiento(palabra):
    """
    Coge la palabra ingresada para obtener las letras en orden inverso.
    Devuelvo una lista con las letras invertidas.
    """
    letras_invertidas = []
    indice = len(palabra) - 1
    while indice >= 0:
        letras_invertidas.append(palabra[indice])
        indice -= 1
    return letras_invertidas

def salida(letras):

    print("Las letras en orden inverso son:")
    for letra in letras:
        print(letra)

def main():
    # Entrada
    palabra = entrada()
    
    # Procesamiento
    letras_invertidas = procesamiento(palabra)
    
    # Salida
    salida(letras_invertidas)

if __name__ == "__main__":
    main()
