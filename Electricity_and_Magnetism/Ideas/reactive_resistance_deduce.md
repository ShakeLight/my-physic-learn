# 交流电路分析：基于相量变换的阻抗与时域模型
电路中阻抗是定量计算元件对电流阻碍作用的物理量。如图，![](https://files.mdnice.com/user/146284/989e62e7-976f-4b66-9cfe-f2428458c07f.png)
在纯电阻电路中，电路阻抗等于电阻之和
$$X=R_1+R_2+R_3$$
但是如果电路中还存在电感和电容呢？
我们该如何计算含电感、电容电路的阻抗呢？
## 电感的时域微分分析
![](https://files.mdnice.com/user/146284/1f758137-4770-4193-ba4d-d63264c773dd.png)
![](https://files.mdnice.com/user/146284/70283387-7fc8-4b0c-bcff-a9c14c83e17f.png)
*电容器（上） 电感器（下）*

当电流 $i$ 流经电感线圈时，在空间中激发出磁场。此时磁感应强度与电流 $i$ 成正比，电感 $L$ 为比例系数：$ \Phi = L \cdot i$. 这时改变电流$ i$，磁通量 $\Phi$ 随之改变，磁场的变化在线圈内部感应一个感应电场。这个感应电场会产生其感应电动势 $e_L$，根据法拉第定律

$$e_L = -\frac{d\Phi}{dt} = -L \frac{di}{dt}$$

该公式的负号意味着感应电动势总与电流方向相反，对电流起阻碍作用。

在交流电路中，给电感施加正弦波电流
$$i(t)=Asin(\omega t)$$
根据电感的物理特性，其电压正比于电流的变化率
$$u(t)=L\frac{di}{dt}$$
将电流公式代入计算得
$$u_L(t) = L \frac{d}{dt} [A \sin(\omega t)] = L \cdot A \cdot \omega \cos(\omega t)$$
为明显对比相位，这里用诱导公式将电流写回余弦形式
$$i(t)=Asin(\omega t)=Acos(\omega t -\frac{\pi}{2})$$


对比发现，电压在相位上领先电流$\pi/2$。因为电能与磁场能的转化不是瞬时进行的，宏观上产生相位延迟。

联立刚才所得到的电感相关方程可得
$$ 
\begin{cases}
u_L(t)=L \cdot A \cdot \omega  \cos(\omega t)\\
i_L(t)=Acos(\omega t-\frac{\pi}{2})
\end{cases}
$$
但是感抗并不是电压与电流的简单相除，两者之间存在相位差，比值不是一个固定的数。感抗反应电感对电流的阻碍效果，是一个固定标量，而电感的定义是电压与电流的振幅或有效值之比
$$X_L=\frac{u_m}{i_m}$$
结合上文方程组，我们可以直接得到感抗计算公式
$$X_L=\frac{u_m}{i_m}=\frac{L \cdot A \cdot \omega  }{A}=\omega \cdot L$$
这里引入一个更高级的计算工具——相量化（Phasor），这个工具会使你在后续处理复杂的动态系统分析和相位振幅分析时更加优雅，这就是后话了。相量化的核心操作是引入了复数，复数的模存放振幅，幅角存放相位。通过欧拉公式
$$e^{j\theta} = \cos \theta + j \sin \theta$$
将正余弦信号转化成指数运算，巧妙地规避了复杂的三角变换运算。并且由于
$$\frac{d}{dt} [A e^{j(\omega t + \phi)}] = j\omega \cdot [A e^{j(\omega t + \phi)}]$$
的优良性质，$\frac{d}{dt}$变成了$ \cdot j\omega$,$\int dt$变成了$/j\omega$，于是复杂的微分式变成了简单的乘除法运算，大大较少了计算难度。 言归正传，我来演示用相量化处理上文方程组。套用欧拉公式将$u_L(t)$、$i_L(t)$代入实部
$$ 
\begin{cases}
L \cdot A \cdot\omega e^{j\omega t}=L \cdot A \cdot \omega [ \cos(\omega t)+j \sin(\omega t)]\\
A e^{j(\omega t -\frac{\pi}{2})}=A[cos(\omega t-\frac{\pi}{2})+j \sin(\omega t-\frac{\pi}{2})]
\end{cases}
$$
因为我们在同一电路内分析，在同频率的稳定状态下，我们将旋转因子 $e^{j \omega t}$ 忽略，得
$$
\begin{cases}
\dot{U} = (LA\omega) \angle 0^\circ = (LA\omega) e^{j0^\circ} = LA\omega\\
\dot{I} = A \angle -90^\circ = A e^{-j90^\circ} = -jA
\end{cases}
$$
这时我们计算复阻抗
$$Z_L = \frac{\dot{U}}{\dot{I}} = \frac{LA\omega}{-jA} = \frac{L\omega}{-j}$$
分子分母同乘$j$,得
$$Z_L = \frac{j \cdot L\omega}{-j^2} = \frac{j\omega L}{1} = j\omega L$$
即求得电感的**感抗计算公式**。细心的读者会发现这个公式结果比之前推导的多一个 $j$.这个无需在意，非理想情况下，电感总是带有电阻的。为了区分和方便运算电阻与电抗，于是将电抗统一放在虚部。

现实总是充满缺憾的，没有电阻的电感只存在于理想。现实中的电子元件的阻抗往往由电阻和电抗组成
$$Z_L=Z e^{j \varphi}=Z \cos \varphi +j \cdot Z \sin \varphi$$
$$
r=Re(Z_L)=Z \cos \varphi;x=Im(Z_L)=Z \sin \varphi
$$
电阻 $r$是阻抗的实部，负责消耗能量。电抗 $x$是阻抗的虚部，负责存储和交换能量。而电抗元件的作用是实现能量在电能与磁场能之间周期性存储和释放。  


在无线电电子技术领域，电抗元件(电感，电容)的重要应用之一就是组成谐振电路，谐振电路利用电抗元件存储，转换能量的作用，所以我们希望，电抗元件的各种能量损耗越少越好，也就是$P_{有功功率}$越小，而存储转换能量的能力越强越好，$P_{无功功率}$越大，这里我们引入品质因数$Q$来标志电抗品质好坏
$$Q=\frac{P_{无功功率}}{P_{有功功率}}$$
假设存在交流电路，它的电流与电压都是正弦波，相量化后记为
$$
\begin{cases}
\dot{U}=Ue^{j\theta_u}\\
\dot{I}=Ie^{j\theta_i}
\end{cases}
$$
我们将交流电路的复功率记为：$\tilde{S}=\dot{U} \cdot \overline{\dot{I}}$。(乘以电流的共轭复数得以计算两初相位的相位差,直接相乘无物理意义)
$$\tilde{S}=\dot{U} \cdot \overline{\dot{I}}=U \cdot Ie^{j(\theta_u -\theta_i)}=U \cdot Ie^{j \varphi}=U \cdot I(\cos \varphi+ j \sin \varphi)$$
 $$P_{有功功率}=\text{Re}(\tilde{S}) = UI \cos \varphi$$
 $$P_{无功功率}=\text{Im}(\tilde{S}) = UI \sin \varphi$$
 把上面两式代入Q值计算公式，立刻得到
 $$Q=\frac{P_{无功功率}}{P_{有功功率}}=\frac{\sin \varphi}{\cos \varphi}$$
 注意到上文提及电阻$r$、电抗$x$公式，得
 $$Q=\frac{\sin \varphi}{\cos \varphi}=\frac{x}{r}$$
 
 ## 电容的时域微分分析
 电容接入电路后，电压驱动电容两端电极板的电荷再分配，使两端电极板呈电极性，电极板中间区域产生电场。与电感不同，电容实现能量在电能与电场能之间的转化。  
 经过上文的铺垫，电容容抗的公式推导就变得容易很多了，读者可以自己动笔推导后再对照本文。
 给电容两端施加正弦电压$u_C(t)=A\sin \omega t$。
 对电容基本公式两侧求导得
 $$i_C(t)=\frac{dq}{dt}=C \frac{dU}{dt}$$
 代入电压表达式得
 $$i_C(t)= \omega CA \cos \omega t$$
 对式子进行相量化处理则有
 $$
 \begin{cases}
 \dot{U}=Ae^{-j90^\circ}=-jA\\
 \dot{I}=\omega C Ae^{j0^\circ}=\omega CA
 \end{cases}
 $$
 可得
 $$X_C=\frac{\dot{U}}{\dot{I}}=-\frac{j}{\omega C}$$
 
 RLC电路是电子工程中最基础且应用广泛的电路模型之一，它在射频通信、信号处理等领域发挥关键作用。后续我将结合大学物理实验，为大家讲解RLC谐振电路的运行原理与其在无线电领域的重要应用，我们下期再会！
 

 PS.作者也是刚刚接触这方面的知识，很多内容是边写边学，只能尽量用通俗易懂的语言把前人的理论复述一遍，如有错误，在此提前道歉，请大家多多指正，愿与大家共同进步！