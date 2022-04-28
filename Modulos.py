############################################################
# Modulos Propios
from Funciones import add
print(add (1,2))



############################################################
# Modulos de terceros
# https://pypi.org/
#
import colorama
print(colorama.Fore.RED + "hola rojo")

############################################################
# Modulos de Python
#
# https://docs.python.org/3/py-modindex.html

#https://docs.python.org/3/library/datetime.html
import datetime
from datetime import timedelta

print(datetime.date.today())

print(datetime.timedelta(minutes=70))# pasa a horas
print(timedelta(minutes=70))# Usa un import parcial
