# Esto es un comentario

# Se pueden usar comillas simples y dobles
print ("Hola Mundo")
print ('Hola Mundo')
print("a"+"b")

#Obtener el tipo de dato
a=None
a=10
print(type(a))#INT 
a=10.5
print(type(a))#Float
a="pepe"
print(type(a))#str

#Tuples
a=(1,2,3)
print(type(a))#tuple
print(a[0]+a[1]+a[2])

#Lists
a=[0,2,3]
print(a[0])
a=list(range(1,100))
print(a)
#Dictionaries Dict
{"nombre" : "pepe",
"apellido" : "pepo",
"Apodo" : "nick"
}

#Convenciones de Definicion de Variables
book_name = "xx" #Snake Case
bookName = "xx" #Camel Case
BookName ="xx" #Pascal Case
PI = 3.14 #Convencion para constantes

# Clausula dir
print(dir(bookName)) #Con esta sentencia listo los metodos que puedo utilizar con la variable
#['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', 
#'__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', 
#'__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', 
#'__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', 
#'__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 
#'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 
#'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 
#'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 
#'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 
#'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 
#'upper', 'zfill']
print(bookName.upper())
print(bookName.capitalize())
print(bookName.replace("x","y"))
print(bookName.count("x"))

# Comentar bloque Ctrl+k Ctrl+c
# DesComentar bloque Ctrl+k Ctrl+u

#Pedir datos por Pantalla
#Edad = input("Ingrese su edad: ")
#NuevaEdad = int(Edad) + 5
#print(NuevaEdad)

