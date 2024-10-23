'''
Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), 
cortando el ingreso de datos cuando el usuario ingrese el monto 0. Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. 
Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.
'''

def entrada():
    """Solicita al usuario que ingrese montos de compras y devuelve una lista de montos válidos."""
    montos = []
    monto = None
    while monto != 0:
        monto = float(input("Ingrese el monto de la compra (0 para terminar): "))
        if monto < 0:
            print("El monto no puede ser negativo. Intente nuevamente.")
        elif monto > 0:
            montos.append(monto)
    return montos

def procesamiento(montos):
    """
    Calcula el total de montos ingresados.
    Aplica un descuento del 10% si el total supera $1000.
    """
    total = sum(montos)
    if total > 1000:
        total *= 0.9
    return total

def salida(total):
    print(f"El total a pagar es: ${total:.2f}")

def main():
    # Entrada
    montos = entrada()
    
    # Procesamiento
    total = procesamiento(montos)
    
    # Salida
    salida(total)

if __name__ == "__main__":
    main()
