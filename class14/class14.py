# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)
# i = int(input("請輸入要跳繩的次數"))
# for i in range(1, i + 1):
#     if i % 10 == 0:
#         print("休息一下")
#         continue
#     print(i)
# import random

# print(random.randrange(3))
# print(random.randrange(0, 10, 2))
#終止值是進行下一次迴圈時，會從終止值的數開始進行抽籤
#ex:(start.stop.+)中的加=公差
# print(random.randint(1, 3))
# print(random.randint(1, 10))
#import random是隨機給一個數的指令
#簡短指令:
#import random as r
#
#print(r.randint(1,10))
#print(r.randrange(1,10))
#猜數字
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
