# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 22:23:53 2020

@author: SAMSUNG
"""

print(2**3) #2^3
print(5%3) #나머지
print(5//3) #몫

print(10 > 3) #True
print(3 == 3) #True
print(1 != 3) #True
print(not(1 !=3)) #False

print(abs(-5)) #-5의 절댓값, 5
print(pow(4, 2)) #4^2 = 4*4 = 16
print(max(5, 12))
print(min(5, 12))
print(round(3.14)) #반올림

from math import * #math library안에 모든것을 이용하겠다.
print(floor(4.99)) #내림
print(ceil(3.14)) #올림
print(sqrt(16)) #제곱근

from random import *

print(random()) #숫자를 난수로(무작위로) 뽑아준다. 0.0~1.0 미만의 임의의 값 생성 
print(random() * 10) #0.0~10.0미만
print(int(random() * 10)) #0~10미만
print(int(random() * 10) + 1) #1~10이하
