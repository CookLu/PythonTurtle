# 海龟画扇子（扇子的打开方式是从右往左）
# 思考如何让扇子从左往右打开？？？
import turtle  # 导入 turtle 库

turtle.bgcolor("teal")  # 设置背景颜色为teal
turtle.pencolor("khaki")  # 设置画笔颜色为khaki
turtle.speed(0)  # 设置海龟的绘图速度为0,最快。参数为1时最慢。
turtle.left(15)  # 绘图之前先让海龟向左旋转15度

'''用while循环实现            
i=1                         # i是while循环的计数器变量，设置让它从1开始计数。
                            # 事实上电脑的计数和我们人类不同，电脑是从0开始计数的，如0、1、2、3……，学for循环去体验电脑报数。
while i<=150:               # 循环体部分要执行150次，每次旋转1度，程序结束后就旋转了150度。
    turtle.forward(200)     # 海龟前进200个像素（步）
    turtle.backward(200)    # 海龟后退200个像素（步）
    turtle.left(1)          # 海龟向左旋转1度
    i=i+1                   # 改变计数器（计数器加1），否则会进入死循环
'''
# 用for循环实现
for i in range(150):  # range函数将会产生0到149，共150个整数。
    # for循环会自动遍历这150个整数，产生150次循环，所以for循环不用计数器。
    turtle.forward(200)  # 海龟前进200个像素（步）
    turtle.backward(200)  # 海龟后退200个像素（步）
    turtle.left(1)  # 海龟向左旋转1度

turtle.home()  # 让海龟回到原点

turtle.penup()  # 画笔抬起，海龟移动时不画线
turtle.right(90)  # 海龟向右旋转90度，也就是海龟的方向朝下。
turtle.forward(70)  # 海龟前进70步
turtle.pendown()  # 画笔落下，海龟移动时将画线

turtle.write("分明一夜文姬梦，只有青团扇子知。", align="center", font=("隶书", 16))  # 海龟书写文本
turtle.hideturtle()  # 隐藏藏海
turtle.done()