import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

fig, axs = plt.subplots(2,2)
data = np.random.randint(0,20,40)

for row in (0,1):
	for col in (0,1):
		sns.distplot(data, kde=row, norm_hist=col, ax=axs[row, col])

axs[0,0].set_ylabel('NO kernel density')
axs[1,0].set_ylabel('KDE on')
axs[1,0].set_xlabel('norm_hist=False')
axs[1,1].set_xlabel('norm_hist=True')