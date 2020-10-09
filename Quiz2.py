# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 22:23:53 2020

@author: SAMSUNG
"""

sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고, 
파이썬은 쉬워요
"""
print(sentence3)


jumin = "990120-1234567"

print("성별: " + jumin[7])
print("연: " + jumin[0:2]) #0부터 2직전까지 (0,1)
print("월: " + jumin[2:4])
print("일: " + jumin[4:6])
print("생년월일: " + jumin[:6]) #처음부터 6직전까지
print("뒤 7자리: " + jumin[7:]) #7부터 끝까지
print("뒤 7자리 (뒤에부터): " + jumin[-7:]) #맨 뒤에서 7번째부터 끝까지

python = "Python is Amazing"
print(python.lower()) #소문자로
print(python.upper()) #대문자로
print(python[0].isupper())
print(len(python)) #길이
print(python.replace("Python", "Java")) #Python을 Java로 바꾼다.

index = python.index("n")
print(index)
index = python.index("n",index + 1)
print(index)
'''
print(python.find("Java")) #원하는 값이 없을때는 -1
print(python.index("Java")) #원하는 값이 없을때는 오류가 나고 종류됨
print(python.count("n")) #n이 총 몇번 등장하느냐
'''

#방법1
print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요" % "파이썬") # %s는 문자열
print("Apple 은 %c로 시작해요." % "A") # %c는 한 글자
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

#방법2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

#방법3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간"))

#방법4
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

print("백문이 불여일견\n백견이 불여일타") #\n줄바꿈

#저는 "나도코딩" 입니다.
print("저는 \"나도코딩\"입니다.") #\" 또는 \' : 문장 내에서 따옴표

#\\ : 문장 내에서 \
#\r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")
#\b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")    
#\t : 탭
print("Red\tApple")
    
    