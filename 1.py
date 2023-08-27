####################################################
#                                                  #
#                                                  #
#                     Box plot                     #
#                                                  #
#                                                  #
####################################################
import matplotlib.pyplot as plt
p_0 =  [0.175,0.125,0.100,0.150,0.150,0.150,0.113,0.163,0.150,0.163]

p_5 =  [0.150,0.213,0.175,0.150,0.150,0.150,0.175,0.163,0.313,0.138]
p_55 = [0.150,0.063,0.188,0.250,0.200,0.175,0.088,0.138,0.125,0.138]

p_10 = [0.388,0.286,0.263,0.350,0.275,0.225,0.175,0.188,0.213,0.350]
p_1010 = [0.200,0.210,0.213,0.175,0.250,0.180,0.200,0.138,0.300,0.250]

p_30 = [0.525,0.575,0.613,0.688,0.438,0.600,0.413,0.450,0.875,0.513]
p_3030 = [0.500,0.490,0.475,0.488,0.500,0.488,0.338,0.463,0.763,0.450]

p_45 = [0.750,0.750,0.700,0.750,0.750,0.850,0.738,0.788,0.838,1.000]
p_4545 = [0.725,0.788,0.725,0.838,0.638,0.750,0.788,0.725,0.850,0.975]

plt.figure(figsize=(10, 6), dpi=700)
color_list = ['cadetblue','steelblue', 'lightpink', 'steelblue', 'lightpink', 'steelblue', 'lightpink', 'steelblue', 'lightpink']
figs = plt.boxplot([p_0, p_5, p_55, p_10, p_1010, p_30, p_3030, p_45, p_4545], patch_artist=True,
                   positions=[1, 2,2.4, 3.4,3.8, 4.8,5.2, 6.2,6.6], widths=0.3)
plt.ylabel("REASR", fontsize=20)
plt.xlabel("Poison rate(%)", fontsize=20)
for box, c in zip(figs['boxes'], color_list):
    box.set(color=c, linewidth=2)
    box.set(facecolor=c)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
city =['0', '5', '10', '30', '45']
plt.xticks([1, 2.2, 3.6, 5, 6.4], city, fontsize=20)

labels = ["Baseline clean model", "Baseline BD model","BD model with TS"]
plt.legend(figs['boxes'], labels, fontsize=20)
#plt.savefig("./figs/REASR.pdf", bbox_inches='tight', pad_inches=0.1)
plt.savefig("./figs/REASR.pdf")
plt.show()
####################################################
#                                                  #
#                                                  #
#                     折线图                        #
#                                                  #
#                                                  #
####################################################
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
x_axis_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
clean = [0.188, 0.200, 0.175, 0.213, 0.175, 0.188, 0.175, 0.200, 0.163, 0.188]
backdoor = [0.950, 0.888, 0.988, 0.988, 0.938, 0.925, 0.955, 0.875, 0.950, 0.975]
TS = [0.988, 0.963, 0.913, 0.963, 0.975, 0.975, 0.920, 0.975, 0.950, 0.955]
LC = [0.350, 0.225, 0.225, 0.175, 0.188, 0.213, 0.250, 0.550, 0.338, 0.750]
TS_LC = [0.238, 0.250, 0.213, 0.200, 0.213, 0.200, 0.235, 0.200, 0.188, 0.225]
# 画图
plt.figure(figsize=(10, 6), dpi=700)
plt.plot(x_axis_data, clean, 'b*-', alpha=0.5, linewidth=2, label='Baseline Clean model')
plt.plot(x_axis_data, backdoor, 'rs-', alpha=0.5, linewidth=2, label='Baseline BD model')
plt.plot(x_axis_data, TS, 'go-', alpha=0.5, linewidth=2, label='BD model with TS')
plt.plot(x_axis_data, LC, 'y1-', alpha=0.5, linewidth=2, label='BD model with LC')
plt.plot(x_axis_data, TS_LC, 'c+-', alpha=0.5, linewidth=2, label='BD model with TS and LC')
# 控制x轴刻度间隔
x_major_locator = MultipleLocator(1)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
#plt.legend(loc='best', bbox_to_anchor=(0.5, 0.7), fontsize=16)
plt.legend(loc='best', fontsize=16)
plt.xlabel('Model', fontsize=20)
plt.ylabel('Max REASR', fontsize=20)
plt.savefig('./figs/max reasr.pdf')
plt.show()


####################################################
#                                                  #
#                                                  #
#                     bar plot                     #
#                                                  #
#                                                  #
####################################################
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1.2453007, 2.5867524, 0.7884415, 1.337854, 0.953327]
hatch_par = ['/', '', '|', 'x', '、']
plt.figure(figsize=(10, 6), dpi=700)
color = ['gainsboro', 'gray',  'gainsboro', 'gainsboro', 'gainsboro']
x_label = ['Clean model\n Baseline', 'BD model\n Baseline', 'BD model\n PR=0.01', 'BD model\n PR=0.1', 'BD model\n PR=0.3']
plt.ylabel('Anomaly Index', fontsize=20)
plt.xticks(x, x_label, rotation=35, fontsize=20)
plt.yticks(fontsize=20)
for i in range(5):
    plt.bar(x[i], y[i], color=color[i], hatch=hatch_par[i], linewidth=2.0, width=0.4)
for a, b in zip(x, y):
    plt.text(a, b, '%.2f' % b, ha='center', va='bottom', fontsize=16)
plt.axhline(y=2.0, linewidth=2, color='k', linestyle='--')
plt.savefig("./figs/NC bar.pdf", bbox_inches='tight', pad_inches=0.1)
plt.show()


####################################################
#                                                  #
#                                                  #
#                     散点图                        #
#                                                  #
#                                                  #
####################################################
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
# 第一组散点
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([3.88, 2.82, 3.72, 2.20, 2.59, 4.34, 6.41, 4.55, 3.77, 4.89])
y1 = np.array([53.22, 30.20, 70.91, 48.89, 89.02, 90.94, 64.99, 43.35, 78.78, 56.26])
plt.figure(figsize=(10, 6), dpi=700)
plt.scatter(x, y, s=50, c='blue', alpha=1, marker='o', label='BD model with TS, LC and AC')  # s 点的大小  c 点的颜色 alpha 透明度
plt.scatter(x, y1, s=50, c='red', alpha=1, marker='v', label='BD model with TS and LC')
# 控制x轴刻度间隔
x_major_locator = MultipleLocator(1)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.axhline(y=8, linewidth=1, color='k', linestyle='--', label='Threshold')
#plt.xlim((-5, 5))
plt.ylim((0, 140))
plt.legend(loc="upper left", fontsize=20)
plt.ylabel('RMMD', fontsize=20)
plt.xlabel('label', fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

#plt.savefig("./figs/Bea.pdf", bbox_inches='tight', pad_inches=0.2)
plt.savefig("./figs/Bea.pdf")
plt.show()
