# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 17:53:11 2021

@author: PedroLuis
"""

# Ejercicio 1
i = 1
pro = 1
tama = 0
numeros = []
while True:
    num = int(input(f'Digite el número {i} o ingrese 0 para finalizar: '))
    if num == 0: break
    numeros.append(num)
    i += 1

suma = sum(numeros)

numeros_ord = list(set(numeros))
orde = sorted(numeros)
menor = orde[0]

for j in range(1, len(numeros)+1):
    pro *= numeros[j-1]

numeros_ord.sort(reverse=True)
mayor = numeros_ord[0]

print(f'Los números ingresados fueron: {numeros}')
print(f'El valor la sumatoria es : {suma} ')
print(f'El valor la prouctorio es : {pro} ')
print(f'El menor elemento es : {menor} ')
print(f'El mayor elemento es : {mayor} ')


# Ejercicio 2
i = 1
numeros = []
while True:
    num = int(input(f'Digite el número {i} o ingrese 0 para finalizar: '))
    if num == 0: break
    numeros.append(num)
    i += 1
print(f'Los números ingresados fueron: {numeros}')

# Recorridos de los vectores
cont_pares = 0
cont_impar = 0
cnp = 0
cont_primo = 0
for numero in numeros:
    if numero % 2 == 0:
        cont_pares += 1
    else:
        cont_impar += 1
    if numero == 2:
        cont_primo += 1

for n in range(2, len(numeros)):
    if numeros[n] % n == 0:
        cnp += 1
    else:
        cont_primo += 1

print(f'La cantidad de números pares ingresador fueron: {cont_pares}')
print(f'La cantidad de números impares ingresador fueron: {cont_impar}')
print(f'La cantidad de números primos ingresador fueron: {cont_primo}')

# Ejercicio 3
i = 1
j = 1
vec_uno = []
vec_dos = []
vec_suma = []
vec_resta = []
while True:
    num_uno = int(input(f'Digite el dato {i} del vector uno o digite Cero 0:'))
    if num_uno == 0: break
    vec_uno.append(num_uno)
    i += 1

while True:
    num_dos = int(input(f'Digite el dato {j} del vector dos o digite Cero 0:'))
    if num_dos == 0: break
    vec_dos.append(num_dos)
    j += 1

print(f'Los números ingresados en el vector uno fueron: {vec_uno}')
print(f'Los números ingresados en el vector dos fueron: {vec_dos}')

for k in range(0, len(vec_uno)):
    vec_suma = vec_uno[k] + vec_dos[k]
    print(f'la suma de los vectores en la posición {k} es: {vec_suma} ')

    vec_resta = vec_uno[k] - vec_dos[k]
    print(f'la resta de los vectores en la posición {k} es: {vec_resta} ')


# Ejercicio 4
i = 1
numeros = []
while True:
    num = int(input(f'Digite el número {i} o ingrese 0 para finalizar: '))
    if num == 0: break
    numeros.append(num)
    i += 1
print(f'Los números ingresados fueron: {numeros}')

from statistics import mode
print('El número que mas se repite es: ')
print(mode(numeros))


# Ejercicio 5
i = 1
pro = 1
numeros = []
v_uno = []
v_dos = []
print('Debes ingresar la cantidad de datos del vector que sean pares')
while True:
    num = int(input(f'Digite el número {i} o ingrese 0 para finalizar: '))
    if num == 0: break
    numeros.append(num)
    i += 1
print(f'Los números ingresados fueron: {numeros}')

vec_dos = numeros[:int(len(numeros) / 2)]
vec_uno = numeros[int(len(numeros) / 2):]

suma = sum(vec_uno)

for j in range(1, len(vec_dos)+1):
    pro *= vec_dos[j-1]

print(f'La primera mitad es: {vec_dos} ')
print(f'La segunda mitad es: {vec_uno} ')
print(f'La productoria de la primera parte es: {pro} ')
print(f'La sumatoria de la segunda parte es: {suma} ')


# Ejercicio 6
i = 1
numeros = []
v_uno = []
v_dos = []
while True:
    num = int(input(f'Digite el número {i} o ingrese 0 para finalizar: '))
    if num == 0: break
    numeros.append(num)
    i += 1
print(f'Los números ingresados fueron: {numeros}')

vec_uno = numeros[:int(len(numeros) / 2)]
vec_dos = numeros[int(len(numeros) / 2):]

if len(vec_uno) == len(vec_dos):
    print('El vector es simetrico')
else:
    print('El vector no es simetrico ')


# Ejercicio 7
i = 1
j = 1
vec_uno = []
vec_dos = []
inter = []
while True:
    num_uno = int(input(f'Digite el dato {i} del vector uno o digite Cero 0:'))
    if num_uno == 0: break
    vec_uno.append(num_uno)
    i += 1

while True:
    num_dos = int(input(f'Digite el dato {j} del vector dos o digite Cero 0:'))
    if num_dos == 0: break
    vec_dos.append(num_dos)
    j += 1

union = set(vec_uno) | set(vec_dos)
inter = set(vec_uno) & set(vec_dos)
a_b = set(vec_uno) - set(vec_dos)
b_a = set(vec_dos) - set(vec_uno)


print(f'La union de los dos vectores ordenado y sin repetir es: {union} ')
print(f'La interseción de los dos vectores es: {inter} ')
print(f'Pertenecen a Vector 1 y no estan en Vector 2: {a_b} ')
print(f'Pertenecen a Vector 2 y no estan en Vector 1: {b_a} ')
