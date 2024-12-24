import matplotlib.pyplot as plt
import numpy as np

# Initialise population size
population_size = 230  # Reduced for better performance in visualisation
print('Population Size: ', population_size)

# Generate frequency values (f)
frequency_values = np.logspace(np.log10(0.001), np.log10(10), population_size)
print('Frequency values (f): ', frequency_values)

# Calculate the inverse of frequency values (1/f)
inverse_f = 1 / frequency_values
print('Inverse of frequency values (1/f): ', inverse_f)

# Plot the inverse frequency values
plt.figure(figsize=(10, 6))
plt.plot(inverse_f, label='1/f')
plt.title('Inverse of Frequency Values')
plt.xlabel('Index')
plt.ylabel('1/f')
plt.grid(True)
plt.legend()
plt.show()

