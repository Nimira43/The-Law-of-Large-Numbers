## Monte Carlo sampling
###### Monte Carlo sampling is a widely-used technique in computational mathematics and statistics. It's based on the idea of using randomness to solve problems that might be deterministic in principle. 

#### What is Monte Carlo Sampling?
###### Monte Carlo sampling involves generating random samples to estimate numerical results. This technique is particularly useful for:

###### Integration and numerical approximations.

###### Simulating complex systems.

###### Solving problems in high-dimensional spaces.

###### Risk assessment and decision-making.

#### How It Works:
##### Define a Domain of Possible Inputs:

###### Specify the range or distribution from which to draw random samples.

##### Generate Random Inputs:

###### Use random sampling to create a set of inputs from the defined domain.

##### Perform a Deterministic Computation:

###### Apply a mathematical function or simulation to each random input to obtain results.

##### Aggregate the Results:

###### Analyse the results to estimate the desired outcome, such as the mean, variance, or probability.

#### Example: Estimating the Value of Pi (π)
###### One classic example of Monte Carlo sampling is estimating the value of Pi using random points in a square.

#### Step-by-Step Example:
##### Define the Domain:

###### Consider a square with sides of length 2 centered at the origin (so it spans from −1 to 1 on both the x and y axes).

###### The inscribed circle will have a radius of 1.

##### Generate Random Points:

###### Generate random points within the square.

##### Count Points Inside the Circle:

###### Check if the points fall inside the circle using the equation 
##### 𝑥^2 + y^2 ≤ 1

##### Estimate Pi:

###### The ratio of points inside the circle to the total number of points, multiplied by 4, will approximate the value of Pi.

#### Python Code Example:
```
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
```

#### Explanation:
###### Generate Random Points: np.random.uniform generates random x and y values between -1 and 1.

###### Check Points Inside Circle: The points inside the circle satisfy 
##### 𝑥^2 + y^2 ≤ 1

###### Estimate Pi: The ratio of the points inside the circle to the total number of points, multiplied by 4, provides an estimate of Pi.

###### Plot: The plot shows points inside the circle in blue and those outside in red.

#### Running the Code:
###### Executing this code will give you a visual representation of the Monte Carlo method for estimating Pi and print the estimated value.

###### Monte Carlo sampling is powerful and versatile, allowing for many applications across various fields.