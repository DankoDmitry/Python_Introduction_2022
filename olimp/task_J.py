n, q = list(map(int,input().split()))

P = input()

L = []

for i in range(q):
    a, b = list(map(int,input().split()))
    if a > b:
        c = a
        a = b
        b = c
    
    if (P[a-1] == '(') and (P[b-1] == ')'):
        open = 0
        close = 0
        for i in range(a-1):
            if P[i] == '(': 
                open += 1
            else: close += 1
        if open > close: L.append('Yes')
        else: L.append('No')
    else:
        L.append('Yes')

print(*L, sep='\n')