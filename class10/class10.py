#星形中心為正五邊形，每一外角360度/5=72度
#星形每隻銳角的角度=180度-2*72度=36度
#180-內角=外角
import turtle

turtle.pensize(5)  #線徑寬度1~10
turtle.pencolor("yellow")  #線的顏色
turtle.fillcolor("yellow")  #線的顏色
turtle.begin_fill()
for i in range(5):
    turtle.forward(200)
    turtle.right(144)
turtle.end_fill()

turtle.done()