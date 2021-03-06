'''
@author : Nasrullah
@created : 25.05.2022
@github : github.com/nasdevs
'''

import numpy as np
import sympy as sy
import math
import os

def clear():
    os.system('clear')

def string_to_matrix(N, x):
    return [list(N[i:i+x]) for i in range(0, len(N), x)]

def char_to_number(N):
    return [[ord(j)-ord('a') for j in i ] for i in N]
    
def number_to_char(N):
    return [[chr(ord('a') + j) for j in i] for i in N]

def mod(N, x):
    return [[j%x for j in i] for i in N]

def encrypt(plaintext, key):
    # C = E(K, P)

    print('\n', '='*5, 'ENCRYPT', '='*5)
    K = string_to_matrix(key, int(math.sqrt(len(key))))
    print(f'\nKey : \n{np.matrix(K)}')
    K = char_to_number(K)
    print(f'\nKey to number : \n{np.matrix(K)}')

    P = string_to_matrix(plaintext, int(math.sqrt(len(key))))
    print(f'\nPlaintext : \n{np.matrix(P)}')
    P = char_to_number(P)
    print(f'\nPlaintext to number : \n{np.matrix(P)}')

    C = np.dot(P, K)
    print(f'\nAfter C = P x K : \n{np.matrix(C)}')
    C = mod(C, 26)
    print(f'\nAfter C mod 26 : \n{np.matrix(C)}')

    C = number_to_char(C)
    print(f'\nMatrix encrypt result : \n{np.matrix(C)}')

    return ''.join(''.join(C[i]) for i in range(len(C)))

def decrypt(cipher, key):
    # P = D(K, C)

    print('\n', '='*5, 'DECRYPT', '='*5)
    K = string_to_matrix(key, int(math.sqrt(len(key))))
    print(f'\nKey : \n{np.matrix(K)}')
    K = char_to_number(K)
    print(f'\nKey to number : \n{np.matrix(K)}')
    
    C = string_to_matrix(cipher, int(math.sqrt(len(key))))
    print(f'\nCiphertext : \n{np.matrix(C)}')
    C = char_to_number(C)
    print(f'\nCiphertext to number : \n{np.matrix(C)}')

    det_K = int(np.linalg.det(K))
    print('\nDeterminant of key : ', det_K)
    det_K = int(np.linalg.det(K) % 26)
    print('After Det K mod 26 : ', det_K)
    for i in range(1, 26):
        if (det_K * i) % 26 == 1:
            det_K = i
            break
    print('\nModular multiplicative inverse : ', det_K)

    invers_K = sy.Matrix(K).adjugate()
    print(f'\nInvers of Key : \n{np.matrix(invers_K)}')
    K = np.multiply(det_K, invers_K)
    print('\nAfter Modular . Invers K : \n', K)
    K = mod(K, 26)
    print(f'\nAfter key mod 26 : \n{np.matrix(K)}')

    P = np.dot(C, K)
    print(f'\nAfter P = C x K : \n{np.matrix(P)}')
    P = mod(P, 26)
    print(f'\nAfter P mod 26 : \n{np.matrix(P)}')
    P = number_to_char(P)
    print(f'\nMatrix decrypt result : \n{np.matrix(P)}')

    return ''.join(''.join(P[i]) for i in range(len(P)))

if __name__ == '__main__':
    clear()

    while True:
        key = str(input('input key : '))
        if math.sqrt(len(key)) not in range(1, 101):
            print(f'number of letters has no integer root, current number of letters {len(key)} and resulting root {round(math.sqrt(len(key)), 5)}')
        else:
            break

    while True:
        plaintext = str(input('input plaintext : '))
        if len(plaintext) % int(math.sqrt(len(key))) != 0:
            print(f'number of letters must be a multiple of {int(math.sqrt(len(key)))}, the current number of letters is {len(plaintext)}. You are excess {len(plaintext) % int(math.sqrt(len(key)))} letters')
        else:
            break

    clear()

    print(f'''
Plaintext : {plaintext.lower()}
Key       : {key.lower()}
''')

    cipher_result  = encrypt(plaintext.lower(), key.lower())
    print('\ncipher result :', cipher_result)

    plaintext_result = decrypt(cipher_result, key.lower())
    print('\nplaintext result = ', plaintext_result)

    print(f'''
================= RESULT =================
Plaintext        : {plaintext.lower()}
Key              : {key.lower()}
Cipher result    : {cipher_result}
Plaintext result : {plaintext_result}
''')
