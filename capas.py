from bitarray import *
import pickle
import unicodedata

print("Comenzando")

mensaje = input("Ingrese un mensaje a mandar\n")
mensaje_ascii = mensaje.encode("ascii", "ignore")
print(mensaje_ascii)


a = bitarray()
a.frombytes(mensaje_ascii)
print(a)

