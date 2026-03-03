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
#Ventajas de utilizar la Programación Orientada a Objetos (P.O.O.):

#Modularidad:
#La programación orientada a objetos permite organizar el código en módulos llamados clases. Cada clase es responsable de una parte del sistema. En este caso, la clase Estadistica encapsula las funcionalidades relacionadas con los cálculos del promedio y la desviación estándar.

#Reutilización del código:

#Una vez definida la clase Estadistica, puedes reutilizarla múltiples veces sin necesidad de reescribir código. Puedes crear instancias de la clase para diferentes conjuntos de datos y obtener los resultados sin alterar la estructura básica.

#Encapsulamiento:

#La P.O.O. permite ocultar la implementación interna (como los cálculos del promedio y la desviación estándar) y proporciona métodos públicos para interactuar con los datos. Esto significa que el usuario no necesita saber cómo se calcula el promedio o la desviación estándar, solo tiene que usar los métodos proporcionados.

#Facilita la extensión del código:

#Si en el futuro se necesitan nuevas funcionalidades, como agregar más métricas estadísticas (mediana, moda, etc.), se puede agregar fácilmente sin alterar el código existente. Solo tienes que agregar un nuevo método a la clase Estadistica.

#Mantenimiento:

#La P.O.O. facilita el mantenimiento del código. Si se encuentra un error en un método, solo necesitas modificar esa parte de la clase sin afectar al resto del programa.

#Abstracción:

#La programación orientada a objetos permite abstraer detalles complejos de la implementación. El usuario solo interactúa con la clase a través de sus métodos públicos, sin necesidad de conocer los detalles internos del cálculo.

#Conclusión:

#Programación Modular: Es más sencilla para problemas pequeños, pero puede volverse más difícil de mantener y ampliar a medida que el sistema crece.

#Programación Orientada a Objetos: Ofrece mayor organización, modularidad y flexibilidad para proyectos más grandes, haciendo que el código sea más fácil de mantener y extender.