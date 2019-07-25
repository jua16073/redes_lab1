import socket
from bitarray import * 

HOST = ''
PORT = 65432

mensaje = input("Ingrese un mensaje a mandar\n")
mensaje_ascii = mensaje.encode("ascii", "ignore")
print(mensaje_ascii)


a = bitarray()
a.frombytes(mensaje_ascii)
print(a)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))
  s.sendall(mensaje_ascii)
  data = s.recv(1024)

print("Received", repr(data))