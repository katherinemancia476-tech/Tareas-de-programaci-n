usuarios = ["juan", "maria", "pedro"]
contras = ["1234", "abcd", "5678"]
roles = [1, 2, 2]  # 1=Admin, 2=Usuario

# LOGIN (IF + FOR)
encontrado = False
intentos = 0

while intentos < 3 and not encontrado:
    print("\n--- LOGIN ---")
    user = input("Usuario: ")
    password = input("Contraseña: ")
    
    for i in range(len(usuarios)):
        if user == usuarios[i] and password == contras[i]:
            encontrado = True
            rolActual = roles[i]
            print("¡Login exitoso!")
            break
    
    if not encontrado:
        print("Usuario o contraseña incorrectos")
        intentos += 1

if not encontrado:
    print("Demasiados intentos. Acceso bloqueado.")
    exit()

# MENÚ (WHILE)
opcion = -1

while opcion != 0:
    print("\n--- MENÚ ---")
    print("1. Ver perfil")
    print("2. Mostrar rol")
    print("0. Salir")
    
    opcion = int(input("Seleccione opción: "))
    
    # SELECT CASE (match)
    match opcion:
        case 1:
            print(f"Usuario actual: {user}")
        
        case 2:
            match rolActual:
                case 1:
                    print("Eres ADMIN - acceso total")
                case 2:
                    print("Eres USUARIO - acceso limitado")
                case _:
                    print("Rol no válido")
        
        case 0:
            print("Saliendo del sistema...")
        
        case _:
            print("Opción incorrecta")
