temperaturas = []

for i in range(5):
    dato = int(input("Ingrese una temperatura: "))
    temperaturas.append(dato)

for temp in temperaturas:
    match temp:
        case 0:
            print("Alerta: Punto de Congelación")

        case 100:
            print("Alerta: Punto de Ebullición")

        case _:
            estado = "Estado: Estable" if 10 <= temp <= 30 else "Estado: Crítico"
            print(estado)