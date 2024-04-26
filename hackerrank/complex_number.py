'''
Polar Cordinate : https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true
'''

import cmath
complex_number = complex(input())
real_number = complex_number.real
img_number = complex_number.imag
r = abs(complex_number)
phi = cmath.phase(complex_number)
print(r)
print(phi)

