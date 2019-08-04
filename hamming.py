#Using even parity

def code(msg):
  #print('hamming ', msg)
  msg_8 = []
  n_parts = []
  #dividir el mensaje en bits de 8
  temp = []
  for x in range(len(msg)):
    if x % 8 == 0 and x !=0:
      msg_8.append(temp)
      temp = []
    temp.append(msg[x])
  msg_8.append(temp)

  n_message = []
  for byte in msg_8:
    n_parts.append(redundant(byte))

  n_complete = []
  for p in n_parts:
    for b in p:
      n_complete.append(b)

  return n_complete

def redundant(part):
  n_part = [0,0,0,0,0,0,0,0,0,0,0,0]
  x = 0
  for r in range(len(n_part)):
    if r in [3,7,9,10]:
      pass
    else:
      n_part[r] = part[x]
      x+=1
  
  # (1, 3, 5, 7, 9, 11, etc).
  #  (2, 3, 6, 7, 10, 11, etc).
  # (4–7, 12–15, 20–23, etc).
  # (8–15, 24–31, 40–47, etc).
  c = [0,0,0,0]
  bits =[0,0,0,0]
  for b in range(len(part)):
    if b in [7,5,3,1]:
      if part[b]:
        c[0] += 1
    if b in [6,5,2,1]:
      if part[b]:
        c[1] += 1
    if b in [4,3,2,1]:
      if part[b]:
        c[2] += 1
    if b == 0:
      if part[b]:
        c[3] += 1

  for x in range(len(bits)):
    if c[x] % 2 ==0:
      bits[x] = 0
    else:
      bits[x] = 1
  
  n_part[10] = bits[0]
  n_part[9] = bits[1]
  n_part[7] = bits[2]
  n_part[3] = bits[3]
  return n_part


def receptor(msg):
  print("recibiendo", msg)
  #partir en 12
  msg_12 = []
  temp = []
  for b in range(len(msg)):
    if b % 12 == 0 and b !=0:
      msg_12.append(temp)
      temp = []
    temp.append(msg[b])
  #msg_11.append(temp)
  
  for part in msg_12:
    errores(part)

def errores(part):
  original = []
  redundantes = []
  for b in range(len(part)):
    if b in [3,7,9,10]:
      redundantes.append(part[b])
    else:
      original.append(part[b])
  comprobante = redundant(part)
  print('original', part)
  print('comprobante',comprobante)

  if part == comprobante:
    print("Todo nitido")
  else:
    print("malo fml")  

import random
def ruido(msg):
  rango = len(msg)
  index = random.randint(0, rango)
  msg[index] = not msg[index]    
