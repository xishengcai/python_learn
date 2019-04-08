#!/usr/bin/python
# -*- coding: utf-8 -*
import math
import random as rdm
import matplotlib.pyplot as plt


# Win10环境下用Python2.7.0写的实现程序。
# 用的数据：由于暂时没有数据，随机生成线性数据，然后加的噪声；
# 用到的函数： 向量内积（点乘）函数、平均值、协方差


# 向量内积函数
def dot(m, n):
    return sum(m_i * n_i for m_i, n_i in zip(m, n))


# 平均值函数
def mean(x):
    return sum(x) / len(x)


# 计算协方差
# 可以通俗的理解为：两个变量在变化过程中是同方向变化？还是反方向变化？同向或反向程度如何？
# Cov(X,Y)=E[(X-\mu _{x})(Y-\mu _{y})]
def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]


def covariance(x, y):
    return dot(de_mean(y), de_mean(y)) / (len(x) - 1)


# 计算相关系数
def correlation(x, y):
    s_x = math.sqrt(covariance(x, x))
    s_y = math.sqrt(covariance(y, y))
    return covariance(x, y) / (s_x * s_y)


# ------------最小二乘法 线性回归系数求法-----------
def line_coef(x, y):
    s1 = covariance(x, x) * (len(x) - 1)
    s2 = dot(y, de_mean(x))
    beta = s2 / s1
    alpha = mean(y) - beta * mean(x)
    return alpha, beta


# ******实验*****
# 生成随机数据
def ran(a1, a2, x):
    return [a1 + a2 * x_i for x_i in x]


a1 = 0
a2 = 2.5
print '实际样本系数 alpha: %f, beta: %f' % (a1, a2)
x = range(10)
y = ran(a1, a2, x)
print y

# 线性拟合
alpha, beta = line_coef(x, y)
print '*------------------------最小二乘法------------------------*'
print '系数为: ', alpha, beta


# 可视化
# 开一个【2x2】的图像窗口
plt.subplot(111)
plt.figure(1)
plt.scatter(x, y, marker='*', color='b')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title('Linear Fit')

# 拟合直线
plt.plot(x, [alpha + beta*x_i for x_i in x], color='orange')
# plt.subplot(222)
plt.show()


def err(alpha, beta, x, y):
    # 误差分析
    # ----主要考察：（1）误差平方和； （2）R方（越大拟合得越好）
    # 返回每个实际y值与拟合值差向量
    return [y_i -(alpha+beta * x_i) for x_i, y_i in zip(x, y)]


def error_total(alpha, beta, x, y):
    y1 = err(alpha, beta, x, y)
    return dot(y1, y1)


print '误差为: ', error_total(alpha, beta, x, y)


# 计算R方
def r_square(alpha, beta, x, y):
    return 1 - error_total(alpha, beta, x, y) / covariance(y, y)


R_square = r_square(alpha, beta, x, y)
print 'R 方: ', R_square
if R_square > 0.95:
    print '在0.5置信水平下，该线性拟合不错'
else:
    print '在0.5置信水平下， 该线性拟合效果不佳'





