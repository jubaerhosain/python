import seaborn as sns
import matplotlib.pyplot as plt
from numpy import random

x = random.uniform(size=(2, 3))

print(x)


sns.distplot(random.uniform(size=1000), hist=False)

plt.show()
