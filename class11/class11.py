#x = int(input('請輸入一個整數'))
#Sum = 0
#for i in range(x + 1):
#   Sum = Sum + i
#x = str(x)
#Sum = str(Sum)
#print("從零加到" + x + "的總合為 " + Sum)
#x = int(x)
#Sum = 0
#Sum = (x + 1) * x / 2
#x = str(x)
#Sum = str(Sum)
#print("從零加到" + x + "的總合為 " + Sum)
for i in range(1, 10):
    for j in range(1, 10):
        i = int(j)
        Sum = j * i
        Sum = str(Sum)
        i = str(i)
        j = str(j)

        print(j + '* ' + i + ' = ' + Sum)
