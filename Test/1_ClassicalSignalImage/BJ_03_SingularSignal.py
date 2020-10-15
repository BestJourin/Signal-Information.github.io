import numpy as np
import matplotlib.pyplot as plt

def x(t):
    return 0*(t<-2)+(t+2)*(t>=-2)

def y(t):
    return 0*(t<-2)+(t+2)*[True if (i>=-2 and i<=2) else False for i in t]+4*(t>2)

def Z(t):
    return 0*(t<-2)+(t+2)*[True if (i>=-2 and i<=2) else False for i in t]+0*(t>2)

def u(t):
    return 0*(t<0)+1*(t>=0)


t1 = np.arange(-5.0, 5.0, 0.01)


plt.figure('奇异信号')

plt.subplot(221)      # 2 rows, 2 column, 1plot

plt.plot(t1, x(t1), 'r-')
#设置坐标轴范围
plt.xlim((-5, 5))
plt.ylim((-1,10))
#设置坐标轴名称
plt.xlabel('t/s')
plt.ylabel('X(t)')
#设置坐标轴刻度 #get current axis 获得坐标轴对象
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')# 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')# 指定下边的边作为 x 轴   指定左边的边为 y 轴
ax.spines['bottom'].set_position(('data', 0))#指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
ax.spines['left'].set_position(('data', 0))
plt.title(r"$Functional Equation:u(t)=\{_{t-1 (t\geq{-2})}^{0 (t<-2)}$")

plt.subplot(222)      # 2 rows, 2 column, 2plot

plt.plot(t1, y(t1), 'g-')
#设置坐标轴范围
plt.xlim((-5, 5))
plt.ylim((-1,10))
#设置坐标轴名称
plt.xlabel('t/s')
plt.ylabel('X(t)')
#设置坐标轴刻度 #get current axis 获得坐标轴对象
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')# 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')# 指定下边的边作为 x 轴   指定左边的边为 y 轴
ax.spines['bottom'].set_position(('data', 0))#指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
ax.spines['left'].set_position(('data', 0))
# plt.title("Functional Equation:u(t)="r"$\begin{cases}{4 (t>{2})}\\{t+2(-2\leq t\leq2)}\\{0 (t<-2)}\end{cases}$")
plt.title(r"$Functional Equation:X(t)=\{_{4 (t>{2})}{t+2(-2\leq t\leq2)}^{0 (t<-2)}$")

plt.subplot(223)      # 2 rows, 2 column, 3plot

plt.plot(t1, Z(t1), 'm-')
#设置坐标轴范围
plt.xlim((-5, 5))
plt.ylim((-1,10))
#设置坐标轴名称
plt.xlabel('t/s')
plt.ylabel('X(t)')
#设置坐标轴刻度 #get current axis 获得坐标轴对象
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')# 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')# 指定下边的边作为 x 轴   指定左边的边为 y 轴
ax.spines['bottom'].set_position(('data', 0))#指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
ax.spines['left'].set_position(('data', 0))
plt.title(r"$Functional Equation:X(t)=\{_{0 (t<{-2}Ut>{2})}^{t+2(-2\leq t\leq2)}$")

plt.subplot(224)      # 2 rows, 2 column, 4plot

plt.plot(t1, u(t1), 'b-')
#设置坐标轴范围
plt.xlim((-5, 5))
plt.ylim((-1,10))
#设置坐标轴名称
plt.xlabel('t/s')
plt.ylabel('u(t)')
#设置坐标轴刻度 #get current axis 获得坐标轴对象
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')# 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')# 指定下边的边作为 x 轴   指定左边的边为 y 轴
ax.spines['bottom'].set_position(('data', 0))#指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
ax.spines['left'].set_position(('data', 0))
plt.title(r"$Functional Equation:X(t)=\{_{1 (t\geq{0})}^{0 (t<0)}$")
plt.show()
