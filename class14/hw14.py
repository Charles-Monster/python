import random

a = random.randint(1, 100)
while True:
    i = int(input("請輸入1~100的數:"))
    if i == a:
        print("恭喜猜中")
        break
    elif i > a:
        print("再小一點")
    elif i < a:
        print("再大一點")
