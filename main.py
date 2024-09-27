import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
font_path = "C:/Windows/Fonts/malgun.ttf"
font_prop = fm.FontProperties(fname=font_path, size=14)
j = 5  # 회전 관성
c = 4  # 댐퍼 계수
k = 3  # 스프링 상수
A = 1  # 초기 각도 (변위)
B = 0  # 초기 각속도
t = np.linspace(0, 10, 100)  # 시간 범위
omega_d = np.sqrt(k/j - (c/(2*j))**2)  # 감쇠 주파수 계산
theta = np.exp(-c/(2*j) * t) * (A * np.cos(omega_d * t) + B * np.sin(omega_d * t))  # 변위 계산

plt.figure(figsize=(10, 6))
plt.plot(t, theta, color='b', linewidth=2, label='각도 변위 (θ)')
plt.title('감쇠 진동 운동', fontproperties=font_prop, fontsize=16)
plt.xlabel('시간 (s)', fontproperties=font_prop, fontsize=14)
plt.ylabel('각도 (θ)', fontproperties=font_prop, fontsize=14)
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(prop=font_prop)
plt.xlim(0, 10)
plt.ylim(-1.5, 1.5)

plt.annotate('진동 감쇠 시작', xy=(0, 1), xytext=(1, 1.2),
             arrowprops=dict(facecolor='black', shrink=0.05), fontproperties=font_prop)
plt.annotate('진동이 감소함', xy=(5, 0.5), xytext=(6, 0.8),
             arrowprops=dict(facecolor='black', shrink=0.05), fontproperties=font_prop)

plt.show()
