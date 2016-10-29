import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path = "E:\python程序练习\machine learning\machine-learning-ex1\ex1"
data = pd.read_csv(path + "\ex1data1.txt", header=None,
                   names=("Population", "Profit"))

data.plot(kind="scatter", x="Population", y="Profit")
