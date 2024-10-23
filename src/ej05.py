'''
Escribir un programa que pregunte al usuario una cantidad a invertir, 
el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión 
cada año que dura la inversión.
'''

def entrada():

    """
    Solicita al usuario la cantidad a invertir, 
    el interés anual y el número de años.
    """
    
    cantidad_invertir = input("Introduce la cantidad a invertir: ")
    interes_anual = input("Introduce el interés anual (%): ")
    años = input("Introduce el número de años: ")

    return float(cantidad_invertir), float(interes_anual), int(años)

def procesamiento(cantidad, interes, años):
    """
    Calcula el capital al final de cada año.
    Devuelve una lista con el capital obtenido al final de cada año.
    """
    capital = cantidad
    capital_por_anio = []

    for año in range(1, años + 1):
        capital *= (1 + interes / 100) 
        capital_por_anio.append(round(capital, 2))
    return capital_por_anio

def salida(capital_por_anio):
    #Muestra por pantalla el capital obtenido al final de cada año.

    print("Capital obtenido al final de cada año:")
    for año, capital in enumerate(capital_por_anio, start=1):
        print(f"Año {año}: {capital} €")

def main():

    # Entrada
    cantidad, interes, años = entrada()
    
    # Procesamiento
    capital_por_año = procesamiento(cantidad, interes, años)
    
    # Salida
    salida(capital_por_año)

if __name__ == "__main__":
    main()
