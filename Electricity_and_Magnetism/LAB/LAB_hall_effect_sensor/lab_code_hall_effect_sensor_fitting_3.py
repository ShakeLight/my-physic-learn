import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# --- 1. 数据输入 ---
x = np.array([-48, -42, -36, -30, -24, -18, -12, -6, 0, 6, 12, 18, 24, 30, 36, 42, 48, 54])
# 这里的 B 值请根据你的计算结果替换，以下为根据 U++ 趋势估算的示例值
B = np.array([215, 222, 228, 233, 236, 239, 241, 241, 242, 241, 241, 241, 241, 241, 241, 239, 238, 236])

# --- 2. 均匀区计算 ---
B0 = B[x == 0][0] # 中心磁场值
thresholds = [0.05, 0.10, 0.20]
colors = ['#2ca02c', '#ff7f0e', '#d62728']
uniform_zones = {}

for t in thresholds:
    within_range = x[np.abs((B - B0) / B0) <= t]
    uniform_zones[t] = (np.min(within_range), np.max(within_range))

# --- 3. 绘图 ---
font_path = 'C:/Windows/Fonts/msyh.ttc' 
prop = fm.FontProperties(fname=font_path)
plt.figure(figsize=(10, 6), dpi=100)

plt.plot(x, B, 'bo-', markersize=5, label='实测磁场分布')
plt.axhline(y=B0, color='gray', linestyle='--', alpha=0.5)

# 标注均匀区
for i, t in enumerate(thresholds):
    x_min, x_max = uniform_zones[t]
    plt.axvspan(x_min, x_max, color=colors[i], alpha=0.1, label=f'{int(t*100)}% 均匀区')
    plt.annotate(f'{int(t*100)}%: [{x_min}, {x_max}]mm', xy=((x_min+x_max)/2, B0 - (i+1)*5), 
                 ha='center', fontproperties=prop, color=colors[i], weight='bold')

plt.title('实验三：亥姆霍兹线圈轴向磁场分布', fontproperties=prop, fontsize=14)
plt.xlabel('位置 x (mm)', fontproperties=prop, fontsize=12)
plt.ylabel('磁感应强度 B (μT)', fontproperties=prop, fontsize=12)
plt.legend(prop=prop, loc='lower center', ncol=2)
plt.grid(True, linestyle=':', alpha=0.6)
plt.show()