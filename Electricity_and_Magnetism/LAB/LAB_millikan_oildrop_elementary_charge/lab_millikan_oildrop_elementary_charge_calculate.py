import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import matplotlib as mpl
t1=float(input("t_g1="))
t2=float(input("t_g2="))
t3=float(input("t_e1="))
t4=float(input("t_e2="))
te=(t3+t4)/2
u=float(input("u="))
tg=(t1+t2)/2
v_g=(5e-4)/tg
v_e=(5e-4)/te
u0=(v_g*u)/(v_g+v_e)
a0=math.sqrt(8.57e-9*v_g)
a=a0-4.06e-8
q=(201.4*a**3)/u0
n=q/1.602e-19
print(f"电荷量为{q*10**-2},n为{n*10**-2}")