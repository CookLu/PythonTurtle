def setup():
    size(800, 600)  # 设定画面宽度、高度
    colorMode(HSB, 360, 100, 100)  # 色相、饱和度、亮度 颜色模型


def draw():
    cClouds = color(330, 25, 100)  # 云的颜色
    cSky = color(220, 50, 50)  # 天空的颜色
    cFurther = color(230, 25, 90)  # 远山的颜色
    cCloser = color(210, 70, 10)  # 近山的颜色
    background(cFurther)  # 背景为远山的颜色
    drawSky(cSky, cFurther)  # 画出天空颜色渐变效果
    drawClouds(cClouds)  # 画出彩色云朵效果
    drawMountains(cFurther, cCloser)  # 画出山脉效果


def mousePressed():  # 鼠标按键时
    noiseSeed(frameCount * int(random(10)))  # 用帧数初始化随机数种子


def drawSky(colSky, colFurther):  # 画出天空颜色渐变效果
    for y in range(height / 2):  # 从顶部开始绘制画面上半部分
        strokeWeight(1)  # 线粗细为1
        # 颜色插值，从天空颜色逐渐变成远山颜色
        stroke(lerpColor(colSky, colFurther, float(y) / (height / 2)))
        line(0, y, width, y)  # 横着的一条线


def drawClouds(colClouds):  # 画出彩色云朵效果
    noStroke()  # 不绘制线条
    for y in range(height / 3):  # 在上面三分之一部分
        for x in range(0, width, 2):  # 横向遍历
            noiseValue = noise(x * 0.004, y * 0.02)  # 柏林噪声
            ration = map(y, 0, height / 3, 150, 5)  # 越向下、云越透明
            fill(colClouds, ration * noiseValue)  # 设置透明度
            circle(x, y, 2)  # 画圆


def drawMountains(colFurther, colCloser):  # 画出山脉效果
    mountainLayer = 8  # 一共画8层山
    for n in range(mountainLayer):
        #  每一层山的y坐标的最小值
        yMin = map(n, 0, mountainLayer, height * 0.2, height * 0.8)
        # 山的颜色由远向近渐变
        fill(lerpColor(colFurther, colCloser, \
                       float(n + 1) / mountainLayer))
        beginShape()  # 开始画一些顶点组成的图形
        vertex(0, height)  # 第一个点在左下角
        for x in range(0, width + 1, 2):  # 从左到右遍历
            # 柏林噪声
            noiseValue = noise(x * 0.005, yMin * 0.02) \
                         + 0.03 * noise(x * 0.3, yMin * 0.2)
            # x横坐标对应的高度，越近的山，高度越向下
            yMountain = map(noiseValue, 0, 1, yMin, yMin + height / 2)
            vertex(x, yMountain)  # 添加这个点
        vertex(width, height)  # 最后一个点在右下角
        endShape(CLOSE)  # 结束画一些顶点组成的封闭图形