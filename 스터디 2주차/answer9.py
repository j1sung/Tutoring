def cal(n, o, m):
    if o == '+':
        print(n,o,m,'=',n+m)
    elif o == '-':
        print(n,o,m,'=',n-m)
    elif o == '*':
        print(n,o,m,'=',n*m)
    elif o == '/':
        print(n,o,m,'=',n/m)
    elif o == '//':
        print(n, o, m, '=', n // m)
    elif o == '%':
        print(n,o,m,'=',n%m)

#n, o, m = map(int, str, int, input("피연산자, 연산자, 피연산자 순으로 입력해주세요: ").split(' '))  이런식으로 써보고 싶었는데 비슷한 방법 있을까요?

n, m = map(int, input("피연산자: ").split())
o = input("연산자: ")
print()

cal(n, o, m)