import matplotlib.pyplot as plt
import numpy as np

# Population Size
population_size = 2.3e5

# Sampling Parameters
sample_size = 50
number_of_samples = 500

# Generate Population of Numbers
population = 1 / np.logspace(np.log10(0.001), np.log10(10), int(population_size))

# True mean
true_mean = np.mean(population)

# Output 
print('[-----------------------------------------------]')
print('[*] Population Size: ', population_size)
print('[-----------------------------------------------]')
print('[*] Generated Population Size: ', population_size)
print('[-----------------------------------------------]')
print('[*] True Mean of Population: ', true_mean)
print('[*] Sample Size: ', sample_size)
print('[*] Number of Sample: ', number_of_samples)
print('[-----------------------------------------------]')
print

# Random Sampling
print('[*] Random Sample of 50 from Population:', np.random.choice(population, size=sample_size))
print('[*] Mean of Another Random Sample of 50: ', np.mean(np.random.choice(population, size=sample_size)))
print('[-----------------------------------------------]')

# Sample means
sample_means = np.zeros(number_of_samples)

for experiment_i in range(number_of_samples):
  random_sample = np.random.choice(population, size=sample_size)
  sample_means[experiment_i] = np.mean(random_sample)

print('[*] Overall Mean of Sample Means: ', np.mean(sample_means)) 
print('[*] Standard Deviation of Sample Means: ', np.std(sample_means)) 
print('[-----------------------------------------------]')

plt.plot(sample_means, 'ko', label='Sample Means')
plt.xlabel('Sample Index') 
plt.ylabel('Sample Mean Value') 
plt.title('Distribution of Sample Means') 
plt.legend() 
plt.show() 


