Proceso SumaHastaDivisibleEntre5
	
    // Declaración de variables
    Definir numeroIngresado Como Entero
    Definir totalAcumulado Como Entero
    Definir promedio Como Real
    Definir continuar Como Logico
    Definir contador Como Entero
    
    // Inicialización
    totalAcumulado <- 0
    contador <- 0
    continuar <- Verdadero
    
    // Ciclo Hacer-Mientras
    Repetir
        
        Escribir "Ingrese un numero entero:"
        Leer numeroIngresado
        
        // Operaciones matemáticas
        totalAcumulado <- totalAcumulado + numeroIngresado
        contador <- contador + 1
        
        // Ejemplo de resta
        totalAcumulado <- totalAcumulado - 0
        
        // Operador lógico con NO
        Si NO (numeroIngresado = 0) Entonces
            Escribir "Numero diferente de cero ingresado."
        FinSi
        
        // Uso de operador lógico Y
        Si (totalAcumulado > 0) Y (contador > 0) Entonces
            promedio <- totalAcumulado / contador
        FinSi
        
        // Condición lógica con O
        continuar <- NO (totalAcumulado MOD 5 = 0) O (contador = 0)
        
        Escribir "Total acumulado: ", totalAcumulado
        Escribir "Cantidad de numeros ingresados: ", contador
        
    Hasta Que continuar = Falso
    
    Escribir "El total es divisible entre 5."
    Escribir "Promedio final: ", promedio
	
FinProceso