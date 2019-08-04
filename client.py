import socket
import capas as capas
import crc as receiver
import crc_sender as sender
import pickle
import random

HOST = '127.0.0.1'
PORT = 65432


def ruido(msg):
  rango = len(msg)
  index = random.randint(0, rango)
  msg[index] = not msg[index]
  return msg


def mensaje():
    mensaje1 = input("Ingrese un mensaje a mandar\n")
    mensaje1 = capas.string_to_binary(mensaje1)
    message = sender.crc(mensaje1)
    message = pickle.dumps(message)
    mensaje1 = capas.to_bitarray(mensaje1)
    mensaje1 = ruido(mensaje1)
    mensaje1 = capas.bitarray_to_binary(mensaje1)
    mensaje1 = pickle.dumps(mensaje1)
    return message, mensaje1


def recibir(data):
    recibir = pickle.loads(data)
    resultado = receiver.crc(recibir)
    return resultado


comprobacion, mensaje_enviado = mensaje()
print(mensaje_enviado)
print(comprobacion)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))
  s.sendall(mensaje_enviado)
  data = s.recv(100000000)
  resultados1 = recibir(data)
  print(resultados1)
  result = recibir(comprobacion)
  if result == resultados1:
    print('No Hay Errores')
  else:
    print('Error')
print("Received", repr(result))