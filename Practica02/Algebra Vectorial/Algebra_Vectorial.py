import math

class AlgebraVectorial:
    def __init__(self, a=[0,0,0], b=[0,0,0]):
        self.a = a
        self.b = b
    def producto_punto(self):
        return sum(self.a[i] * self.b[i] for i in range(3))
    def magnitud(self, v):
        return math.sqrt(sum(v[i]**2 for i in range(3)))
    def producto_cruz(self):
        a1,a2,a3 = self.a
        b1,b2,b3 = self.b
        return [
            a2*b3 - a3*b2,
            a3*b1 - a1*b3,
            a1*b2 - a2*b1
        ]
    def perpendicular(self):
        return self.producto_punto() == 0
    def paralela(self):
        cruz = self.producto_cruz()
        return cruz == [0,0,0]
    def proyeccion(self):
        escalar = self.producto_punto() / (self.magnitud(self.b)**2)
        return [escalar * x for x in self.b]
    def componente(self):
        return self.producto_punto() / self.magnitud(self.b)
v1 = [1,2,3]
v2 = [2,4,6]
obj = AlgebraVectorial(v1, v2)
print("Perpendicular:", obj.perpendicular())
print("Paralela:", obj.paralela())
print("Proyección:", obj.proyeccion())
print("Componente:", obj.componente())