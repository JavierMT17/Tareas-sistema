def suma_binaria(a, b):
    a = a.zfill(8)
    b = b.zfill(8)
    resultado = ""
    acarreo = 0

    for i in range(7, -1, -1):
        bit_a = int(a[i])
        bit_b = int(b[i])
        suma = bit_a + bit_b + acarreo

        if suma == 0:
            resultado = '0' + resultado
            acarreo = 0
        elif suma == 1:
            resultado = '1' + resultado
            acarreo = 0
        elif suma == 2:
            resultado = '0' + resultado
            acarreo = 1
        else:
            resultado = '1' + resultado
            acarreo = 1

    return resultado[-8:]


def resta_binaria(a, b):
    a = a.zfill(8)
    b = b.zfill(8)
    resultado = ""
    acarreo = 0

    for i in range(7, -1, -1):
        bit_a = int(a[i])
        bit_b = int(b[i])

        resta = bit_a - bit_b - acarreo

        if resta == 0:
            resultado = '0' + resultado
            acarreo = 0
        elif resta == 1:
            resultado = '1' + resultado
            acarreo = 0
        elif resta == -1:
            resultado = '1' + resultado
            acarreo = 1
        elif resta == -2:
            resultado = '0' + resultado
            acarreo = 1

    return resultado[-8:]  # mantener 8 bits


def calculadora_binaria(operacion):
    a = input("Introduzca el primer número binario: ")
    if len(a) > 8:
        print("Error, Máximo 8 bits")
        return
    for n in a:
        if n != "1" and n != "0":
            print("Error,el número binario solo contiene  0 o 1")
            return

    b = input("Introduzca el segundo número binario: ")
    if len(b) > 8:
        print("Error, Máximo 8 bits")
        return
    for n in b:
        if n != "1" and n != "0":
            print("Error,el número binario solo contiene  0 o 1")
            return

    if operacion != "suma" and operacion != "resta" and operacion != "ambas":
        print("Error, operacion solo puedes sumar (+), restar (-) o dejarlo vacio para ambas")
        return
    if operacion == 'suma':
        print(suma_binaria(a, b))
    elif operacion == 'resta':
        print(resta_binaria(a, b))
    else:
        print("--- SUMA ---")
        print(suma_binaria(a, b))
        print("--- RESTA ---")
        print(resta_binaria(a, b))
operador = input("Introduzca una operacion(suma, resta o ambas): ")
calculadora_binaria(operador)

