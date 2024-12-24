import numpy as np
import matplotlib.pyplot as plt

# Number of random points
num_points = 100000

# Generate random points
x = np.random.uniform(-1, 1, num_points)
y = np.random.uniform(-1, 1, num_points)

# Check if points are inside the circle
inside_circle = x**2 + y**2 <= 1

# Estimate the value of Pi
pi_estimate = (inside_circle.sum() / num_points) * 4
print('Estimated Pi:', pi_estimate)

# Plot the points
plt.figure(figsize=(8, 8))
plt.scatter(x[inside_circle], y[inside_circle], color='blue', s=1)
plt.scatter(x[~inside_circle], y[~inside_circle], color='red', s=1)
plt.title('Monte Carlo Estimation of Pi')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
