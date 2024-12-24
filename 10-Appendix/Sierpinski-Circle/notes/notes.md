## Sierpinski Circle 

###### This is just an extra small side project not really related to the overall project - The Law of Large Numbers. 

###### The Sierpinski Circle code is focused on generating a fractal pattern through a recursive approach. It doesn't directly relate to the Law of Large Numbers, which is a concept from probability theory and statistics.

##### However after doing the Monte Carlo example of estimating the Value of Pi I was immediately struck by the output given. After doing the Sierpinski Triangle and Sierpinski Carpet in other projects I wanted to do a Sierpinski Circle!!! 

#### Code Explanation

##### sierpinski_circle Function:

###### This function recursively adds circles to the plot.

###### Base case: Adds a circle at the given position with the given radius when the depth is zero.

###### Recursive case: Adds smaller circles around the current circle, reducing the depth each time.

##### Plot Configuration:

###### fig, ax = plt.subplots(figsize=(8, 8)): Sets up the plot with equal aspect ratio.

###### sierpinski_circle(ax, 0, 0, 1, depth): Starts the recursive drawing of circles.

###### Adjusts the plot limits and turns off the axis for a cleaner look.