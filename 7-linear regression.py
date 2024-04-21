#Implement a linear regression to predict a continuous value based on one variable. 

import numpy as np 

  

class LinearRegression: 

  def __init__(self): 

    self.slope = None 

    self.intercept = None 

  

  def fit(self, x, y): 

    # Convert x and y to NumPy arrays for efficient calculations 

    x = np.asarray(x) 

    y = np.asarray(y) 

  

    # Calculate mean of x and y 

    x_mean = np.mean(x) 

    y_mean = np.mean(y) 

  

    # Calculate numerator and denominator for slope 

    numerator = np.sum((x - x_mean) * (y - y_mean)) 

    denominator = np.sum((x - x_mean) ** 2) 

  

    # Calculate slope and intercept 

    self.slope = numerator / denominator 

    self.intercept = y_mean - self.slope * x_mean 

  

  def predict(self, x): 

    if self.slope is None or self.intercept is None: 

      raise RuntimeError("Model not fit yet. Call fit(x, y) before making predictions.") 

    return self.slope * x + self.intercept 

  

# Example data (replace with your actual data) 

x = [1, 2, 3, 4, 5] 

y = [2, 4, 5, 4, 5] 

  

# Create and fit the linear regression model 

model = LinearRegression() 

model.fit(x, y) 

  

# Predict for a new data point 

new_x = 6 

predicted_y = model.predict(new_x) 

  

print(f"Predicted value for x = {new_x}: {predicted_y}") 

"""  Predicted value for x = 6: 5.8


** Process exited - Return Code: 0 **
Press Enter to exit terminal  """
