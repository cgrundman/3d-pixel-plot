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

blur_tensor = tensor.copy()

# Blur tensor
for i in range(size):
    for j in range(size):
        for k in range(size):
            #rint(type(tensor[i,j,k]))
            loc_array = tensor[i-3:i+3,j-3:j+3,k-3:k+3]
            if loc_array.size > 0:
                blur_tensor[i,j,k] = np.mean(loc_array) * random.uniform(0.90, 1)
            else:
                blur_tensor[i,j,k] = np.float64(0.0)
            #print(type(tensor[i,j,k]))

# Create threshhold
for idx, iteration in enumerate(np.linspace(0, 180, 50)):

    # Mask low values to avoid plotting every point
    threshhold = round(0.9 - iteration/450, 3)
    mask = blur_tensor > threshhold

    dx = coords[1]-coords[0]
    dy = coords[1]-coords[0]
    dz = coords[1]-coords[0]

    # Plot 3D bar
    fig = plt.figure(figsize=(8, 9))
    ax1 = fig.add_subplot(111, projection='3d')
    ax1.bar3d(
        X[mask], Y[mask], Z[mask],
        dx=dx, dy=dy, dz=dz,
        shade=True
    )

    # Axes settings
    ax1.set_box_aspect((1, 1, 1))  # equal aspect ratio
    ax1.set_title("3D Conical Tensor Distribution Display with Threshhold\n")
    ax1.set_xlim([-10, 10])
    ax1.set_ylim([-10, 10])
    ax1.set_zlim([0, 20])
    ax1.xaxis.set_tick_params(labelbottom=False)
    ax1.yaxis.set_tick_params(labelbottom=False)
    ax1.zaxis.set_tick_params(labelbottom=False)
    plt.tight_layout()
    #plt.show()
    plt.savefig(f"plots/threshhold/threshold_{idx}.png")
    plt.close()

# Create angle
for idx, iteration in enumerate(np.linspace(0, 180, 90)):

    # Mask low values to avoid plotting every point
    mask = blur_tensor > 0.1

    # Plot 3D scatter above view
    fig = plt.figure(figsize=(16, 8))
    fig.suptitle("3D Conical Tensor Distribution", fontsize=24)
    ax1 = fig.add_subplot(121, projection='3d')
    p1 = ax1.scatter(
        X[mask], Y[mask], Z[mask],
        c=blur_tensor[mask], cmap="inferno", marker=".", s=25
    )
    ax1.view_init(elev=30, azim=idx-45, roll=0)

    # Axes settings
    ax1.set_box_aspect((1, 1, 1))  # equal aspect ratio
    #ax1.set_title("3D Conical Tensor Distribution")
    ax1.set_xlim([-10, 10])
    ax1.set_ylim([-10, 10])
    ax1.set_zlim([0, 20])
    ax1.xaxis.set_tick_params(labelbottom=False)
    ax1.yaxis.set_tick_params(labelbottom=False)
    ax1.zaxis.set_tick_params(labelbottom=False)
    fig.colorbar(p1, ax=ax1, label="Value", fraction=0.035, pad=0.02)

    # Plot 3D scatter under view
    ax2 = fig.add_subplot(122, projection='3d')
    p2 = ax2.scatter(
        X[mask], Y[mask], Z[mask],
        c=blur_tensor[mask], cmap="inferno", marker=".", s=25
    )
    ax2.view_init(elev=-30, azim=idx-60, roll=0)

    # Axes settings
    ax2.set_box_aspect((1, 1, 1))  # equal aspect ratio
    #ax2.set_title("3D Conical Tensor Distribution")
    ax2.set_xlim([-10, 10])
    ax2.set_ylim([-10, 10])
    ax2.set_zlim([0, 20])
    ax2.xaxis.set_tick_params(labelbottom=False)
    ax2.yaxis.set_tick_params(labelbottom=False)
    ax2.zaxis.set_tick_params(labelbottom=False)
    fig.colorbar(p2, ax=ax2, label="Value", fraction=0.035, pad=0.02)
    plt.tight_layout()
    #plt.show()
    plt.savefig(f"plots/angle/angle_{idx}.png")
    plt.close()
