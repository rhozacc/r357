# coding=utf-8

import matplotlib.pyplot as plt 


text = """
insert text here. 
"""


sentences = text.split(". ")
lengths = [len(s) for s in sentences]

plt.figure()
plt.plot(lengths)
plt.show();
