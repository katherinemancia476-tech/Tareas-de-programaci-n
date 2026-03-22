Proceso operaciones_basicas
	Definir num1, num2 como Real;
	
	Escribir "Ingrese el primer número:";
	Leer num1;
	
	Escribir "Ingrese el segundo número:";
	Leer num2;
	
	Escribir "suma: ", num1 + num2;
	Escribir "Resta: ", num1 - num2;
	Escribir "Multiplicación: ", num1 * num2;
	
	si num2 <> 0 Entonces
		Escribir "División: ", num 1 / num2;
	Sino 
		Escribir "División: No se puede dividir por cero";
	FinSi
FinProceso
