## si la cadena de texto tiene numeros
siTieneNumero = "Kath 2026"
## este texto tiene numero -> True
## isnumeric -> es un espacio en la memoria
## isnumeric () -> dentro de la función
respuesta = siTieneNumero.isnumeric()
print(respuesta)

## isnumeric como numeros que van a estar ejecutándose desde una
## cadena de texto 

isLowerCase1 = "El también se fue, me abandonó y destrozó mi corazón"
minusculas = isLowerCase1.isLowerCase1()
## islowerCase() 
## isLowerCase.isLower.Case()
## true o false
print("solo minusculas", minusculas)

## 3 minutos
def solo_mayusculas (texto):
    return texto.isupper()
palabra = "HOLA"
if solo_mayusculas (palabra):
    print("Tiene solo mayúsculas")
else:
    print("No tiene solo mayúsculas")

## solo se debe de tener mayúsculas
fraseIconica = "soltala Ericka"
respuesta = fraseIconica.isupper()
print(respuesta)

## tener un contenido -> entrada a la función que inicie con el.

respuesta = fraseIconica.upper()
## esta función la vamos a encadenar con la otra >:)
print(respuesta)

respuesta = fraseIconica.title().istitle()
print(fraseIconica, respuesta)
## cuando una funcion retorna algo (tipo de datos)
## string -> espacio de memoria diferentes al de un numerico
## int
## loat
## decimal
## boolean

## string -> K A T H A -> lista o un array
## variable : 
## tiene un tipo
## nombre sea único -> indice
## no puede iniciar con variables
## va a tomar siempre el valor de la última modificación

print(fraseIconica)
fraseIconica = "soltala mama"
print(fraseIconica)
controlarEspacio = fraseIconica.isspace()
print(controlarEspacio)
## islower minusculas
## isupper
## isspace espacio
## isalnum para verificar si hay numero
## isalpha sin contiene numeros y letras

## metodos de búsqueda
temazo = " En el bosque de la china la chinita se perdió " 
## E n e l b o s q u e  d  e  c  h  i  n  a  l  a  c  h  i  n  i  t  a  s  e  p  e  r  d  i  ó
## 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 
## siempre parte desde el 0 al último numero 
## si indicamos algo que no esta en el string nos va indicar el -1
temazof = temazo.find("se")
print (temazof)

## desde la derecha vamos a tomar lo siguiente rfind()
temazof = temazo.upper().find("BOSQUE")

print(temazo)

poema = """ Ella amará a otro hombre.
Yo voy lejos, andando hacia el olvido.
Y puede suceder que alguien me nombre,
pero ella fingirá no haber oído.

Ella amará a otro hombre:
el tiempo pasa y el amor finaliza,
y es natural que lo que fue una brasa
acabe convirtiéndose en ceniza."""
contador = poema.count("i")
contador = poema.startswith("Ella")
contador = poema.endswith("ceniza")
print(contador)

poemaModificado = poema.replace("Ella" "Lupita")
print(poemaModificado)



