# Challenge 2 developed in python


def perimetro(area):
    iteration = 1
    while iteration * iteration <= area:
        if area % iteration == 0:
            calc = int(area / iteration)
            perimetro = int(2 * (calc + iteration))
        iteration = iteration + 1
    return print("Resultado: ", perimetro)


try:
    area = int(input("Area: "))
    perimetro(area)
except Exception as e:
    print("Error de argumentos: ", e)