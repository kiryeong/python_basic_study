# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 13:11:28 2020

@author: SAMSUNG
"""
'''
print("Python", "Java", sep = " , ", end="?")
print("무엇이 더 재밌을까요?")
'''
'''
import sys
print("Python", "Java", file=sys.stdout) #표준출력으로 처리
print("Python", "Java", file=sys.stderr) #표준에러로 처리
'''
'''
#시험 성적
scores = {"수학":0, "영어":50, "코딩":100} #dictionary 형태이르모 key와 value
for subject, score in scores.items(): #scores.items() 하면 key와 value의 값들이 모두 출력
    print(subject.ljust(8),str(score).rjust(4), sep=":")
    
#ljust, rjust는 왼쪽정렬, 오른쪽정렬

#은행 대기순번표
#001, 002, 003 ...
for num in range(1,21):
    print("대기번호 : " + str(num).zfill(3))
    
answer = input("아무 값이나 입력하세요 : ")
print(type(answer))
print("입력하신 값은" + answer + "입니다.")
#사용자 입력을 통해 입력을 받으면 항상 문자열 형태로 저장이 된다. 

#다양한 출력포맷
# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
# 왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:_<10}".format(500))
# 3자리마다 콤마를 찍어주기
print("{0:,}".format(10000000000))
# 3자리마다 콤마를 찍어주기, +-부호도 붙이기
print("{0:+,}".format(10000000000))
print("{0:+,}".format(-10000000000))
#3자리마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
#돈이 많으면 행복하니까 빈 자리는 ^로 채워주기
print("{0:^<+30,}".format(100000000000000))
#소수점 출력
print("{0:f}".format(5/3))
#소수점 특정 자리수까지만 표시(소수점 3째 자리에서 반올림)
print("{0:.2f}".format(5/3))


#파일입출력
score_file = open("score.txt", "w", encoding="utf8") #파일을 쓰기목적으로 연다. utf8선언을 안해주면 한글이 이상하게 나올수도 있다.
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8") #이미 있는 파일에다가 위에다가 더 쓰고 싶을때 append
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read()) #한번에 불러오기
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
print(score_file.readline()) #줄별로 읽기, 한줄 읽고 커서는 다음줄로 이동
score_file.close()


#파일이 총 몇줄인지 모를때

score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() #list형태로 저장
for line in lines:
    print(line, end="")
    
score_file.close()
'''
'''
#pickle (프로그램상에서 우리가 사용하고 있는 데이터를 파일 형태로 저장하는 것)
import pickle
profile_file = open("profile.pickle", "wb") #pickle은 encoding 할 필요 없음
profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
print(profile)
pickle.dump(profile,profile_file) #profile에 있는 정보를 file에 저장
profile_file.close

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()
'''
'''
import pickle
with open("profile.pickle","rb") as profile_files:
    print(pickle.load(profile_files))


with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")
    
with open("study.txt","r",encoding = "utf8") as study_files:
    print(study_files.read())

#with를 사용하면 매번 close를 해줄 필요가 없음
'''

for i in range(1, 51):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 - ".format(i))
        report_file.write("\n부서 : ")
        report_file.write("\n이름 : ")
        report_file.write("\n업무요약 : ")
        

