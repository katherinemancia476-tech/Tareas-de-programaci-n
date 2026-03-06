Proceso SumaNumerosPositivos
	
    Definir numero Como Entero
    Definir suma Como Entero
    
    suma <- 0
    
    Repetir
        Escribir "Ingrese un número:"
        Leer numero
        
        Si numero >= 0 Entonces
            suma <- suma + numero
        FinSi
        
    Hasta Que numero < 0
    
    Escribir "La suma de los números positivos es: ", suma
	
FinProceso
