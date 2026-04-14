import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import matplotlib.font_manager as fm

# --- 1. 数据准备 (来自你的实验2表格) ---
Is = np.array([1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00]) # mA
Vh = np.array([0.41, 0.82, 1.23, 1.64, 2.06, 2.47, 2.88, 3.30]) # mV

# --- 2. 线性拟合 ---
slope, intercept, r_value, p_value, std_err = stats.linregress(Is, Vh)
fit_line = slope * Is + intercept
r_square = r_value**2

# --- 3. 彻底解决乱码：手动指定系统字体路径 ---
# Windows 系统的微软雅黑字体路径通常是这个
font_path = 'C:/Windows/Fonts/msyh.ttc' 
try:
    prop = fm.FontProperties(fname=font_path)
except:
    # 如果路径不对，尝试系统默认寻找
    prop = fm.FontProperties(family='SimHei')

# 设置全局参数解决负号乱码
plt.rcParams['axes.unicode_minus'] = False 

# --- 4. 绘图 ---
plt.figure(figsize=(9, 6), dpi=100)
plt.style.use('seaborn-v0_8-whitegrid')

# 散点
plt.scatter(Is, Vh, color='#d62728', s=60, label='测量数据 $V_H$', zorder=3)

# 拟合线 (使用 r"" 原始字符串，并简化公式显示)
fit_eq = f"V_H = {slope:.4f} * I_s {'+' if intercept>0 else ''}{intercept:.4f}"
plt.plot(Is, fit_line, color='#1f77b4', linestyle='-', linewidth=2, label=f'线性拟合: {fit_eq}')

# 标注文字统一使用 fontproperties 参数
plt.title('实验二：霍尔电压 V_H 与工作电流 I_s 的关系', fontproperties=prop, fontsize=14, pad=15)
plt.xlabel('工作电流 I_s (mA)', fontproperties=prop, fontsize=12)
plt.ylabel('霍尔电压 V_H (mV)', fontproperties=prop, fontsize=12)

# 统计信息框 (避免使用容易报错的 LaTeX 符号，改用常用字符)
stats_text = (f"决定系数 R² = {r_square:.5f}\n"
              f"拟合斜率 a = {slope:.4f} mV/mA\n"
              f"磁场强度 B ≈ 2427.5 μT")

plt.gca().text(0.05, 0.95, stats_text, transform=plt.gca().transAxes, 
               fontproperties=prop, fontsize=11, verticalalignment='top',
               bbox=dict(boxstyle='round', facecolor='white', alpha=0.9, edgecolor='#cccccc'))

plt.legend(prop=prop, loc='lower right', frameon=True)
plt.tight_layout()
plt.show()

# 控制台输出填表数据
print(f"拟合斜率 a = {slope:.6f}")
print(f"决定系数 R^2 = {r_square:.6f}")