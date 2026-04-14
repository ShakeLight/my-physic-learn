import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import matplotlib as mpl

# --- 1. 数据准备 (对应实验一表格第一行和最后一行) ---
# U++ (mV)
U_pp = np.array([-4.18, -3.83, -3.50, -3.14, -2.81, -2.46, -2.11, -1.78])
# Vh (mV)
Vh = np.array([0.335, 0.687, 1.02, 1.37, 1.71, 2.05, 2.39, 2.73])

# --- 2. 线性拟合计算 VH = alpha * Upp + beta ---
alpha, beta, r_value, p_value, std_err = stats.linregress(U_pp, Vh)
fit_line_2 = alpha * U_pp + beta
r_square_2 = r_value**2

# --- 3. 字体兼容性处理 ---
for font in ['Microsoft YaHei', 'SimHei', 'SimSun', 'STHeiti']:
    if font in [f.name for f in mpl.font_manager.fontManager.ttflist]:
        plt.rcParams['font.sans-serif'] = [font]
        break
plt.rcParams['axes.unicode_minus'] = False 

# --- 4. 精美绘图 ---
plt.figure(figsize=(8, 6), dpi=100)
plt.style.use('seaborn-v0_8-muted')

# 绘制散点
plt.scatter(U_pp, Vh, color='darkorange', s=50, edgecolors='k', label='测量数据点 $(U_{++}, V_H)$', zorder=3)

# 绘制拟合直线
# 使用 f-string 动态构建标签，自动判断 beta 的符号
sign = "+" if beta >= 0 else "-"
label_text = f'拟合直线: $V_H = {alpha:.4f}U_{{++}} {sign} {abs(beta):.4f}$'
plt.plot(U_pp, fit_line_2, color='seagreen', linestyle='-', linewidth=2, label=label_text)

# 图表装饰
plt.title('霍尔电压 $V_H$ 与测量电压 $U_{++}$ 的关系拟合', fontsize=14, pad=15)
plt.xlabel('测量电压 $U_{++}$ (mV)', fontsize=12)
plt.ylabel('霍尔电压 $V_H$ (mV)', fontsize=12)

# 添加统计信息框 (R^2, alpha, beta)
stats_box = (f'拟合系数 $\\alpha = {alpha:.4f}$\n'
             f'偏移量 $\\beta = {beta:.4f}$ mV\n'
             f'决定系数 $R^2 = {r_square_2:.5f}$')
plt.gca().text(0.05, 0.92, stats_box, transform=plt.gca().transAxes, 
               bbox=dict(boxstyle='round', facecolor='white', alpha=0.8), fontsize=11, verticalalignment='top')

plt.legend(loc='lower right', frameon=True)
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()

# 显示
plt.show()

# 输出填表数据
print(f"alpha = {alpha:.6f}")
print(f"beta = {beta:.6f}")
print(f"R^2 = {r_square_2:.6f}")