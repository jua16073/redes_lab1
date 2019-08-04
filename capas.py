from bitarray import *


def string_to_binary(msg):
    var = bin(int.from_bytes(msg.encode(), 'big'))[2:]
    return var


def binary_to_string(binary, encoding='utf-8', errors ='surrogatepass'):
    var2 = int(binary,2)
    return var2.to_bytes(var2.bit_length()+7 // 8, 'big').decode(encoding, errors)


def bitarray_to_binary(bitarray):
    var3 = bin(int.from_bytes(bitarray, 'big', signed=False))[2:]
    return var3


def to_bitarray(something):
    var4 = bitarray(something)
    return var4


