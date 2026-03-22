Proceso division_dos_numeros
		Definir num1, num2 como Real;
		Definir resultado Como Real
		
		Escribir "ingrese el primer número:";
		leer num1;
		
		Escribir "ingrese el segundo número:";
		leer num2;
		
		si num2 <> 0 Entonces
			resultado = num1 / num2;
			Escribir "La división es: ", resultado; 
		SiNo
			Escribir "error: no se puede dividir por cero.";
		FinSi
FinProceso

