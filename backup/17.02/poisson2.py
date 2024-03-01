import numpy as np
import matplotlib.pyplot as plt

def generate_poisson_samples(x_range, y_range, radius, n_samples):
    # Initialize an empty list to store the samples
    samples = []
    
    # Generate the first sample randomly
    x, y = np.random.uniform(x_range[0], x_range[1]), np.random.uniform(y_range[0], y_range[1])
    samples.append((x, y))
    
    # Initialize an empty list to store the active samples
    active_samples = [0]
    
    while active_samples:
        # Randomly select an active sample
        index = np.random.choice(active_samples)
        x, y = samples[index]
        
        # Generate a new sample within the specified radius
        found = False
        for _ in range(30):
            theta = np.random.uniform(0, 2 * np.pi)
            r = np.random.uniform(radius, 2 * radius)
            new_x = x + r * np.cos(theta)
            new_y = y + r * np.sin(theta)
            
            # Check if the new sample is within the range and not too close to any existing samples
            if x_range[0] <= new_x < x_range[1] and y_range[0] <= new_y < y_range[1]:
                closest_distance = min([np.hypot(new_x - s[0], new_y - s[1]) for s in samples])
                if closest_distance > radius:
                    samples.append((new_x, new_y))
                    active_samples.append(len(samples) - 1)
                    found = True
                    break
                    
        # If no new sample was found, remove the active sample from the list
        if not found:
            active_samples.remove(index)
            
    return samples[:n_samples]

# Set the range and radius for the samples
x_range = (0, 100)
y_range = (0, 100)
radius = 10
n_samples = 60

# Generate the samples
samples = generate_poisson_samples(x_range, y_range, radius, n_samples)

# Plot the samples
x = [s[0] for s in samples]
y = [s[1] for s in samples]
plt.scatter(x, y)
plt.show()