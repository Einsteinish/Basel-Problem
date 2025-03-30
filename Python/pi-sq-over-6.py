import numpy as np
import matplotlib.pyplot as plt

n = 100
terms = 1 / (np.arange(1, n+1)**2)
partial_sums = np.cumsum(terms)
plt.plot(partial_sums, label='Sum of 1/n²')
plt.axhline(np.pi**2/6, color='r', linestyle='--', label='π²/6')
# Adjusted red y-value label to avoid title overlap
plt.text(50, np.pi**2/6 - 0.1, 'π²/6 ≈ 1.64493', color='red', ha='center', fontsize=12)
plt.legend()
plt.title('Basel Problem')
plt.xlabel('Terms')
plt.ylabel('Sum')
plt.show()
