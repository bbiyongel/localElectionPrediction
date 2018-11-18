# -*- coding: utf-8 -*- 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_path = "C:/Windows/Fonts/NanumBarunGothic.ttf"
font_name = font_manager.FontProperties(fname = font_path).get_name()
print(font_name)
rc('font', family = font_name)

file = open("/Users/YOUNG/Desktop/test_src", "r", encoding='utf-8')
lines = file.readlines()
file.close()

new_lines = []
chart_x = []
chart_y = []

# 
for line in lines:
  new_lines.append(line[1:-2].replace(',',' ').replace('\'',' ').split())


for i in range(0,10):
  chart_x.append(str(new_lines[i][1]))
  chart_y.append(int(new_lines[i][0]))

print(chart_x)
print(chart_y)

# 의미있는 가장 높은 빈도수의 10개 단어만 표현
index = np.arange(10)

plt.bar(index, chart_y, tick_label = chart_x, align='center')


plt.xlabel('단어')
plt.ylabel('빈도수')
plt.title('선거철에 가장 등장 빈도수가 높은 단어들')
plt.xlim(-1, 10)
plt.ylim(0, 400)
plt.show()




