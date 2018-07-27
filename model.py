import pandas as pd
import numpy as np
import sklearn
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

df1 = pd.read_csv('./dengue_features_train.csv')
dfFeaturesTrain = df1.iloc[:,4:].interpolate()


df2 = pd.read_csv('./dengue_labels_train.csv')
dfLabelsTrain = df2.iloc[:,3:]

df3 = pd.read_csv('./dengue_features_test.csv')
dfFeaturesTest = df3.iloc[:,4:].interpolate()

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(dfFeaturesTrain, dfLabelsTrain)

# Make predictions using the testing set
patients_y_pred = regr.predict(dfFeaturesTest)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(dfFeaturesTest, patients_y_pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(dfFeaturesTest, patients_y_pred))

# Plot outputs
plt.scatter(dfFeaturesTest,patients_y_pred,  color='black')

plt.xticks(())
plt.yticks(())

plt.show()