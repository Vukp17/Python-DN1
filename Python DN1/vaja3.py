import math


P = int(input())
B = int(input())
D = int(input())

d1=P/B
x = math.trunc(d1)
ost=P%B
res= x*D + ost
print(res)
