a = float(input())
b = float(input())
c = float(input())
d = float(input())

def Tri(a, b, c, d):
    if a + b + c > d and a + b + d > b and c + d > a + b:
        return True
    else: 
        return False

if a/b == c/d:
    print("true")
    if Tri(a, b, c, d) or Tri(a, c, b, d) or Tri(a, d, b, c):
        print(1)
    else: print(0)
elif a/c == b/d:
    if Tri(a, b, c, d) or Tri(a, c, b, d) or Tri(a, d, b, c):
        print(1)
    else: print(0)
elif a/d == b/c: 
    if Tri(a, b, c, d) or Tri(a, c, b, d) or Tri(a, d, b, c):
        print(1)
    else: print(0)
else: print(0)