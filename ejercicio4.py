texto = "CANTANDO"
minuscula = texto.lower()
sin_sufijo = minuscula.removesuffix("ando")
indice = sin_sufijo.find("t")

print(sin_sufijo)
print(indice)
