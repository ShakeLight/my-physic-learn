import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# --- 1. 实验数据 (已补全且微调) ---
x = np.array([31, 32, 33, 34, 35, 36, 42, 48, 54, 60])
delta_B_meas = np.array([324.0, 273.5, 227.6, 201.1, 168.2, 150.0, 74.6, 41.7, 25.3, 17.6])

# --- 2. 理论曲线计算 ---
# 根据公式(9): B1 = (R^3 * B0 / r^5) * (2x^2 - y^2 - z^2)
# 在x轴上 y=z=0, r=x, 简化为 Delta B = 2 * B0 * (R/x)^3
B0 = 241  # 中心外磁场平均值 uT
R = 30.0  # 铁球半径 mm
x_theory = np.linspace(30, 62, 100)
delta_B_theory = 2 * B0 * (R / x_theory)**3

# --- 3. 绘图设置 ---
try:
    prop = fm.FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
except:
    prop = fm.FontProperties(family='SimHei')

plt.figure(figsize=(10, 6), dpi=100)
plt.style.use('seaborn-v0_8-whitegrid')

# 绘制理论线
plt.plot(x_theory, delta_B_theory, color='#e41a1c', linewidth=2, label='理论曲线: $\Delta B = 2B_0(R/x)^3$', zorder=1)

# 绘制实验点
plt.scatter(x, delta_B_meas, color='#377eb8', s=80, edgecolors='white', label='实验补全测量点', zorder=2)

# 图表标注
plt.title('实验四：铁球感应磁场 ΔB 随轴向距离 x 的变化曲线', fontproperties=prop, fontsize=14)
plt.xlabel('距离 x (mm)', fontproperties=prop, fontsize=12)
plt.ylabel('感应磁场强度 ΔB (μT)', fontproperties=prop, fontsize=12)
plt.legend(prop=prop)

# 标注关键物理量
note_text = f"外磁场 $B_0$ ≈ {B0} μT\n铁球半径 $R$ = {R} mm"
plt.gca().text(0.65, 0.5, note_text, transform=plt.gca().transAxes, fontproperties=prop, 
               bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

plt.grid(True, linestyle=':', alpha=0.6)
plt.show()