n = int(input())

print("A long time ago in a galaxy",  end = '')
while n > 0:
    n -= 1
    if n == 0:
        break
    print("far", end = ',')
print('far away...')