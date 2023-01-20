import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

##skrearn의 독립변수는 항상 2차원 배열로 입력

df = pd.DataFrame(['animal': ['falcon', 'falcon', 'parrot','parrot'],
                   ['captive','wild','captive','wild'])

arrays = [['falcon', 'falcon', 'parrot','parrot'], ['captive','wild','captive','wild']]

index = pd.MultiIndex.from_arrays(arraysm , names=('animal', 'type'))

df = pd.DataFrame({'max_speed' : [390, 350, 240, 100]})

mapping = {'a':'red', 'b' : 'red', 'c' : 'blue',
           'd': 'blue', 'e': 'red', 'f' : 'orange'}