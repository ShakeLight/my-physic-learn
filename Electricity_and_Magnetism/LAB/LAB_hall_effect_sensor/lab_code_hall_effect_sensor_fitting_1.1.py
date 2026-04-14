import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import matplotlib as mpl

# --- 1. 数据准备 ---
# 励磁电流 Im (mA)
Im = np.array([50, 100, 150, 200, 250, 300, 350, 400])
# 霍尔电压 Vh (mV)
Vh = np.array([0.335, 0.687, 1.02, 1.37, 1.71, 2.05, 2.39, 2.73])
# 假设磁场转换系数 k = 4.285 (根据北师大实验手册常用值)
B = 4.046 * Im 

# --- 2. 线性拟合计算 ---
slope, intercept, r_value, p_value, std_err = stats.linregress(B, Vh)
fit_line = slope * B + intercept
r_square = r_value**2

# --- 3. 字体兼容性处理 (解决乱码) ---
# 自动寻找系统内支持中文的字体
for font in ['Microsoft YaHei', 'SimHei', 'SimSun', 'Arial Unicode MS']:
    if font in [f.name for f in mpl.font_manager.fontManager.ttflist]:
        plt.rcParams['font.sans-serif'] = [font]
        break
plt.rcParams['axes.unicode_minus'] = False # 解决负号显示为方框

# --- 4. 精美绘图 ---
plt.figure(figsize=(8, 6), dpi=100)
plt.style.use('seaborn-v0_8-muted') # 使用简洁美观的主题

# 绘制原始数据点
plt.scatter(B, Vh, color='red', s=50, label='实验测量值 $V_H$', zorder=3)

# 绘制拟合直线
label_text = f'拟合直线: $V_H = {slope:.5f}B {"+" if intercept>0 else "-"}{abs(intercept):.4f}$'
plt.plot(B, fit_line, color='royalblue', linestyle='--', linewidth=2, label=label_text)

# 添加图表信息
plt.title('霍尔电压 $V_H$ 与磁感应强度 $B$ 的线性拟合', fontsize=14, pad=15)
plt.xlabel('磁感应强度 $B$ ($\mu T$)', fontsize=12)
plt.ylabel('霍尔电压 $V_H$ (mV)', fontsize=12)

# 在左上角添加决定系数文本框
stats_box = f'$R^2 = {r_square:.5f}$\n$a = {slope:.6f}$ mV/$\mu T$'
plt.gca().text(0.05, 0.92, stats_box, transform=plt.gca().transAxes, 
               bbox=dict(boxstyle='round', facecolor='white', alpha=0.7), fontsize=11)

plt.legend(loc='lower right', frameon=True, fontsize=10)
plt.grid(True, linestyle=':', alpha=0.7)
plt.tight_layout()

# 显示图像
plt.show()

# 控制台打印结果，方便填表
print(f"拟合斜率 a = {slope:.6f}")
print(f"决定系数 R^2 = {r_square:.6f}")