import numpy as np
import matplotlib.pyplot as plt

# Parameters
size = 50       # cube size (NxNxN)
height = 1.0    # peak value at cone center
radius = size/2 # radius to edge of cube

# Create coordinate grid (centered at zero)
coords = np.linspace(-1, 1, size)
X, Y, Z = np.meshgrid(coords, coords, coords, indexing="ij")

# Convert to cylindrical radius
R = np.sqrt(X**2 + Y**2)

# Cone equation: value decreases linearly with radius, flat along Z
# Limit negative values to 0
tensor = np.maximum(height * (1 - R / np.max(R)), 0)

# Visualize cross-section
mid = size // 2
plt.imshow(tensor[:, :, mid], origin="lower", cmap="inferno")
plt.colorbar(label="Value")
plt.title("Conical Distribution - Mid Z Slice")
plt.savefig("test.png")
