# IF
x = 40
if x == 40:
    print("es 40")
else:
    print("no es 40")

# FOR
a=[1,2,3,4,5]
for numero in a:
    print(numero)
#
nums = [4, 78, 9, 84]
it = iter(nums)
print(next(it))
#
valores = {'A': 4, 'E': 3, 'I': 1, 'O': 0}
for v in valores.values():
    print(v)
#
valores = {'A': 4, 'E': 3, 'I': 1, 'O': 0}
for k, v in valores.items():
    print('k=', k, ', v=', v)
#
for i in range(11):
    print(i)    
#
for num in range(0, 11, 2): # step 2
    print(num)

#
coleccion = [2, 4, 5, 7, 8, 9, 3, 4]
for e in coleccion:
    if e == 7:
        break
    print(e)

#
coleccion = [2, 4, 5, 7, 8, 9, 3, 4]
for e in coleccion:
    if e % 2 != 0:
        continue
    print(e)