# 조건문
#1330
# A, B = map(int, input().split())
# if A > B:
#     print(">")
# elif A < B:
#     print("<")
# elif A == B:
#     print("==")

# A = int(input())
# if 90<= A <=100:
#     print("A")
# elif 80<= A <= 89:
#     print("B")
# elif 70<= A <= 79:
#     print("C")
# elif 60 <= A <= 69:
#     print("D")
# else:
#     print("F")

#2753 윤년 ==> 4의 배수 and 100의 배수가 아닐때 or 400의 배수 일때
# A = int(input())
#
# if (A%4==0 and A%100 !=0) or A%400 ==0:
#     print("1")
# else:
#     print("0")

#사분면 고르기 14681
#
# x = int(input())
# y = int(input())
# if x>0 and y>0:
#     print("1")
# elif x<0 and y>0:
#     print("2")
# elif x<0 and y<0:
#     print("3")
# else:
#     print("4")

#2884 알람 시계 ==> 45분 일찍 알람 설정하기
# list(range (100)) #range의 범위를 만들고
# for i in range(100): # 변수 넣고 만들어둔 range for문에 넣기
#     print(i)


#range(start, stop, step)

# for i in range(1,31,3):
#     print(i)

# for "*" in range(1,6):
#     if "*" + 1:
#         print("*")

# for num in range(10): #1,2,3,4,5,6,7,8,9
#     print(num/10)     # 1/10
# for num in range(1,10):
#     print(3,"x",num, "=", 3*num)


i = int(input())
for i in range(1,i+1):
    print("*"*i)

# for i in range(1,10,2):
#     print(3,"x",i,"=",3*i)

# hab = 0
# for i in range(1,11):
#     hab += i
#     print(hab)



















