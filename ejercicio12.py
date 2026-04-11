archivo = "Sunombre.txt"
sin_txt = archivo.removesuffix(".txt")
sin_prefijo = sin_txt.removeprefix("ING. ")
minuscula = sin_prefijo.lower()
lista = minuscula.split()

print(lista)
