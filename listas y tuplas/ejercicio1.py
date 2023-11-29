# Ejercicio 1
'''Escribir un programa que almacene las asignaturas de un curso
 (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.'''
asignaturas = ["Matematicas,", "Fisca,", "Quimica,", "Historia,", "Lengua;"]
print('Asignaturas: ',*asignaturas)
print (len(asignaturas))

# Ejercicio 2
'''Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista y la muestre por pantalla el mensaje
Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.'''
print('Yo esdudio:',*asignaturas, 'Total de asignatura es: ', len(asignaturas) )

#Ejercicio 3
'''Escribir un programa que almacene las asignaturas de un curso
 (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
pregunte al usuario la nota que ha sacado en cada asignatura,
y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura>
es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes 
notas introducidas por el usuario'''
asignaturas = []
notas=[]
asignatura = input('Ingrese la Asignatura: ')asignaturas.append(asignatura)nota = int (input('Ingrese la nota de la asignatura: '))notas.append(nota)print('En Asignatura: ',*asignaturas, 'ha sacado: ', *notas)


#Ejecicio 4
'''Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.'''
numeros = []
for numero in range(6):
    numero = int(input('Ingrese los numeros: '))
    numeros.append(numero)
numeros.sort()
print('Los numero de la loteria:',*numeros, sep=',')

#Ejercicio 5
'''Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla
 en orden inverso separados por comas.'''
numeros = []
for numero in range(1,11):  
    numeros.append(numero)
numeros.sort(reverse=True)
print(*numeros,sep=', ')

#ejercicio 6
'''Escribir un programa que almacene las asignaturas de un curso
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista 
las asignaturas aprobadas. Al final el programa
debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.'''

asignaturas = ["Matematicas,", "Fisca,", "Quimica,", "Historia,", "Lengua;"]
asignaturas_pasadas =[]
asignaturas_reprobadas = []
for asignatura in  asignaturas:
    nota = int(input('Ingresa una nota: '))
    if nota >= 5:
        asignaturas_pasadas.append(asignatura)
    else:
        asignaturas_reprobadas.append(asignatura)

print(asignaturas_reprobadas)




