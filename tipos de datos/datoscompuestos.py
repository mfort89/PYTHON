#una agrupacion de datos
lista = ["mariano","jack","true","23"]
#la tupla no se puede modificar los datos
tupla = ("mariano","jack","true","23")
print(lista[0])

#creando un conjunto set

conjunto = {"mariano","jack","true","23"}
#podemos redefinirlo pero no podemos modificarlo cambiarlo como en el caso de la tupla
#no podemos acceder a algun valor 
#no muestra datos duplicados
#no se accede a elementos por el indice

#creando un diccionario
#la estructura es key: value y separamos todo con comas 
diccionario = {
 'nombre': "mariano",
 'profesion': "profesion",
 'esta emocionado': "true",
 'altura': "1.78",
 'dato duplicado': "mariano",   
}

print(diccionario['altura'])
