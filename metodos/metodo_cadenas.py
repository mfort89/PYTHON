cadena1 = "hola soy mariano"
cadena2 = "bienvenido a python"

#dir ejecuta algo nos indica que metodos pueden ser usados
#print(dir(cadena1))

#combierte todo a mayusculas
mayusc = cadena1.upper()

#combierte todo a minisculas
minusc = cadena1.lower()

#combierte la primera letra a mayuscula
primera_letra_mayusc = cadena1.capitalize()

#buscamos una cadena en otra cadena, sino hay cincidencias devuelve -1
busqueda_find = cadena1.find("a")

#buscamos una cadena en otra cadena; sino hay coincidencias lasnza una exepcion
busqueda_index = cadena1.index("a")

#si es numerico devuelve true
es_numerico = cadena1.isnumeric()

#si es alfanumerico devuelve true
es_alfanumerico = cadena1.isalpha()

#buscamos una cadena en otra cadena, si hay coincidencias
contar_coincidencias = cadena1.count()

#buscamos una cadena la cantidad de caracteres
contar_caracteres = cadena1.len()

#verifica con que empieza la cadena
empieza_con = cadena1.startswith()

#verifica con que termina la cadena
termina_con = cadena1.endswith()

#remplaza un pedazo de la cadena 
cadena_nueva = cadena1.replace("la","lu")

#va a separar cadena con la cadena que le pasemos 
cadena_separada = cadena1.split(" , ")





print(cadena_nueva)