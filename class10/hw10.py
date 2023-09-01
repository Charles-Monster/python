#turtle.home() # 是讓烏龜回到原點的指令
#turtle.clear() # 清空畫面指令
#import time  # 匯入time模組
#time.sleep(1) # 延遲1秒
import turtle

turtle.penup()
for i in range(8):
    turtle.forward(100)
    turtle.stamp()
    turtle.backward(100)
    turtle.right(45)
