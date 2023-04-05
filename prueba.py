while True:
    respuesta = input("Ingrese un texto: ")
    if not respuesta.isnumeric():
        print("El texto ingresado es:", respuesta)
        break
    else:
        print("Por favor, ingrese un texto que no sea solo un número.")