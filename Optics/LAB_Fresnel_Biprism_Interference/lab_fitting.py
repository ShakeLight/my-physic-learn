import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# --- 1. 数据对齐 (严格取自 image_a16c6a.png) ---
# 原始像素读数 x_pix
factor=3.45e-6
x_pix=[55,138,225,301,388,471,550,625,709,792,875,954,1037,1121,1200,1283,1366,1445,1529,1612]
pixels = np.array(x_pix)

# 级数 i (1 to 20)
order = np.arange(1, 21)

# 单位转换: 1 pixel = 3.45 um = 0.00345 mm
# 转换后的实际距离 y_mm (mm)
y = pixels * factor

# --- 2. 线性拟合与不确定度计算 (根据讲义第143页算法) ---
def model(x, k, b):
    return k * x + b

# popt: [k, b], pcov: 协方差矩阵
popt, pcov = curve_fit(model, order, y)
k, b = popt
# 参数标准不确定度 u(k), u(b)
perr = np.sqrt(np.diag(pcov))
uk, ub = perr[0], perr[1]

# 统计量计算
residuals = y - model(order, *popt)
w_star = np.sum(residuals**2)  # 残差平方和 (W*)
ss_tot = np.sum((y- np.mean(y))**2)
r_squared = 1 - (w_star / ss_tot)

# --- 3. 学术风格绘图 (无中文干扰，解决乱码) ---
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 11,
    "mathtext.fontset": "stix", # 采用类似 LaTeX 的字体
    "xtick.direction": "in",
    "ytick.direction": "in",
    "axes.grid": True,
    "grid.linestyle": "--",
    "grid.alpha": 0.5
})

fig, ax = plt.subplots(figsize=(8, 6), dpi=150)

# 数据点与拟合线
ax.scatter(order, y, color='black', marker='s', s=20, label='Experimental Data', zorder=3)
ax.plot(order, model(order, k, b), color='darkred', lw=1.5, label='Linear Fit', zorder=2)

# 标注文字内容 (学术严谨格式)
fit_info = (
    r"$\mathbf{Fitting\ Results}$" + "\n"
    r"Eq: $y = k \cdot i + b$" + "\n"
    f"$k$ ($\Delta x$): ${k:.6f} \pm {uk:.6f}$ m\n"
    f"$b$: ${b:.5f} \pm {ub:.5f}$ m\n"
    f"$W^*$: ${w_star:.4e}$ $\mathrm{{m^2}}$\n"
    f"$R^2$: ${r_squared:.9f}$"
)

# 使用文本框展示参数
props = dict(boxstyle='round', facecolor='white', alpha=0.9, edgecolor='gray')
ax.text(0.05, 0.95, fit_info, transform=ax.transAxes, verticalalignment='top', bbox=props)

# 坐标轴标签 (使用英文以避免乱码，符合学术惯例)
ax.set_xlabel(r"Order of Interference Fringes ($i$)")
ax.set_ylabel(r"Position $x_i$")
ax.set_title("Linear Fit of Fresnel Biprism Interference Fringes", fontsize=13, pad=15)
ax.legend(loc='lower right')

plt.tight_layout()
plt.show()

# 命令行输出精确数值
print(f"Slope (Fringe Spacing Delta x): {k:.7f} ")
print(f"Uncertainty u(k): {uk:.7e} ")
print(f"R-squared: {r_squared:.12f}")