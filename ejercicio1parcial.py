etiqueta = input("Ingrese la etiqueta de rastreo: ")

if etiqueta == "" or etiqueta is None :
    print("Error, la etiqueta esá vacía.")
else:
    inicio = etiqueta.find ("-") + 1
    fin = etiqueta.rfind("-")
    categoría = etiqueta[inicio:fin]

    print(f"categoría del paquete: {categoría}")

    ruta = "Ruta Local" if etiqueta.endswith("SV") else "Ruta Internacioal"

    print(ruta)
    
