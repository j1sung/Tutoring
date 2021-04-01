def d(is_odd):
    if is_odd%2==0:
        print(1)
    else:
        print(0)

n = int(input("자연수 하나 입력: "))
print(d(n))