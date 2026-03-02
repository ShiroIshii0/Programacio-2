import math
def promedio(datos):
    return sum(datos) / len(datos)
def desviacion(datos):
    n = len(datos)
    prom = promedio(datos)
    suma = 0
    for x in datos:
        suma += (x - prom) ** 2
    return math.sqrt(suma / (n - 1))
datos = list(map(float, input("Ingrese 10 números separados por espacio: ").split()))
if len(datos) != 10:
    print("Debe ingresar exactamente 10 números.")
else:
    print(f"El promedio es {promedio(datos):.2f}")
    print(f"La desviación estándar es {desviacion(datos):.5f}")


