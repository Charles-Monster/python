'''
製作一個丟骰子的指令
使用者可以輸入擲骰子的次數n
指令會一次回傳所有擲骰子的結果
程式內容前兩行打成
import random
def roll_dice(n):
'''
#上面是我的作業
n=(int(input('請輸入擲骰子的次數:')))
for n in range(n):
    import random
    ans=random.randint(1,6)
    def roll_dice(n):
        print(str(ans))
    roll_dice(n)
#下面是老師的範例
import random

def roll_dice(n):
    dice=[]
    for i in range(n):
        dice.append(random.randint(1,6))
    #回傳結果到dice，dice會新增迴圈中的隨機數
    return dice
cnt=int(input('輸入丟骰子的次數:'))
print(roll_dice(cnt))