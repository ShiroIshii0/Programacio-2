import math
class calcular_el_promedio_y_a_desviacion:
    def __init__(self, datos):
        self.datos = datos
    def promedio(self):
        return sum(self.datos) / len(self.datos)
    def desviacion(self):
        n = len(self.datos)
        prom = self.promedio()
        suma = 0
        for x in self.datos:
            suma += (x - prom) ** 2
        return math.sqrt(suma / (n - 1))
datos = list(map(float, input("Ingrese 10 números separados por espacio: ").split()))

if len(datos) != 10:
    print("Debe ingresar exactamente 10 números.")
else:
    est = calcular_el_promedio_y_a_desviacion(datos)
    print(f"El promedio es {est.promedio():.2f}")
    print(f"La desviación estándar es {est.desviacion():.5f}")