size = 100
x = [1] * (size+2)
for i in range(2, size+2):
    x[i] = x[i-1] + x[i-2]
    print (x[i-2])
