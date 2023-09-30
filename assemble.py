# Importing necessary libraries
import pandas as pd
import numpy as np
import statsmodels.api as sm

# Re-defining the original Anscombe Quartet data
anscombe = pd.DataFrame({
    'x1': [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
    'x2': [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
    'x3': [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
    'x4': [8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8],
    'y1': [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68],
    'y2': [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74],
    'y3': [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73],
    'y4': [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]
})

# Generating the new datasets and fitting linear regression models
y1_new = anscombe['y1'] + (anscombe['x1'] - np.mean(anscombe['x1']))**2 * 0.5
y2_new = anscombe['y2'] + np.sin(anscombe['x2']) * 2
y3_new = anscombe['y3'] + np.log(anscombe['x3'])
y4_new = anscombe['y4'] + np.exp((anscombe['x4'] - np.mean(anscombe['x4']))/5.0)

set_I_new_design_matrix = sm.add_constant(anscombe['x1'])
set_I_new_model = sm.OLS(y1_new, set_I_new_design_matrix)
set_II_new_design_matrix = sm.add_constant(anscombe['x2'])
set_II_new_model = sm.OLS(y2_new, set_II_new_design_matrix)
set_III_new_design_matrix = sm.add_constant(anscombe['x3'])
set_III_new_model = sm.OLS(y3_new, set_III_new_design_matrix)
set_IV_new_design_matrix = sm.add_constant(anscombe['x4'])
set_IV_new_model = sm.OLS(y4_new, set_IV_new_design_matrix)

(set_I_new_model.fit().params, set_II_new_model.fit().params, 
 set_III_new_model.fit().params, set_IV_new_model.fit().params)

import matplotlib.pyplot as plt  # Importing the plotting library

# Plotting the Modified Anscombe Quartet datasets again

plt.figure(figsize=(10, 8))

# Quadratic trend
plt.subplot(2, 2, 1)
plt.scatter(anscombe['x1'], y1_new, color='blue')
plt.title('Quadratic Trend')
plt.xlabel('x1')
plt.ylabel('y1_new')
plt.xlim(2, 20)
plt.ylim(2, 14)

# Sinusoidal pattern
plt.subplot(2, 2, 2)
plt.scatter(anscombe['x2'], y2_new, color='green')
plt.title('Sinusoidal Pattern')
plt.xlabel('x2')
plt.ylabel('y2_new')
plt.xlim(2, 20)
plt.ylim(2, 14)

# Logarithmic pattern
plt.subplot(2, 2, 3)
plt.scatter(anscombe['x3'], y3_new, color='red')
plt.title('Logarithmic Pattern')
plt.xlabel('x3')
plt.ylabel('y3_new')
plt.xlim(2, 20)
plt.ylim(2, 14)

# Exponential increase
plt.subplot(2, 2, 4)
plt.scatter(anscombe['x4'], y4_new, color='purple')
plt.title('Exponential Increase')
plt.xlabel('x4')
plt.ylabel('y4_new')
plt.xlim(2, 20)
plt.ylim(2, 14)

plt.tight_layout()
plt.show()
