import random

def xor_cipher(texto):
    clave = [random.randint(0, 1) for _ in texto]

    cifrado = ""
    for i in range(len(texto)):
        cifrado += chr(ord(texto[i]) ^ clave[i])


    descifrado = ""
    for i in range(len(cifrado)):
        descifrado += chr(ord(cifrado[i]) ^ clave[i])

    return clave, cifrado, descifrado

texto = input("Ingrese un texto: ")

clave, cifrado, descifrado = xor_cipher(texto)

print("Clave generada:", clave)
print("Texto cifrado:", cifrado.encode())  
print("Texto descifrado:", descifrado)
