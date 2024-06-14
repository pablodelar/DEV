import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# np.random.seed(0)
# values = np.random.randn(100) # array of normally distributed random numbers
# s = pd.Series(values) # generate a pandas series
# s.plot(kind='hist', title='Normally distributed random values') # hist computes distribution
# plt.show()

# Basic method to create a Series
l = [1,2,3,4,5]
d = {'ja': 1, 'je': 2, 'ji': 3, 'jo': 4, 'ju': 5}
random = np.random.randn(5)
index = ["a", "b", "c", "d", "e"]
s = pd.Series(random, index=index)
print(s.index)

print('\n' + '=' * 100)
print('=' * 100 + '\n')

sd = pd.Series(d, index=['ja','je','ji','jo','ju'], name = 'Dictionary like series')
print(sd)

n = pd.Series(5.0, index=index)
print(n)

print('\n' + '=' * 100)
print('=' * 100 + '\n')

# print(s.iloc[0])
# print(s.iloc[:3])
# print(s[s > s.median()])
# print(s.iloc[[4, 3, 1]])
# print(np.exp(s))
# print(type(s))
# print(type(s.to_numpy()))

# A Series is also like a fixed-size dict in that you can get and set values by index label
print(sd['ja'])
print('ja' in sd)
print('jj' in sd)
print(sd.get('g', np.nan))
print(sd.ja) # Access values as attributes

print('\n' + '=' * 100)
print('=' * 100 + '\n')

# print(sd + sd)
# print(np.exp(sd))
# print(sd.iloc[1:])
print(sd.name)