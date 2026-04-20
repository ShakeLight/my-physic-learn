![GitHub language count](https://img.shields.io/github/languages/count/ShakeLight/my-physic-learn)
![GitHub last commit](https://img.shields.io/github/last-commit/ShakeLight/my-physic-learn)
# Lab of General Physics
# 物理实验与计算物理 (Physics Lab & Computational Physics) 

本项目用于存放北京师范大学开设的普通物理实验课程的实验报告、原始数据及配套的 Python 数据处理脚本。旨在通过版本控制（Git）实现实验数据的科学管理，并借此学习 linux 控制语言。

##   仓库导航 (Navigation)

### [Electromagnetism (电磁学)](./Electricity_and_Magnetism)
* **[RC & RLC Transient Response](./Electricity_and_Magnetism/LAB/LAB_rc_rlc_transient_response)**: 研究电路在激励信号下的暂态性质。
* **[RLC Resonance Steady State](./Electricity_and_Magnetism/LAB/LAB_rc_rlc_transient_response)**: 测量谐振曲线，计算谐振频率 $f_0$ 与品质因数 $Q$与R、L、C之间的关系。
* **[Hall Effect Sensor](./Electricity_and_Magnetism/LAB/LAB_hall_effect_sensor)**: 利用霍尔效应探究磁感应强度 $B$等。
* **[Reactive Resistance Deduce](./Electricity_and_Magnetism/Ideas/reactive_resistance_deduce.md)**: **科普文**  交流电路分析：基于相量变换的阻抗与时域模型 。
* **[Millikan OilDrop for Measuring Elementary charge](./Electricity_and_Magnetism/LAN/LAB_millikan_oildrop_elementary_charge)** :利用密里根油滴法测量油滴的电荷量并探究电荷分立的量子化特征。
### [Optics(光学)](./Optics)
* **[Fresnel Biprism Interference](./Optics/LAB_Fresnel_Biprism_Interference)**:基于菲涅尔双棱镜研究双光束干涉。
* **[Dispersion Curve of Glass Measured by Spetrometer](./Optics/LAB_DispersionCurve_Measure_spectrometer)**:使用分光计测量玻璃的色散曲线。
##   核心实验逻辑 (Core Physics Logic)

### 1. RLC 谐振拟合
实验中使用信号发生器改变频率 $f$，记录电压 $U_R$。我们采用非线性最小二乘法对幅频特性曲线进行拟合：
$$I(\omega) = \frac{U_0}{\sqrt{R^2 + (\omega L - \frac{1}{\omega C})^2}}$$

### 2. 霍尔效应测量
通过改变工作电流 $I_s$ 和励磁电流 $I_M$，验证线性关系：
$$V_H = R_H \frac{I_s B}{d}$$

### 2.密里根油滴法测电荷量

---

##   工具链与运行说明 (Tools)
请注意： **本仓库的大部分内容在Gemini的协助下完成**
本仓库的代码部分主要基于 **Python 3** 开发，使用了以下科学计算库：
* **NumPy**: 矩阵运算与数据预处理。
* **SciPy**: 使用 `curve_fit` 进行物理参数拟合。
* **Matplotlib**: 绘制符合学术规范的实验图像。

**如何运行拟合脚本：**
```bash
# 进入对应目录
cd /Electricity_and_Magnetism
# 运行 Python 脚本
python rlc_fitting.py
