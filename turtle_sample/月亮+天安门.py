from turtle import *
import time
import turtle as t

#位移函数
def Skip(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

#画笔基础设置
t.screensize(1200,800)
t.pensize(5)
t.hideturtle()
t.speed(20)
t.pencolor("red")

#画笔移动
Skip(t,-200,100)

#画房盖
t.circle(40,90)
t.right(90)
t.forward(200)
t.right(90)
t.circle(40,90)
t.right(180)
t.forward(280)

#顶层
t.left(135)
t.forward(20)
t.left(45)
t.forward(252)
t.left(45)
t.forward(20)

Skip(t,-184,82)
t.right(135)
t.forward(20)
t.left(90)
t.forward(249)
t.left(90)
t.forward(20)

#第二层屋檐
Skip(t,-184,62)
t.left(110)
t.forward(50)
t.circle(-40,50)
t.left(150)
t.circle(30,60)
t.forward(354)
t.circle(30,60)
t.left(150)
t.circle(-40,50)
t.forward(50)

#第二层
Skip(t,-214,33)
t.left(110)
t.forward(30)
t.left(90)
t.forward(309)
t.left(90)
t.forward(30)

#第二层柱子
t.left(180)
Skip(t,-183,33)
t.forward(30)
Skip(t,-152,33)
t.forward(30)
Skip(t,-121,33)
t.forward(30)
Skip(t,-90,33)
t.forward(30)
Skip(t,-59,33)
t.forward(30)
Skip(t,-28,33)
t.forward(30)
Skip(t,3,33)
t.forward(30)
Skip(t,34,33)
t.forward(30)
Skip(t,65,33)
t.forward(30)
t.left(180)

#外墙
Skip(t,-214,3)
t.left(90)
t.forward(250)
t.left(90)
t.forward(100)
t.left(90)
t.forward(809)
t.left(90)
t.forward(100)
t.left(90)
t.forward(250)
Skip(t,-464,-15)
t.left(180)
t.forward(383)
Skip(t,-37,-15)
t.forward(383)

#正门和侧门
Skip(t,-79,-97)
t.left(90)
t.forward(15)
t.circle(-20,180)
t.forward(15)

Skip(t,-189,-97)
t.left(180)
t.forward(10)
t.circle(-15,180)
t.forward(10)

Skip(t,31,-97)
t.left(180)
t.forward(10)
t.circle(-15,180)
t.forward(10)

Skip(t,-269,-97)
t.left(180)
t.forward(10)
t.circle(-15,180)
t.forward(10)

Skip(t,111,-97)
t.left(180)
t.forward(10)
t.circle(-15,180)
t.forward(10)

#文字
Skip(t,-340,-15)
t.forward(20)

t.left(90)
t.forward(190)
t.left(90)
t.forward(20)

Skip(t,25,-15)
t.left(180)
t.forward(20)

t.left(90)
t.forward(190)
t.left(90)
t.forward(20)

#画框
Skip(t,-77,-4)
t.left(180)
t.forward(45)
t.left(90)
t.forward(36)
t.left(90)
t.forward(45)
t.left(90)
t.forward(36)


def gotopos(x, y):
    up()
    goto(x, y)
    down()
    ht()

def writez(x, y, str_, size=56, font="华文行楷"):
    gotopos(x, y)
    write(str_, font=(font, size))


setup(1280, 800)
speed(5)
bgcolor("#9c917f")
color("#afa697")
begin_fill()
gotopos(0, -400)
circle(400)
end_fill()
#author()
color("#7d776d")
s = "在天愿作比翼鸟"
s2 = "在地愿为连理枝"
for i in range(len(s)):
    writez(560, 350 - i * 50, s[i], 36)
for i in range(len(s2)):
    writez(460, 350 - i * 50, s2[i], 36)
color("#888475")
writez(-50, 100, "我")
writez(-50, 40, "的")
writez(-160, 0, "心", 96)
writez(-50, 0, "月", 176)
writez(33, -30, "代", 62)
writez(-18, -95, "表", 78)
writez(-213, -210, "亮", 196)
t.done()