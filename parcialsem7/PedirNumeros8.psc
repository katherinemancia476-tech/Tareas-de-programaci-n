Algoritmo Positivo_o_menor_a_100
	
    Definir numer Como Entero
	
    Escribir "Hola! Vamos a ver si tu número es positivo y menor que 100 :)"
	
    Repetir
        Escribir "Escribe un número cualquiera:"
        Leer numer
		
        Si numer > 0 Y numer < 100 Entonces
            Escribir "¡Perfecto! Este número cumple las condiciones:"
            Escribir Verdadero
        SiNo
            Si numer <= 0 Entonces
                Escribir "Uy, este número es negativo o cero, no sirve:"
            FinSi
			
            Si numer >= 100 Entonces
                Escribir "Aunque es positivo, es demasiado grande, no cumple:"
            FinSi
			
            Escribir Falso
        FinSi
		
    Hasta Que numer > 0 Y numer < 100
	
FinAlgoritmo