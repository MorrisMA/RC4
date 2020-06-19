'''
    Implementation of RC4 Stream Cypher
'''

def KSA(key):
    i = j = 0
    keyLen = len(key)

    S = list(i for i in range(256))

    for i in range(256):
       j = (j + key[i % keyLen] + S[i]) % 256
       S[i], S[j] = S[j], S[i]

    return S

def PRGA(S):
    i = 0; j = 0
    while(True):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        yield S[(S[i] + S[j]) % 256]

def RC4(key):
    return PRGA(KSA(key))

if __name__ == '__main__':

    key = bytes("AlphaBetaTechnologies3325TrianaBlvdHuntsvilleAL35805", 'utf-8')

    keystream = RC4(key)
    
    keys = list(next(keystream) for k in range(16))

    for k in range(len(keys)):
        print('%02x ' % keys[k], end='')
    print()
