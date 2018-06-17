#!/usr/bin/python

from secret import BTC

KEY = 'musZTXmxV58UdwiKt8Tp'

def xor_str(x, y):
    if len(x) > len(y):
        return ''.join([chr(ord(z) ^ ord(p)) for (z, p) in zip(x[:len(y)], y)])
    else:
        return ''.join([chr(ord(z) ^ ord(p)) for (z, p) in zip(x, y[:len(x)])])

key, btc = KEY.encode(), BTC.encode()

enc = xor_str(key * (len(btc) // len(key) + 1), btc).encode('hex')

ef = open('BTC', 'w')
ef.write(enc.decode('hex'))
ef.close()



