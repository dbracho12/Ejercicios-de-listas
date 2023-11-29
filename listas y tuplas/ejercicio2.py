#Ejercicio 7
'''Escribir un programa que almacene el abecedario en una lista, 
elimine de la lista las letras que ocupen posiciones múltiplos de 3, 
y muestre por pantalla la lista resultante.'''
abcdarios = ['a','b','c',
            'd', 'e', 'f',
            'g', 'h', 'i', 
            'j', 'k', 'l', 
            'm', 'n', 'ñ', 
            'o', 'p', 'r',
            't', 'u', 'v',
            'w', 'x', 'y', 
            'z']
for abcdario in range(len(abcdarios),0, -1):
       if abcdario % 3 ==0:
           abcdarios.pop(abcdario-1)
print(abcdarios)



#Ejercicio 8
'''Escribir un programa que pida al usuario una palabra
 y muestre por pantalla si es un palíndromo.'''

palabra = input('Ingrese la palabra: ')
palabra_invertida = palabra[::-1]

lista_palabra = []

for i in palabra_invertida:
        lista_palabra.append(i)
       
if palabra == palabra_invertida and len(palabra) == len(palabra_invertida):      
    print(f'la palabra {''.join(lista_palabra)} es palindrimo')
else:
    print(f'la palabra {''.join(reversed(lista_palabra))} No es palindrimo')

#Ejercicio 9
'''Escribir un programa que pida al usuario una palabra y muestre por pantalla 
el número de veces que contiene cada vocal.'''
palabra= input('Ingrese una palabra: ')
#len(vocal_repetida)
vocal_a = []
vocal_e = []
vocal_i = []
vocal_o = []
vocal_u = []
for i in palabra:
    if i == 'a':
        vocal_a.append(i)
    elif i == 'e':
        vocal_e.append(i)
    elif i == 'i':
        vocal_i.append(i)
    elif i == 'o':
        vocal_o.append(i)
    elif i == 'u':
        vocal_u.append(i)

print(f'a = {len(vocal_a)}')
print(f'e = {len(vocal_e)}')
print(f'i = {len(vocal_i)}')
print(f'o = {len(vocal_o)}')
print(f'u = {len(vocal_u)}')
