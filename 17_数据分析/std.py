# _*_ coding : utf-8 _*_
# @Time : 2024/6/15 16:37
# @Author : chalet.you
# @File : std
# @Project : bigdata_python_course
import matplotlib.pyplot as plt
import numpy as np

# 成绩数据
scores = [82, 85, 90, 95, 100, 103, 110, 115, 126, 125]

# 计算平均值、方差和标准差
mean_score = np.mean(scores)
variance_score = np.var(scores)
std_dev_score = np.std(scores)

# 绘制图形
plt.figure(figsize=(10, 6))
plt.plot(scores, 'o-', label='Scores')
plt.axhline(mean_score, color='r', linestyle='--', label=f'Mean: {mean_score:.2f}')
plt.fill_between(range(len(scores)), mean_score - std_dev_score, mean_score + std_dev_score, color='g', alpha=0.2, label=f'Standard Deviation: {std_dev_score:.2f}')
plt.title('Class Language Scores Distribution')
plt.xlabel('Student')
plt.ylabel('Score')
plt.legend()
plt.grid(True)
plt.show()
