'''
Find Angle : https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true
'''
import math

A = float(input())
B = float(input())

c = math.sqrt(A*A + B*B) / 2
cos_value = (B / 2) / c

print(f"{round(math.degrees(math.acos(cos_value)))}\N{DEGREE SIGN}")


