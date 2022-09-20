#RSA Toy Implementation

import random

# 1 generate p & q given bit-size. (2048 & 4096 is recommended)
p, q = random.getrandbits(1024), random.getrandbits(1024)

print(p, '\n', q)

'''
# Generate n from p * q 
n = p*q
print('\n\n', n)

# Phi(n) = (p - 1)(q - 1)

# 
print('\n\n', p-1)

'''
