import matplotlib
from matplotlib import pyplot as plt
#通过 Matplotlib，开发者可以仅需要几行代码，便可以生成绘图，直方图，功率谱，条形图，错误图，散点图等。
# 显示中文
# 配置字体
matplotlib.rcParams['font.sans-serif'] = ['simhei']
matplotlib.rcParams['font.family'] = 'sans-serif'

# 画线
# plt.plot([1,2], [3,5])
# plt.plot([1,3,7], [2,5,8])
# plt.plot([1,3,7], [2,5,8], '--')  # 虚线
# xy轴文字
plt.xlabel('x轴')
plt.ylabel('y轴')

# 参数x：x轴位置
# 参数height：高度
# 参数width：默认0.8
plt.bar([1], [123], label='bj')
plt.bar([2], [200], label='bj')
plt.bar([3], [245], label='sz')

plt.legend()  # 绘制

plt.show() # 显示
# plt.savefig('line') # 保存图片