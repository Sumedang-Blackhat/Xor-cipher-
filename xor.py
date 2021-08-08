#Sekedar Singgah

from itertools import cycle

def repeated_xor(string, key):
    result = ""
    for c, k in zip(string, cycle(key)):
        result += chr(ord(c) ^ ord(k))
    return result

a = raw_input('masukan file: ')
f = open(a,'r').read()

c = repeated_xor(a, "anjay")

d = a.replace('.txt','._txt')
k = open(d,'w')
k.write(c)
k.close()