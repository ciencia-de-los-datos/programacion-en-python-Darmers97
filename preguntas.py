"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv, collections

def myPrint(data_structure):

    print(type(data_structure))
    if type(data_structure)==dict:
       for x in data_structure.keys():
           print(x,':',data_structure[x])    
    elif type(data_structure)==list:    
        for x in data_structure:
            print(x)
    elif type(data_structure)== int:
        print(data_structure)
    else:
        print(type(data_structure),' Type can\'t be printed')


#myPrint(data)

def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    Rta/
    214
    """
    with open('data.csv', newline='') as File:  
    reader = csv.reader(File, delimiter='\t')
    data = list(reader)
    
    counter=sum([int(x[1]) for x in data])

    return counter

#myPrint(pregunta_01())

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.
    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]
    """
    with open('data.csv', newline='') as File:  
    reader = csv.reader(File, delimiter='\t')
    data = list(reader)
    
    counter =sorted(collections.Counter([ x[0] for x in data ]).most_common(),key=lambda tup:tup[0])
    
    return counter
    
#myPrint(pregunta_02())

def sumvalues(valor,listax):

    return sum([int(x[1]) for x in listax if valor == x[0]])


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.
    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]
    """
    with open('data.csv', newline='') as File:  
    reader = csv.reader(File, delimiter='\t')
    data = list(reader)
    
    letras = sorted(set([x[0] for x in data]))
    lista =[((x,sumvalues(x,data))) for x in letras]

    return lista

#myPrint(pregunta_03())

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.
    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]
    """
    with open('data.csv', newline='') as File:  
    reader = csv.reader(File, delimiter='\t')
    data = list(reader)
    
    return sorted(collections.Counter([ x[2][5:7] for x in data ]).most_common(),key=lambda tup:tup[0])

#myPrint(pregunta_04())

def valores(letra, arraylist):

    newarray = [int(x[1]) for x in arraylist if letra == x[0]]

    return newarray

#def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.
    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]
    """
    with open('data.csv', newline='') as File:  
    reader = csv.reader(File, delimiter='\t')
    data = list(reader)
  

    letras = sorted(set([x[0] for x in data]))
    letrasmax = [((x,max(valores(x,data)),min(valores(x,data)))) for x in letras]
    
    return letrasmax

#myPrint(pregunta_05())

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.
    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]
    """
    with open('data.csv', newline='') as File:  
    reader = csv.reader(File, delimiter='\t')
    data = list(reader)

    listaclaves = []
    listadelistas = sorted([x[4] for x in data])
    listadelistas = [ x.split(',') for x in listadelistas]
    for x in listadelistas:
        for y in range (0, len(x)):
            listaclaves.append((x[y][0:3],int(x[y][4:])))

    letras = sorted(set([x[0] for x in listaclaves]))
    dicty = [((x,max(valores(x,listaclaves)),min(valores(x,listaclaves)))) for x in letras]
    return dicty

#myPrint(pregunta_06())

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.
    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]
    """
    with open('data.csv', newline='') as File:  
    reader = csv.reader(File, delimiter='\t')
    data = list(reader)
    
    numbers = sorted(set([x[1] for x in data]))
    listatuplas = []

    for x in numbers:
        listaletras = []
        for y in data:
            if x == y[1]:
                listaletras.append(y[0])
        listatuplas.append((x,listaletras))

    return listatuplas

#myPrint(pregunta_07()) 

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.
    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]
    """
    with open('data.csv', newline='') as File:  
    reader = csv.reader(File, delimiter='\t')
    data = list(reader)
    
    listadetuplas = pregunta_07()
    listadetuplas_ordenada = [(x[0],sorted(set(x[1]))) for x in listadetuplas]


    return listadetuplas_ordenada

#myPrint(pregunta_08())



def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.
    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }
    """
    with open('data.csv', newline='') as File:  
    reader = csv.reader(File, delimiter='\t')
    data = list(reader)
    
    listaclaves = []
    listadelistas = sorted([x[4] for x in data])
    listadelistas = [ x.split(',') for x in listadelistas]
    dictionary = {}

    for x in listadelistas:
        for y in x:
            if y[0:3] not in dictionary:
                dictionary[y[0:3]]=1
            else:
                dictionary[y[0:3]]+=1


    return dictionary

#myPrint(pregunta_09())

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.
    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]
    """
    with open('data.csv', newline='') as File:  
    reader = csv.reader(File, delimiter='\t')
    data = list(reader)
    
    Listatuplas = [((x[0],(len(x[3].split(','))),(len(x[4].split(','))))) for x in data]


    return Listatuplas

#myPrint(pregunta_10())

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.
    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }
    
    :
        ):
            listamerge.append()
    """
    with open('data.csv', newline='') as File:  
    reader = csv.reader(File, delimiter='\t')
    data = list(reader)
    
    listadelistas = sorted([x[3] for x in data])
    listadelistas = [ x.split(',') for x in listadelistas]
    listamerge = sorted(set([ x[y] for x in listadelistas for y in range(len(x))]))
    dicty = {}

    for x in listamerge:
        for y in data:
            if x in y[3] and x not in dicty.keys():
                dicty[x]=int(y[1])
            elif x in y[3]:
                dicty[x]+=int(y[1])


    return dicty

#myPrint(pregunta_11())

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.
    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }
    """
    with open('data.csv', newline='') as File:  
    reader = csv.reader(File, delimiter='\t')
    data = list(reader)
    
    letras = sorted(set([x[0] for x in data]))
    dicty = {}
    for x in letras:
        for y in data:
            if x == y [0] and x not in dicty.keys():
                dicty[x] = sum([ int(i[4:]) for i in y[4].split(',')])
            elif  x == y [0]:
                dicty[x] += sum([int(i[4:]) for i in y[4].split(',')])

    return dicty

#myPrint(pregunta_12())
