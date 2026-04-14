import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# ================= 1. 录入实验数据 (Table 3) =================
f_khz = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 
                  2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 25.0, 30.0, 45.0])
f_hz = f_khz * 1e3

# 使用归一化后的数据 κ * UR/U
gain_exp = np.array([0.031212, 0.061925, 0.093158, 0.124160, 0.155701, 
                     0.188671, 0.216649, 0.247519, 0.27963, 0.311178, 
                     0.595357, 0.822786, 1.002401, 1.010849, 0.996770, 
                     0.951233, 0.889317, 0.545071, 0.268110, 0.165331])

# 相位数据
phase_exp = np.array([-88, -85, -84, -82.0, -80.9, -79.3, -77.5, -75.6, -74.3, -72.5, 
                      -53.8, -35.5, -18.72, -2.7, 10.24, 20.73, 28.84, 57.98, 75.1, 81.2])

# ================= 2. 修正模型函数 =================
def amplitude_model(f, f0, Q, A):
    return A / np.sqrt(1 + Q**2 * (f/f0 - f0/f)**2)

def phase_model(f, f0, Q, phi_offset):
    # 根据你的数据走势，符号调整为从负到正
    return np.degrees(np.arctan(Q * (f/f - f0/f))) + phi_offset

# ================= 3. 执行拟合 (增加限制以确保 Q 为正) =================
# p0: [f0, Q, A/offset], bounds: (下限, 上限)
popt_amp, _ = curve_fit(amplitude_model, f_hz, gain_exp, p0=[5100, 6, 1.0], bounds=(0, [10000, 100, 2]))
popt_phase, _ = curve_fit(phase_model, f_hz, phase_exp, p0=[5100, 6, 0])

# ================= 4. 理论参数更新 (C = 0.1uF) =================
L = 9.481e-3
C = 0.1e-6 # 修正为 0.1uF
R_total = 501.943
f0_theory = 1 / (2 * np.pi * np.sqrt(L * C))
Q_theory = (1 / R_total) * np.sqrt(L / C)

f_smooth = np.logspace(2, 5, 1000)
gain_theory = amplitude_model(f_smooth, f0_theory, Q_theory, 1.0)
# 理论相位也按你的测量习惯调整符号
phase_theory = np.degrees(np.arctan(Q_theory * (f_smooth/f0_theory - f0_theory/f_smooth)))

# ================= 5. 绘图 =================
plt.figure(figsize=(10, 8))

# 幅频图
plt.subplot(2, 1, 1)
plt.semilogx(f_hz, gain_exp, 'ro', label='Data (Table 3)')
plt.semilogx(f_smooth, amplitude_model(f_smooth, *popt_amp), 'b-', label=f'Fit (Q={popt_amp[1]:.2f}, f0={popt_amp[0]/1e3:.2f}k)')
plt.semilogx(f_smooth, gain_theory, 'g--', label=f'Theory (C=0.1uF, f0={f0_theory/1e3:.2f}k)')
plt.ylabel('Normalized Gain')
plt.legend()
plt.grid(True, which="both", alpha=0.3)

# 相频图
plt.subplot(2, 1, 2)
plt.semilogx(f_hz, phase_exp, 'ro', label='Data (Table 3)')
plt.semilogx(f_smooth, phase_model(f_smooth, *popt_phase), 'b-', label=f'Fit (Q={popt_phase[1]:.2f})')
plt.semilogx(f_smooth, phase_theory, 'g--', label='Theory (C=0.1uF)')
plt.ylabel('Phase (Deg)')
plt.xlabel('Frequency (Hz)')
plt.legend()
plt.grid(True, which="both", alpha=0.3)

plt.tight_layout()
plt.show()

print(f"理论 Q: {Q_theory:.2f}, 拟合 Q: {popt_amp[1]:.2f}")