import turtle
import time  # 匯入time模組

turtle.shape('circle')
turtle.shapesize(0.01)
turtle.home()
turtle.stamp()
turtle.forward(100)
turtle.penup()
turtle.backward(100)
for i in range(60):
    time.sleep(1)  # 延遲1秒
    turtle.clear()
    turtle.pendown()
    turtle.stamp()
    turtle.right(6)
    turtle.forward(100)
    turtle.penup
    turtle.backward(100)
