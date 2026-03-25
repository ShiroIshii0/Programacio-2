import math

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, other):
        return Vector3D(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )
    def __mul__(self, r):
        return Vector3D(
            self.x * r,
            self.y * r,
            self.z * r
        )
    def __rmul__(self, r):
        return self.__mul__(r)
    def magnitud(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    def normal(self):
        m = self.magnitud()
        if m == 0:
            return Vector3D(0,0,0)
        return Vector3D(self.x/m, self.y/m, self.z/m)
    def producto_punto(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z
    def producto_cruz(self, other):
        return Vector3D(
            self.y*other.z - self.z*other.y,
            self.z*other.x - self.x*other.z,
            self.x*other.y - self.y*other.x
        )
    def mostrar(self):
        return f"({self.x}, {self.y}, {self.z})"