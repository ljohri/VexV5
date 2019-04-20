import pandas as pd 
import numpy as np
import csv
import matplotlib as mpl
mpl.get_backend()
import matplotlib.pyplot as plt
 

print ("hello World")
pid_data = pd.read_csv("data.csv", delimiter=',')
#print (pid_data.head())

series = pid_data[['output']]
print (series)

plt.plot(series)
plt.show()