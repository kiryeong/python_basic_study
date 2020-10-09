# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 21:53:49 2020

@author: SAMSUNG
"""
'''
import theater_module
theater_module.price(3)
theater_module.price_morning(3) 
theater_module.price_soldier(3)
'''
'''
import theater_module as mv
mv.price(3)
mv.price_morning(3)
mv.price_soldier(3)
'''
'''
from theater_module import *
price(3)
price_morning(3)
price_soldier(3)
'''
'''
from theater_module import price, price_morning
price(5)
price_morning(5)
'''
'''
from theater_module import price_soldier as price
price(5)
'''
'''
#import travel.thailand #class나 함수는 import를 바로 할수 없다, 모듈이나 패키지만 가능
#import travel.thailand.ThailandPackage XXXX
# from import에서는 가능함
from travel.thailand import ThailandPackage

trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam

trip_to = vietnam.VietnamPackage()
trip_to.detail()
'''

from travel import *
'''
#trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()
'''
'''
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))

#pip install 은 패키지를 설치하는 것
'''
'''
#input : 사용자 입력을 받는 함수 
language = input("무슨 언어를 좋아하세요?")
print("{0}은 아주 좋은 언어입니다!".format(language))
'''

#dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
#print(dir())
'''
import random

print(dir())
import pickle

print(dir(random))
'''
'''
#glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
import glob

print(glob.glob("*.py"))
'''
'''
#os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd()) #현재 디렉토리

folder = "sample_dir"

if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)
    print(folder,"폴더를 삭제하였습니다.")
else: 
    os.makedirs(folder) #폴더생성
    print(folder, "폴더를 생성하였습니다.")
    '''
#import os
#print(os.listdir())

#time : 시간 관련 함수들을 제공하는 외장함수
#import time 
#print(time.localtime())
#print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("오늘 날짜는", datetime.date.today())

#timedelta : 두 날짜 사이의 간격
today = datetime.date.today() #오늘 날짜 저장
td = datetime.timedelta(days = 100) #100일 저장
print("우리가 만난지 100일은", today + td) #오늘부터 100일 후