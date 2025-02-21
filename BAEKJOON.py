A = int(input())
B = int(input())

print(A*(B%10))
print(A*(B%100-B%10)//10) # B%100이 십의자리수로 나와서 문제임
print(A*(B//100))
print(A*B)






