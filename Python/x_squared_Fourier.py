import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the interval
x = np.linspace(-np.pi, np.pi, 1000)
f_x = x**2

# Fourier series function
def fourier_series_x2(x, n_terms):
    fourier_sum = np.full_like(x, np.pi**2 / 3)
    for n in range(1, n_terms + 1):
        an = 4 * (-1)**n / n**2
        fourier_sum += an * np.cos(n * x)
    return fourier_sum

# Setup figure
fig, ax = plt.subplots(figsize=(10, 6))
line, = ax.plot(x, f_x, 'k-', label='f(x) = x²', linewidth=2)
approx_line, = ax.plot([], [], 'b--', label='Fourier Approx')
ax.set_xlim(-np.pi, np.pi)
ax.set_ylim(-1, 12)
ax.set_title('Fourier Series Building f(x) = x² (Basel Link)')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axhline(0, color='gray', alpha=0.5)
ax.axvline(0, color='gray', alpha=0.5)
ax.grid(True, alpha=0.3)
ax.legend()

# Add a text object to display the number of terms in blue
terms_text = ax.text(0.05, 0.95, 'n = 0', transform=ax.transAxes, fontsize=12, 
                     verticalalignment='top', color=approx_line.get_color())

# Animation function
def update(frame):
    n_terms = frame + 1
    fourier_approx = fourier_series_x2(x, n_terms)
    approx_line.set_data(x, fourier_approx)
    approx_line.set_label(f'(Σ 1/n² → π²/6)')
    terms_text.set_text(f'n = {n_terms}')  # Update the text with the current number of terms
    ax.legend()
    return approx_line, terms_text

# Create frames for 3 repeats (20 frames per cycle, repeated 3 times = 60 frames)
frames = list(range(20)) * 3  # Repeats 0-19 five times

# Create animation
ani = FuncAnimation(fig, update, frames=frames, interval=500, blit=True)

# Save animation 
ani.save('fourier_x2_basel_3_repeats.gif', writer='pillow', fps=2)  # Adjust fps as needed

plt.show()
