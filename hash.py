import time
import hashlib
import itertools
import sys


palabra= "PEPE"
palabra_normal = palabra.encode()
hash_generado = hashlib.sha256(palabra_normal).hexdigest()
print(hash_generado)



inicio = time.time()
mayusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","Q","R","S","T","U","V","W","X","Y","Z"]
minusculas =["a","b","c","d","e", "f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","x","y","z"]
numeros = ["0","1","2","3","4","5","6","7","8","9"]
caracteres = ["!","@","#","$","%","&","/","(",")","="]

todos_los_caracteres = mayusculas + minusculas + numeros + caracteres



def fuerza_bruta(hash_objetivo, caracteres, long):
    for longitud in range(0, long + 1):
        for combo in itertools.product(caracteres, repeat=longitud):
            palabra = ''.join(combo)
            hash_palabra = hashlib.sha256(palabra.encode()).hexdigest()

            if hash_palabra == hash_objetivo:
                return palabra

    return None

resultado = fuerza_bruta(hash_generado, todos_los_caracteres, len(palabra))

if resultado:
    print("Contraseña encontrada:", resultado)
else:
    print("No se encontró")

print("Tiempo:", time.time() - inicio, "segundos")
