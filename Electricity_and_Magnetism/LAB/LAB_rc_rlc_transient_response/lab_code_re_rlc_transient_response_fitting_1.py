import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 定义一阶暂态模型
def rc_model(t, u0, u_inf, tau):
    return u_inf + (u0 - u_inf) * np.exp(-t / tau)

# --- 数据输入 ---
# 第一组: C = 326.3 nF, R = 60 Ohm
t1 = np.array([0.00, 1.47, 4.92, 7.23, 12.92, 20.03, 25.92, 32.57, 38.91, 77.69])
u1 = np.array([1.99, 1.71, 1.02, 0.636, -0.119, -0.767, -1.13, -1.40, -1.59, -1.94])
theory1 = 60 * 326.3e-9 * 1e6

# 第二组: C = 1.016 uF, R = 60 Ohm
t2 = np.array([0.00, 9.21, 17.47, 28.03, 50.68, 69.50, 92.73, 114.04, 128.83, 169.34])
u2 = np.array([1.98, 1.37, 0.887, 0.360, -0.472, -0.933, -1.31, -1.54, -1.65, -1.93])
theory2 = 60 * 1.016e-6 * 1e6

# --- 执行拟合 ---
popt1, _ = curve_fit(rc_model, t1, u1, p0=[2, -2, 20])
popt2, _ = curve_fit(rc_model, t2, u2, p0=[2, -2, 60])

# 计算 R^2
def get_r2(y, t, popt):
    res = y - rc_model(t, *popt)
    return 1 - (np.sum(res**2) / np.sum((y - np.mean(y))**2))

r2_1 = get_r2(u1, t1, popt1)
r2_2 = get_r2(u2, t2, popt2)

# --- 绘图 ---
plt.figure(figsize=(12, 7))

# 第一组绘图
plt.scatter(t1, u1, color='blue', alpha=0.6, label='数据点 (326.3nF)')
t_fine1 = np.linspace(0, 180, 200)
plt.plot(t_fine1, rc_model(t_fine1, *popt1), 'b--', label='拟合曲线 1')

# 第二组绘图
plt.scatter(t2, u2, color='red', alpha=0.6, label='数据点 (1.016uF)')
plt.plot(t_fine1, rc_model(t_fine1, *popt2), 'r-', label='拟合曲线 2')

# 构建信息文本框 (不含相对误差)
info1 = (f"【第一组 C=326.3nF】\n"
         f"公式: $u(t) = {popt1[1]:.2f} + ({popt1[0]:.2f}{popt1[1]:+.2f})e^{{-t/{popt1[2]:.2f}}}$\n"
         f"拟合 $\\tau = {popt1[2]:.2f} \\mu s$\n"
         f"理论值 $RC = {theory1:.2f} \\mu s$\n"
         f"$R^2 = {r2_1:.5f}$")

info2 = (f"【第二组 C=1.016uF】\n"
         f"公式: $u(t) = {popt2[1]:.2f} + ({popt2[0]:.2f}{popt2[1]:+.2f})e^{{-t/{popt2[2]:.2f}}}$\n"
         f"拟合 $\\tau = {popt2[2]:.2f} \\mu s$\n"
         f"理论值 $RC = {theory2:.2f} \\mu s$\n"
         f"$R^2 = {r2_2:.5f}$")

plt.text(80, 0.5, info1, fontsize=10, bbox=dict(facecolor='white', edgecolor='blue', alpha=0.8))
plt.text(80, -1.0, info2, fontsize=10, bbox=dict(facecolor='white', edgecolor='red', alpha=0.8))

plt.title("RC电路不同电容下的暂态过程拟合对比", fontsize=14)
plt.xlabel("时间 $t$ ($\\mu s$)", fontsize=12)
plt.ylabel("电压 $u$ (V)", fontsize=12)
plt.legend(loc='upper right')
plt.grid(True, which='both', linestyle=':', alpha=0.5)
plt.ylim(-2.5, 2.5)
plt.show()