# Apriori Algorithm tutorial from Machine Learning A-Z - SuperDataScience -> Input by Ryan L Buchanan 09OCT20

!pip install apyori

# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Data prerocessing
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
transactions = []
for i in range(0, 7501):
    transactions.append([str(dataset.values[i, j]) for j in range(0, 20)])


# Train the Apriori model on the dataset


# Visualize the result


# Display the first result coming directly from the output of the apriori function


# Put the results into a well-organized Pandas DataFrame


# Display the results non-sorted


# Display the results sorted by descending lifts

