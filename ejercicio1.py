# Función que transforma el texto según la opción elegida
def transformar_texto(texto, opcion):
    if opcion == 1:
        return texto.upper()       # Convierte todo a mayúsculas
    elif opcion == 2:
        return texto.lower()       # Convierte todo a minúsculas
    elif opcion == 3:
        return texto.capitalize()  # Primera letra en mayúscula
    else:
        return "Opción inválida"   # Si no es 1, 2 o 3

# --- Ejemplo de uso ---
if __name__ == "__main__":
    texto = input("Ingresa un texto: ")
    print("Opciones:\n1 - Mayúsculas\n2 - Minúsculas\n3 - Primera letra mayúscula")
    opcion = int(input("Elige una opción (1, 2 o 3): "))
    
    resultado = transformar_texto(texto, opcion)
    print("Texto transformado:", resultado)
