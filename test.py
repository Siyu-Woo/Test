#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/4/16 10:23
# @Author : Siyu Wu 
# @Email : sy-wu20@tsinghua.org.cn
# @Software: VScode

import math

def VehModel(x, y, v, theta, a, delta_theta, delta_t):
    """
    根据给定的当前状态和控制量，更新并返回车辆的下一个状态。

    参数:
    x, y         : 当前车辆的坐标
    v            : 当前车辆的速度
    theta        : 当前车辆的朝向角（单位为弧度）
    a            : 控制输入的加速度
    delta_theta  : 控制输入的朝向角速度
    delta_t      : 时间步长

    返回:
    (x_next, y_next, v_next, theta_next) : 更新后的状态
    """
    # 更新速度
    v_next = v + a * delta_t

    # 更新朝向角
    theta_next = theta + delta_theta * delta_t

    # 确保 theta_next 在 -pi 到 pi 范围内
    theta_next = (theta_next + pi) % (2 * pi) - pi

    # 更新位置
    x_next = x + v * cos(theta) * delta_t
    y_next = y + v * sin(theta) * delta_t

    return x_next, y_next, v_next, theta_next


# 示例使用
x, y, v, theta = 0.0, 0.0, 10.0, pi / 4  # 初始状态
a, delta_theta, delta_t = 2.0, pi / 180, 1.0  # 控制量和时间步长

# 调用函数获取下三步的状态，并输出