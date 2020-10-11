# Apriori Algorithm tutorial from Machine Learning A-Z - SuperDataScience -> Input by Ryan L Buchanan 09OCT20

# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Data prerocessing
dataset = pd.read_csv('Market_Basket_Optimisation.csv')
X = dataset.iloc[:, [3,4]].values

# Train the Apriori model on the dataset


# Visualize the result


# Display the first result coming directly from the output of the apriori function


# Put the results into a well-organized Pandas DataFrame


# Display the results non-sorted


# Display the results sorted by descending lifts

