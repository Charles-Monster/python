'''
作業1.
使用turtle模組與for 劃出一個正六邊形
作業2.
做一個可以列印出0-100之間3的倍數的機器。
ex:
3
6
9
12
....
'''
import turtle

for i in range(6):

    turtle.forward(60),  #int or float
    turtle.left(60)  #int or float
turtle.done()  # 讓視窗保持顯示

for i in range(3, 100, 3):
    print(i)
