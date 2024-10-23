'''
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
'''

def entrada():

    return input("Introduce una palabra: ")

def procesamiento(palabra):
    """
    Repite la palabra 10 veces utilizando `while` y 
    devuelve la palabra repetida 10 veces.
    """
    contador = 0
    resultado = ""
    while contador < 10:
        resultado += palabra + "\n"  # Añade la palabra seguida de un salto de línea
        contador += 1
    return resultado

def salida(texto):
    print(texto)


def main():

    #Entrada
    palabra = entrada()

    #Procesamiento
    texto_generado = procesamiento(palabra)

    #Salida
    salida(texto_generado)

if __name__ == "__main__":

    main()