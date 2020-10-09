# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 21:01:53 2020

@author: SAMSUNG
"""



class SoldOutError(Exception):
    pass
chicken = 10
waiting = 1 #홀 안에는 현재 만석, 대기번호 1부터 시작
while(True):
    try : 
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chicken:
            print("재료가 부족합니다.")
        elif order <= 0:
            raise ValueError
        else:
            print("[대기번호 {0}] {1}마리 주문이 완료되었습니다.".format(waiting, order))
            waiting += 1
            chicken -= order
            
        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break