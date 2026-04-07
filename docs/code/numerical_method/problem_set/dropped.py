import numpy as np
import matplotlib.pyplot as plt

# 输入参数
h = float(input("Enter the height of the tower: "))
t = float(input("Enter the time interval: "))

# 物理常数
g = 9.81

# 计算指定时刻的位置
s = g * t**2 / 2
position = h - s

# 生成完整轨迹（从0到落地时间）
t_max = np.sqrt(2 * h / g)  # 落地时间
t_trajectory = np.linspace(0, t_max, 100)
y_trajectory = h - 0.5 * g * t_trajectory**2
y_trajectory = np.maximum(y_trajectory, 0)  # 落地后保持为0

# 绘图
plt.figure(figsize=(10, 6))
plt.plot(t_trajectory, y_trajectory, 'b-', linewidth=2, label='Trajectory')
plt.plot(t, position, 'ro', markersize=8, label=f'Ball at t = {t}s')
plt.axhline(y=0, color='k', linestyle='--', alpha=0.5, label='Ground')

# 标注
plt.text(t, position, f'  Height: {position:.2f}m', fontsize=10, verticalalignment='bottom')
plt.text(t_max/2, h/2, f'g = {g} m/s²', fontsize=12, bbox=dict(boxstyle="round", facecolor='wheat'))

plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.title('Free Fall from Tower')
plt.grid(True, alpha=0.2)
plt.legend()
plt.xlim(0, t_max * 1.05)
plt.ylim(-1, h * 1.05)

print(f"\nAt t = {t}s:")
print(f"  Fall distance: {s:.2f} m")
print(f"  Height above ground: {position:.2f} m")
print(f"  Time to hit ground: {t_max:.2f} s")

plt.show()