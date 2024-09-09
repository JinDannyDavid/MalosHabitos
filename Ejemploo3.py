# Función para calcular el área de un rectángulo
def arearectangulo(altura, baserectangulo):
    resultadorectangulo = altura * baserectangulo
    return resultadorectangulo

# Función para calcular el área de un triángulo
def areatriangulo(basetriangulo, alturatriangulo):
    resultadotriangulo = 0.5 * basetriangulo * alturatriangulo
    return resultadotriangulo

# Función principal
if __name__ == "__main__":
    x = float(input("Ingrese altura rectangulo: "))
    y = float(input("Ingrese base rectangulo: "))
    rect_area = arearectangulo(x, y)
    print(f"{x} * {y} = {"Área del rectángulo:"} = {rect_area}")

    u = float(input("Ingrese altura triangulo: "))
    z = float(input("Ingrese altura triangulo: "))
    tri_area = areatriangulo(u, z)
    print(f"{u} * {z} = {"Área del triangulo:"} = {tri_area}")

