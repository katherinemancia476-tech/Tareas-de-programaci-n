# las comillas triples son las que se encargan de hacer
# Cadenas de texto largas sin mdoficar el formato.
# texto corto

cancion = (
    "Cómo estás"
    "Hace tiempo que no hablamos"
    "Tú y yo curando heridas"
    "Qué ironía, he sido yo"
    "Quien la tuya ha desgarrado"
    "Me acuerdo"
    "Conduciendo y tú a mi lado"
    "Gritando por volverte a ver"
    "y ahora evitamos mirarnos"
    "Aunque se veía perfecto"
    "En cada historia hay un final"
    "El cuento de hadas que contamos dejó de ser ideal"
    "Fuiste la suerte que no supe cuidar"
    "Y si necesitas odiarme"
    "Si ya no puedes hablarme"
    "Sigue tu camino que alguien"
    "Volverá a hacerte sentir que arde"
)


# textos largos ''' o """
cancion1= """ Cómo estás?
    Hace tiempo que no hablamos
    Tú y yo curando heridas
    Qué ironía, he sido yo
    Quien la tuya ha desgarrado
    Me acuerdo
    Conduciendo y tú a mi lado
    Gritando por volverte a ver
    y ahora evitamos mirarnos
    Aunque se veía perfecto
    En cada historia hay un final
    El cuento de hadas que contamos dejó de ser ideal
    Fuiste la suerte que no supe cuidar
    Y si necesitas odiarme
    Si ya no puedes hablarme
    Sigue tu camino que alguien
    Volverá a hacerte sentir que arde"""


## computadora -> que variable queres imprimir
## print()
# void -> no devuelve nada
# odjeto -> devuelve un tipo de dato

## realizar una wiki tambien puede darle doble clic al documentoy se les
## despliega el editor de texto 

## MAYUSCULAS
## multabilidad -> siempre debemos evitar transformar objeto original
## clases -> estereotipos (como molde)
## propiedades ->
## color
## tipo de motor (electricos o de gas)
## ojos
## color de pelo

##funciones -> string (cadenas de texto) es un objeto
## moverse
## frenar
## cargarse
## descargarse

# cancion es un espacio de memoria para string
# se va a llenar con el contenido de poema alterar con la acción Upper (mayusculas)
cancion_Mayusculas = cancion.upper()
print(cancion_Mayusculas)

## convertir en minusculas 
## string .lower
cancion_minusculas = cancion.lower()
print(cancion_minusculas)

## tiene que ingresar 100 nombres en mayuscula
mensaje = "hOlA kACe progRMando o qUe HaCe"
## Capitalize a que la primera letra de cada palabra sea mayuscula
mensajeCorrecto = mensaje.capitalize()
print(mensajeCorrecto)

## Las flipantess aventuras de el gato con bolson magico y alfredo
titulo = "Las flipantess aventuras de el gato con bolson magico y alfredo"
tituloCorrecto = titulo.title()
# print(tituloCorrecto)

## swapCase() permite cambiar entre mayusculas y minusculas
swapCaseTitulo = tituloCorrecto.swapcase()
print(swapCaseTitulo)

numero = "512"
solo_letras = "El chico del apartamentos "
Coro = "piribiribanban"

quieroSoloLetras = numero.isalpha()
print(quieroSoloLetras)
