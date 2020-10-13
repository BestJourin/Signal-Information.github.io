import numpy as np
import matplotlib.pyplot as plt


def f2(n):
    return np.power(1,n)

def g2(n):
    return np.power(2,n)

def h2(n):
    return np.power(1/2,n)

def I2(n):
    return np.power(-2,n)

def y2(n):
    return np.power(-1/2,n)


n2 = np.arange(-5.0, 5.0, 1)


plt.figure('离散复指数函数信号')
plt.subplot(231)      # 2 rows, 3 column, 1plot
plt.plot(n2, g2(n2), 'bo')
#设置坐标轴范围
plt.xlim((-6, 6))
plt.ylim((-1,10))
#设置坐标轴名称
plt.xlabel('n')
plt.ylabel('X[n]')
#设置坐标轴刻度
ax = plt.gca()                                            # get current axis 获得坐标轴对象
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')          # 指定下边的边作为 x 轴   指定左边的边为 y 轴
ax.spines['bottom'].set_position(('data', 0))   #指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
ax.spines['left'].set_position(('data', 0))
plt.title(r"$Functional Equation:ω=0,r=2,X[n]=2^n$")


plt.subplot(232)      # 2 rows, 3 column, 2plot
plt.plot(n2, h2(n2), 'ro')
#设置坐标轴范围
plt.xlim((-6, 6))
plt.ylim((-1,10))
#设置坐标轴名称
plt.xlabel('n')
plt.ylabel('X[n]')
#设置坐标轴刻度
ax = plt.gca()                                            # get current axis 获得坐标轴对象
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')          # 指定下边的边作为 x 轴   指定左边的边为 y 轴
ax.spines['bottom'].set_position(('data', 0))   #指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
ax.spines['left'].set_position(('data', 0))
plt.title(r"$Functional Equation:ω=0,r=\frac{1}{2},X[n]=\frac{1}{2}^n$")


plt.subplot(233)      # 2 rows, 3 column, 3plot
plt.plot(n2, f2(n2), 'go')
#设置坐标轴范围
plt.xlim((-6, 6))
plt.ylim((-1,10))
#设置坐标轴名称
plt.xlabel('n')
plt.ylabel('X[n]')
#设置坐标轴刻度
ax = plt.gca()                                            # get current axis 获得坐标轴对象
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')          # 指定下边的边作为 x 轴   指定左边的边为 y 轴
ax.spines['bottom'].set_position(('data', 0))   #指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
ax.spines['left'].set_position(('data', 0))
plt.title(r"$Functional Equation:ω=0,r=1,X[n]=1^n$")


plt.subplot(234)      # 2 rows, 3 column, 4plot
plt.plot(n2, I2(n2), 'mo',)
#设置坐标轴范围
plt.xlim((-6, 6))
plt.ylim((-10,10))
#设置坐标轴名称
plt.xlabel('n')
plt.ylabel('X[n]')
#设置坐标轴刻度
ax = plt.gca()                                            # get current axis 获得坐标轴对象
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')          # 指定下边的边作为 x 轴   指定左边的边为 y 轴
ax.spines['bottom'].set_position(('data', 0))   #指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
ax.spines['left'].set_position(('data', 0))
plt.title(r"$Functional Equation:ω=0,r=-2,X[n]=(-2)^n$")


plt.subplot(235)      # 2 rows, 3 column, 5plot
plt.plot(n2, y2(n2), 'yo')
#设置坐标轴范围
plt.xlim((-6, 6))
plt.ylim((-10,10))
#设置坐标轴名称
plt.xlabel('n')
plt.ylabel('X[n]')
#设置坐标轴刻度
ax = plt.gca()                                            # get current axis 获得坐标轴对象
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')          # 指定下边的边作为 x 轴   指定左边的边为 y 轴
ax.spines['bottom'].set_position(('data', 0))   #指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
ax.spines['left'].set_position(('data', 0))
plt.title(r"$Functional Equation:ω=0,r=-\frac{1}{2},X[n]=(-\frac{1}{2})^n$")


plt.subplot(236)      # 2 rows, 3 column, 6plot

plt.plot(n2, g2(n2), 'bo',label=r"$X[n]=2^n$")
plt.plot(n2, h2(n2), 'ro',label=r"$X[n]=\frac{1}{2}^n$")
plt.plot(n2, f2(n2), 'go',label=r"$X[n]=1^n$")
plt.plot(n2, I2(n2), 'mo',label=r"$X[n]=(-2)^n$")
plt.plot(n2, y2(n2), 'yo',label=r"$X[n]=(-\frac{1}{2})^n$")
plt.legend(loc='best')
#设置坐标轴范围
plt.xlim((-6, 6))
plt.ylim((-10,10))
#设置坐标轴名称
plt.xlabel('t/s')
plt.ylabel('X(t)')
ax = plt.gca()                                            # get current axis 获得坐标轴对象
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')          # 指定下边的边作为 x 轴   指定左边的边为 y 轴
ax.spines['bottom'].set_position(('data', 0))   #指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
ax.spines['left'].set_position(('data', 0))
plt.title("All The Functional Equation")