def pot(a,b):
    res = 1
    for i in range(b):
        res*=a
    return res

print(pot(10,3))