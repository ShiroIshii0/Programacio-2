import math

class Ecuaciones_Cuadraticas:

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
    def getDiscriminante(self):
        return self.__b**2 - 4*self.__a*self.__c
    def getRaiz1(self):
        d = self.getDiscriminante()
        if d < 0:
            return 0
        return (-self.__b + math.sqrt(d)) / (2*self.__a)
    def getRaiz2(self):
        d = self.getDiscriminante()
        if d < 0:
            return 0
        return (-self.__b - math.sqrt(d)) / (2*self.__a)
for i in range(3):
    a, b, c = map(float, input("Ingrese a, b, c: ").split())
    ecuacion = Ecuaciones_Cuadraticas(a, b, c)
    d = ecuacion.getDiscriminante()
    if d > 0:
        print(f"La ecuación tiene dos raíces {ecuacion.getRaiz1():.6f} y {ecuacion.getRaiz2():.5f}")
    elif d == 0:
        print(f"La ecuación tiene una raíz {ecuacion.getRaiz1():.0f}")
    else:
        print("La ecuación no tiene raíces reales")