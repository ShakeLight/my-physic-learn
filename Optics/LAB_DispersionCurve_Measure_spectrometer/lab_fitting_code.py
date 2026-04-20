import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

# 1. 原始数据录入
wavelengths = np.array([579.0, 546.1, 435.8]) 
raw_angles =[
    (51, 8, 27.6),  # 橙
    (51, 31, 30), # 绿
    (53, 31, 30)  # 蓝
]
A_deg = 60.0

# 2. 预处理数据
def dms_to_deg(d, m, s):
    return d + m/60.0 + s/3600.0

delta_mins = np.array([dms_to_deg(*angle) for angle in raw_angles])
A_rad = np.radians(A_deg)
n_measured = np.sin((A_rad + np.radians(delta_mins)) / 2) / np.sin(A_rad / 2)

# 3. Cauchy 拟合
def cauchy_func(lam, a, b):
    return a + b / (lam**2)

popt, _ = curve_fit(cauchy_func, wavelengths, n_measured)
A_fit, B_fit = popt
n_pred = cauchy_func(wavelengths, A_fit, B_fit)
r_squared = r2_score(n_measured, n_pred)

# 4. 绘图与标注
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False 
plt.style.use('seaborn-v0_8-paper')

fig, ax = plt.subplots(figsize=(9, 6), dpi=120)

# 绘制拟合线
x_fit = np.linspace(min(wavelengths)-20, max(wavelengths)+20, 100)
ax.plot(x_fit, cauchy_func(x_fit, A_fit, B_fit), 'b--', label='Cauchy 方程拟合曲线', linewidth=1.5)

# 绘制散点
ax.scatter(wavelengths, n_measured, color='red', s=50, label='实验测量值', zorder=3)

# 【重点：循环标注每个点的坐标】
for x, y in zip(wavelengths, n_measured):
    label = f"({x:.1f}, {y:.4f})"
    ax.annotate(label, 
                (x, y), 
                textcoords="offset points", 
                xytext=(0, 10), 
                ha='center', 
                fontsize=9,
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", lw=0.5, alpha=0.8))

# 拟合公式显示
formula = r'$n = {:.4f} + \frac{{ {:.2f} }}{{\lambda^2}}$'.format(A_fit, B_fit)
ax.text(0.05, 0.95, f'拟合方程: {formula}\n决定系数: $R^2 = {r_squared:.6f}$', 
        transform=ax.transAxes, fontsize=11, verticalalignment='top',
        bbox=dict(boxstyle="round", facecolor='white', alpha=0.9))

ax.set_xlabel('波长 $\lambda$ (nm)', fontsize=12)
ax.set_ylabel('折射率 $n$', fontsize=12)
ax.set_title('三棱镜色散关系曲线及 Cauchy 方程拟合', fontsize=14)
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper right')

plt.tight_layout()
plt.show()