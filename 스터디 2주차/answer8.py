n = int(input("2~9의 숫자중 하나를 입력하세요: "))

print(n,"단: ")

for i in range(1, 10):
    print(n,'*',i,'=',n*i, end='   ')
