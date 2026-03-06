Proceso PedirNumeros
	
    Definir num Como Entero
	
    num <- 0   // inicializamos
	
    Mientras num <= 10 Hacer
        Escribir "Pon un número del 1 al 10 (0 no vale)" 
        Leer num
		
        Si num = 0 Entonces
            Escribir "Te dije que no servía :) Ingresa otro del 1-10"
        SiNo
            Si num <= 10 Entonces
                Escribir "Número válido:", num
            SiNo
                Escribir "Número mayor a 10, no cuenta fin del programa."
            FinSi
        FinSi
		
    FinMientras
	
FinProceso