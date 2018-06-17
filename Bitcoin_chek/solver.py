#!/usr/bin/python

def xor_str(x, y):
    if len(x) > len(y):
        return ''.join([chr(ord(z) ^ ord(p)) for (z, p) in zip(x[:len(y)], y)])
    else:
        return ''.join([chr(ord(z) ^ ord(p)) for (z, p) in zip(x, y[:len(x)])])

KEY = 'musZTXmxV58UdwiKt8Tp'
file = open('BTC', 'rb').read()

key = KEY.encode()

enc = xor_str(key * (len(file) // len(key) + 1), file).encode('hex')

ef = open('solve', 'wb')
ef.write(enc.decode('hex'))
ef.close()


