import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
%matplotlib inline

co2 =USAhousing = pd.read_csv('CO2 Emissions_Canada.csv')
x = co2[['Engine Size(L)', 'Cylinders','Fuel Consumption Comb (L/100 km)']]
y = co2['CO2 Emissions(g/km)']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=101)

lm = LinearRegression()
lm.fit(X_train,y_train)

pickle.dump(lm, open('co2_model.pkl','wb'))
