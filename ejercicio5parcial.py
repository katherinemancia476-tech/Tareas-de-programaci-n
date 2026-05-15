nombre_completo = input("Ingrese su nombre completo: ")

datos = nombre_completo.split()

invertido = datos[::-1]

for palabra in invertido:
    
    for letra in palabra:
        print(letra, end=".")
    
    print()