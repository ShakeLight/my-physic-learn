import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# --- 1. 原始实验数据 ---
k = np.array([1, 2, 3, 4, 5, 6, 7])
T = 78.8e-6  # 周期 78.8 us 转化为 s
t_data = (k - 1) * T
v_data = np.array([99.51, 67.41, 45.33, 30.47, 20.65, 13.89, 9.28]) # 单位 mV

# --- 2. 拟合函数定义 (V = V0 * exp(-alpha * t)) ---
def damping_model(t, V0, alpha):
    return V0 * np.exp(-alpha * t)

# 进行非线性拟合
popt, pcov = curve_fit(damping_model, t_data, v_data, p0=[100, 5000])
V0_fit, alpha_fit = popt

# --- 3. 计算 Q 值 (测量值) ---
# Q = omega_0 / (2 * alpha), 这里的 omega_0 约等于 2*pi / T
Q_measured = np.pi / (alpha_fit * T)

# 计算决定系数 R^2
residuals = v_data - damping_model(t_data, *popt)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((v_data - np.mean(v_data))**2)
r_squared = 1 - (ss_res / ss_tot)

# --- 4. 绘图 ---
plt.rcParams['font.sans-serif'] = ['SimHei'] # 解决中文显示
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(9, 6))
plt.scatter(t_data * 1e6, v_data, color='red', label='实验测量点 ($V_k$)')

t_smooth = np.linspace(0, max(t_data), 200)
v_smooth = damping_model(t_smooth, V0_fit, alpha_fit)
plt.plot(t_smooth * 1e6, v_smooth, 'b-', label='指数包络拟合曲线')

# 标注结果
result_text = (f'拟合方程: $V(t) = {V0_fit:.2f} \cdot e^{{-{alpha_fit:.1f}t}}$\n'
               f'实验衰减系数 $\\alpha$ = {alpha_fit:.1f} $s^{{-1}}$\n'
               f'实验品质因数 $Q$ = {Q_measured:.2f}\n'
               f'决定系数 $R^2$ = {r_squared:.5f}')

plt.text(150, 60, result_text, bbox=dict(facecolor='white', alpha=0.8), fontsize=11)

plt.title('RLC 阻尼振荡电路振幅衰减拟合', fontsize=14)
plt.xlabel('时间 $t$ ($\mu s$)', fontsize=12)
plt.ylabel('电压振幅 $V_k$ (mV)', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

print(f"拟合结果：alpha = {alpha_fit:.2f}, Q = {Q_measured:.2f}, R2 = {r_squared:.5f}")