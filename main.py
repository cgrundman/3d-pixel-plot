import numpy as np
import matplotlib.pyplot as plt
import random

# Parameters
size = 50       # cube size (NxNxN)
height = 1.0    # peak value at cone center
r = 3 # radius to edge of cube

# Create coordinate grid (centered at zero)
coords = np.linspace(-10, 10, size)
coords_z = np.linspace(0, 20, size)
X, Y, Z = np.meshgrid(coords, coords, coords_z, indexing="ij")

# Limit negative values to 0
tensor = np.zeros((size, size, size))

# Cone creation
for i in range(size):
    for j in range(size):
        distance = np.sqrt((coords[i])**2 + (coords[j])**2)
        #print(f"{i}x{j}: {distance}")
        for k in range(size):
            #print((k+1)/10)
            if distance < r + (k+1)/9:
                tensor[i, j, k] = 1 - k/100
            #tensor[i, j, k] = k
#tensor = tensor/np.max(tensor)
#tensor = np.maximum(height * (1 - R / np.max(R)), 0)

blur_tensor = tensor.copy()

# Blur tensor
for i in range(size):
    for j in range(size):
        for k in range(size):
            #rint(type(tensor[i,j,k]))
            loc_array = tensor[i-3:i+3,j-3:j+3,k-3:k+3]
            if loc_array.size > 0:
                blur_tensor[i,j,k] = np.mean(loc_array) * random.uniform(0.95, 1)
            else:
                blur_tensor[i,j,k] = np.float64(0.0)
            #print(type(tensor[i,j,k]))


for threshhold in range(0, 10):
    # Mask low values to avoid plotting every point
    mask = blur_tensor > (1 - threshhold/10)

    # Plot 3D scatter
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    p = ax.bar3d(
        X[mask], Y[mask], Z[mask],
        dx=coords[1]-coords[0], dy=coords[1]-coords[0], dz=coords[1]-coords[0],
        #c=blur_tensor[mask], 
        cmap="inferno", #marker="."
    )

    # Axes settings
    ax.set_box_aspect((1, 1, 1))  # equal aspect ratio
    ax.set_title("3D Conical Tensor Distribution")
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_zlim([0, 20])
    fig.colorbar(p, ax=ax, label="Value")
    #plt.show()
    plt.savefig(f"/plots/threshold/test_{threshhold}.png")
