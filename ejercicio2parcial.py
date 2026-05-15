from decimal import Decimal

total = Decimal ("0") 

while True:
    try:
        precio = Decimal (input("Ingrese el precio del producto (0 para salir): "))

        if precio == 0:
            break

        total += precio

    except ValueError:
        print("Entrada no válida. Debe ingresar un número.")
    except:
        print("(Error e el dato ingresado.")

print(f"Total acumulado: ${total}")

