import matplotlib.pyplot as plt
import numpy as np

# Initialise population size
population_size = 2.3e5
print('[-----------------------------------------------]')
print('[*] Population Size: ', population_size)
print('[-----------------------------------------------]')

# Parameters for sampling
sample_size = 50
number_of_samples = 500

# Generate Population of Numbers
population = 1 / np.logspace(np.log10(0.001), np.log10(10), int(population_size))
print('[*] Generated Population of Numbers')
print('[*] True Mean of Population: ', np.mean(population))
print('[-----------------------------------------------]')

# Function to draw multiple samples
print('[*] Drawing Multiple Samples...')
samples = [np.random.choice(population, size=sample_size) for _ in range(number_of_samples)]
print('[*] Samples Drawn')
print('[-----------------------------------------------]')

# Calculate the mean of each sample
sample_means = np.array([np.mean(sample) for sample in samples])
print('[*] Calculated Mean of Each Sample')
print('[*] Number of Samples: ', number_of_samples)
print('[-----------------------------------------------]')

# Plot the distribution of sample means
plt.figure(figsize=(10, 6))
plt.hist(sample_means, bins=30, edgecolor='k', alpha=0.7)
plt.title('Distribution of Sample Means')
plt.xlabel('Mean Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
print('[-----------------------------------------------]')
print('[*] Overall Mean of Sample Means: ', np.mean(sample_means))
print('[*] Standard Deviation of Sample Means: ', np.std(sample_means))
print('[-----------------------------------------------]')
