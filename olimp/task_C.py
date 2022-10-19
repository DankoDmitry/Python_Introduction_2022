
def f (A):
    B = str(input())

    A = str(A)

    six = 0
    nine = 0
    sum = 0

    for i in A:
        j = int(i)
        sum += j
        if j == 6: six += 1
        if j == 9: nine += 1

    print(A)
    if sum % 3 != 0: 
        print(-1)
    else:
        if sum % 9 == 0:
            print(0)
        elif sum % 9 == 3 and (nine > 0 or six > 2):
            if nine > 0:
                print(1)
            else: print(2)
        elif sum % 9 == 6 and (nine > 1 or six > 0):
            if six > 0:
                print(1)
            else: print(2)
        else: 
            print(-1)

i = 1
while True:
    f(i)
    i += 1