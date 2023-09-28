
diccionario = {"Perro":5, 
               "gato":7,
               "pez": 23,}

y = 0
for i in diccionario:
    if diccionario[i] > y:
        name = i
        y = diccionario[i]
print(y) 
print(name)
     