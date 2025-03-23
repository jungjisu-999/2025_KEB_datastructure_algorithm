# 스네이크 버드
#n = 과일 갯수, m = 스네이크 버드 길이
n,m = map(int, input().split())

num_list = list(map(int, input().split()))
num_list.sort()

for i in num_list:
    if i <= m :
        m += 1

print(m)

