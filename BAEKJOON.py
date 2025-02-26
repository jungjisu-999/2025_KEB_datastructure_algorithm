
# T = int(input())
# A = int(input())
# B = int(input())
#
# for T in range(1,):
# print(A+B)


# result = 1
# for i in range(1,11):
#     result = result * i
# print(result)

# result = 1
# for i in range(1, 11) :
#     result *= i
# print(result)







# hap = 0 # hap이라는 변수를 지정해줘야함 !!!!!!!!
# for i in range(1,11,2):
#     hap = hap + i
# print("합 :",hap)

# 10950
# T = int(input())
# for T in range(1,T+1):
#     A,B = map(int, input().split())
#     print(A+B)

#10951
# A,B = map(int, input().split())
# print(A+B)

# A, B = map(int, input().split())
# while A < 10 and B < 10:
#         print(A + B)

#아 ㅅㅂ 진짜 어케 해야댐? 무조건 해냄 딱 대
# A, B = map(int, input().split())
# if A < 10 and B < 10:
#     while True:
#         print(A + B)

# while 의 기초 다지기
# prompt = """
#     1.Add
#     2.Del
#     3.List
#     4.Quit
#     Enter number: """
#
# number = 0
# while number != 4:
#     print(prompt)
#     number = int(input())

# coffee = 10 # 변수 지정
# money = 300  # 변수 지정
# while money: # while + 조건문
#     print("돈을 받았으니 커피를 줍니다.")
#     coffee = coffee -1
#     print("남은 커피의 양은 %d개입니다." % coffee)
#     if coffee ==0:
#         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
#         break

#coffee.py
# coffee = 10
# while True: # break가 실행될 때 까지 계속 반복, 무한 루프를 의미
#     money = int(input("돈을 넣어 주세요: "))
#     if money == 300:
#         print("커피를 줍니다.")
#         coffee = coffee -1
#     elif money > 300:
#         print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
#         coffee = coffee -1
#     else:
#         print("돈을 다시 돌려주고 커피를 주지 않습니다.")
#         print("남은 커피의 양은 %d개 입니다." % coffee)
#     if coffee ==0:
#         print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
#         break


#while문의 맨 처음으로 돌아가기 /  continue 사용
# a = 0
# while a < 10:
#     a = a + 1
#     if a % 2 == 0: continue
#     print(a)

# 무한 루프 (endless loop



    

































