x = int(input('請輸入一個開始的正整數'))
y = int(input('請輸入一個結束的正整數'))  #數值要比x大
for i in range(y - x + 1):
    a = x % 7
    if (a == 0):
        print(x)
    x = x + 1