class Ecuacion_Lineal:
    def __init__(self, a,b, c ,d,e,f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
    def tieneS(self):
        x = self.a * self.d - self.b * self.c
        return x !=0.0
    def getX(self):
        if (self.tieneS()):
            return (self.e * self.d - self.b * self.f) / (self.a * self.d - self.b * self.c)
        else:
            return "la ecuacion no tiene solucion"
    def getY(self):
        if (self.tieneS()):
            return (self.a * self.f - self.e * self.c) / (self.a * self.d - self.b * self.c)
        else:
            return "la ecuacion no tiene solucion"
    def __str__(self):
        return "{},{},{},{}".format(self.a, self.b, self.c, self.d)
t1 =  Ecuacion_Lineal(9.0,4.0,3.0,-5.0,-6.0,-21.0)
print(t1.tieneS())
print("X = ",t1.getX())
print("y = ",t1.getY())
t2 =  Ecuacion_Lineal(1.0,2.0,2.0,4.0,4.0,5.0)
print(t1.tieneS())
print("X = ",t2.getX())
print("y = ",t2.getY())
