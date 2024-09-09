def calcular(numero1, numero2, numero3):
    resultado = numero1 * numero2 + numero3
    return resultado

if __name__ == "__main__":
    x = float(input("Ingrese numero 1: "))
    y = float(input("Ingrese numero 2: "))
    z = float(input("Ingrese numero 3: "))
    resultado = calcular(x, y, z)
    print(f"{x} * {y} + {z} = {"El resultado es:"} = {resultado}")


