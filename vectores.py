# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 17:53:11 2021

@author: PedroLuis
"""

# Ejercicio 1
i = 1
j = 1
pro = 0
tama = 0
numeros = []
while True:
    num = int(input(f'Digite el número {i} o ingrese 0 para finalizar: '))
    if num == 0: break
    numeros.append(num)
    i += 1

suma = sum(numeros)

for j in range(len(numeros)):
    pro *= numeros[j]
    j += 1

numeros_ord = list(set(numeros))
menor = numeros_ord[1]
mayor = numeros_ord[tama]

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
for numero in numeros:
    if numero % 2 == 0:
        cont_pares += 1
    else:
        cont_impar += 1
print(f'La cantidad de números pares ingresador fue: {cont_pares}')
print(f'La cantidad de números impares ingresador fueron: {cont_impar}')
# Falta el calculo de primo


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

for k in range(1, len(vec_uno) + 1):
    vec_suma[k] = vec_uno[k] + vec_dos[k]
    vec_resta[k] = vec_uno[k] - vec_dos[k]

print('Vector Suma')
print(vec_suma)
print('Vector resta')
print(vec_resta)


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

vec_uno = numeros[:int(len(numeros) / 2)]
vec_dos = numeros[int(len(numeros) / 2):]

suma = sum(vec_uno)
# pro = produc

print(f'La primera mitad es: {vec_uno} ')
print(f'La segunda mitad es: {vec_dos} ')
print(f'La sumatoria de la primera parte es: {suma} ')


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
    print(f'El vector es simetrico: {numeros} ')
else:
    print(f'El vector no es simetrico: {numeros} ')


# Ejercicio 7
i = 1
j = 1
vec_uno = []
vec_dos = []
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

numeros_ord_uno = list(set(vec_uno))
numeros_ord_dos = list(set(vec_dos))
union = numeros_ord_uno + numeros_ord_dos


print(f'La union de los dos vectores sin repetir es: {union} ')
