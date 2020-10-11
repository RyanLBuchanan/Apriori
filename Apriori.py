# Apriori Algorithm tutorial from Machine Learning A-Z - SuperDataScience -> Input by Ryan L Buchanan 09OCT20

# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import the dataset
dataset = pd.read_csv('Market_Basket_Optimisation.csv')
X = dataset.iloc[:, [3,4]].values

