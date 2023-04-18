import seaborn as sns
import matplotlib.pyplot as plt
from numpy import random

x = random.chisquare(df=2, size=(2, 3))

print(x)

sns.distplot(random.chisquare(df=1, size=1000), hist=False)

plt.show()
