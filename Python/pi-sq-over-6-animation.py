import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of terms
n = 100
terms = 1 / (np.arange(1, n+1)**2)
partial_sums = np.cumsum(terms)

# Setup figure
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, n)
ax.set_ylim(0, 2)  # Adjust y-limit to fit the sum and label
ax.set_title('Basel Problem')
ax.set_xlabel('Terms')
ax.set_ylabel('Sum')
ax.axhline(np.pi**2/6, color='r', linestyle='--', label='π²/6')
ax.text(50, np.pi**2/6 - 0.1, 'π²/6 ≈ 1.64493', color='red', ha='center', fontsize=12)
ax.legend()

# Initialize an empty line for the partial sums
line, = ax.plot([], [], label='Sum of 1/n²')

# Animation initialization function (optional, but good practice)
def init():
    line.set_data([], [])
    return line,

# Animation update function
def update(frame):
    # Frame goes from 0 to n-1, but we want 1 to n terms
    x_data = np.arange(frame + 1)
    y_data = partial_sums[:frame + 1]  # Slice up to current frame
    line.set_data(x_data, y_data)
    return line,

# Create animation
ani = FuncAnimation(fig, update, frames=range(n), init_func=init, interval=50, blit=True)

# Save animation as a GIF that loops forever (optional)
ani.save('basel_problem_convergence.gif', writer='pillow', fps=20)

plt.show()
