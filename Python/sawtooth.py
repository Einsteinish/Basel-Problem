import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the interval
x = np.linspace(-np.pi, np.pi, 1000, endpoint=False)
f_x = x

# Fourier series function for sawtooth
def fourier_series_sawtooth(x, n_terms):
    fourier_sum = np.zeros_like(x)
    for n in range(1, n_terms + 1):
        bn = 2 * (-1)**(n + 1) / n
        fourier_sum += bn * np.sin(n * x)
    return fourier_sum

# Setup figure
fig, ax = plt.subplots(figsize=(10, 6))
line, = ax.plot(x, f_x, 'k-', label='f(x) = x (sawtooth)', linewidth=2)
approx_line, = ax.plot([], [], 'b--', label='Fourier Approx')
ax.set_xlim(-np.pi, np.pi)
ax.set_ylim(-4, 4)
ax.set_title('Sawtooth Fourier Series Links to Basel Problem')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axhline(0, color='gray', alpha=0.5)
ax.axvline(0, color='gray', alpha=0.5)
ax.grid(True, alpha=0.3)
ax.legend()

# Animation function
def update(frame):
    fourier_approx = fourier_series_sawtooth(x, frame + 1)
    approx_line.set_data(x, fourier_approx)
    approx_line.set_label(f'n terms')
    ax.legend()
    # Add Basel tie-in at the end
    if frame == 19:  # Last frame
        ax.text(0, -3, 'Parseval: π²/3 = 2 Σ(1/n²) → Σ(1/n²) = π²/6', 
                ha='center', fontsize=12, color='red')
    return approx_line,

# Create frames for one cycle (n = 1 to n = 20)
frames = range(20)

# Create animation
ani = FuncAnimation(fig, update, frames=frames, interval=500, blit=True)

# Save animation as a GIF that loops forever
ani.save('fourier_sawtooth_basel_loopforever.gif', writer='pillow', fps=2)

plt.show()
