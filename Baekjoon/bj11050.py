'''
Created by sunwoong on 2022/04/05
'''
from math import factorial

n, k = map(int, input().split())
print(factorial(n) // (factorial(n - k) * factorial(k)))