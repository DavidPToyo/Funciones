lista_numeros = [1,2,3,4,5]


def sumar_contar_tipos(lista, funcion):
   
    opcion = funcion (lista)
    
    return opcion



suma = sumar_contar_tipos(lista_numeros, sum)

print(suma)


"""def extremo_multiplicado(lista, factor):
    minimo = min(lista)
    maximo = max(lista)
    return factor*minimo, factor*maximo



print(extremo_multiplicado([1,2,3,4], 4))

print(extremo_multiplicado(factor = 4, lista = [1,2,3,4])"""

"""def elevar(base, exponente, redondear = False):
    if redondear:
        valor = round(base**exponente,2)
    else:
        valor = base**exponente
    return valor

print(elevar(2, 3))

print(elevar(2, 3, redondear = True))

def sumar_numeros(*args):
    suma = 0
    for num in args:
        suma += num
    
    return suma

print(sumar_numeros(1, 2, 3))

print(sumar_numeros(1, 2, 3, 4, 5))

print(sumar_numeros(1, 2))

print(sumar_numeros())

def crear_perfil(**kwargs):
    perfil = {}
    for key, value in kwargs.items():
        perfil[key] = value
    return perfil

perfil1 = crear_perfil(nombre='Alice', edad=25, ciudad='Barcelona')
perfil2 = crear_perfil(nombre='Bob', edad=30, ocupacion='Ingeniero')

print(perfil1)
print(perfil2)

def get_multiple(diccionario, *claves):
    pass
    return {clave: diccionario[clave] for clave in claves}

diccionario_prueba = {'manzana' : 'verde',
                      'platano': 'amarillo',
                      'frutilla': 'roja'
                      }

resultado = get_multiple(diccionario_prueba, 'platano','frutilla')
print(resultado)

#Ejercicio Loto
import random
pool = [n for n in range(1,42)]

elegido = random.choice(pool)
print("El primer numero elegido es", elegido)

pool.remove(elegido)
elegido = random.choice(pool)
print("El segundo numero elegido es", elegido)

pool.remove(elegido)
elegido = random.choice(pool)
print("El tercer numero elegido es", elegido)

pool.remove(elegido)
elegido = random.choice(pool)
print("El cuarto numero elegido es", elegido)

pool.remove(elegido)
elegido = random.choice(pool)
print("El quinto numero elegido es", elegido)

pool.remove(elegido)
elegido = random.choice(pool)
print("El sexto numero elegido es", elegido)

pool.remove(elegido)
print(pool)
elegido = random.choice(pool)
print("El Comodin numero elegido es", elegido)


def sacar_numero(posicion):
    global pool
    elegido = random.choice(pool)
    pool.remove(elegido)
    print(f"El {posicion} es {elegido}")"""

