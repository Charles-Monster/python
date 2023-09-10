'''
HW12:
輸入一組整數範圍，將範圍中的所有質數顯示於畫面上。
EX:
請輸入開始整數:10
請輸入結束整數:50
11
13
17
19
23
29
31
37
41
43
47
'''
# a = int(input("請輸入正整數"))
# ans = False
# if a ==1:
#     print("1不是質數")
# else:
#     for i in range(2,int(a/2+1)):
#         if a % i ==0:
#             ans = True
#     if ans == True:
#         print(str(a)+"不是質數")
#     else:
#         print(str(a)+"是質數")
y = int(input('請輸入一個數字:'))
ans = False
if y == 1:
    print('1不是一個質數')
else:
    for i in range(2, y - 1):
        if y % 0 == 0 or y == y - 1:
            ans = False
        else:
            ans = True
if ans == True:
    print(str(y) + "這不是一個質數!")

else:
    print(str(y) + "這是一個質數!")
