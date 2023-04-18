import seaborn as sns
import matplotlib.pyplot as plt
from numpy import random

x = random.binomial(n=100, p=0.5, size=10)

print(x)


# sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=True)
# plt.show()


sns.distplot(random.normal(loc=50, scale=5, size=1000),
             hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000),
             hist=False, label='binomial')

plt.show()
