'''
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
B = []
C = []
sum = 0

for i in range(len(A)):
    sum += A[i]

avr = sum//len(A)
print("평균:" , avr)
()
for i in range(len(A)):
    if A[i]<avr:
        B.append(A[i])
    elif A[i]>avr:
        C.append(A[i])
    else:
        print("평균과 같은 점수")

print("<평균보다 낮은 점수>")
for i in range(len(B)):
    print(B[i])

print("<평균보다 높은 점수>")
for i in range(len(C)):
    print(C[i])
'''

A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

avg = sum(A) / len(A)

[print(x, end=' ') for x in A if x > avg]
print()
[print(x, end=' ') for x in A if x < avg]
