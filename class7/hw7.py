'''
判斷輸入成績的等第
使用者輸入成績
顯示使用者的等第
成績等第
A : 90 以上
B : 80 分到 89 分
C : 70 分到 79 分
D : 60 分到 69 分
E : 59 分以下
ex:
例如:使用者輸入成績50 顯示E。使用者輸入62則顯示D
'''
score = int(input("請輸入你的分數"))
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('c')
elif score >= 60:
    print('d')
else:
    print('e')
