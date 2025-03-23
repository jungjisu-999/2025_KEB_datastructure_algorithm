#11399 atm
#2217 로프



X = int(input()) #26000
N = int(input()) # 4
total = 0
for i in range(N):
    h,m = map(int, input().split())
    total += h*m
if total == X:
    print("Yes")
else:
    print("No")

