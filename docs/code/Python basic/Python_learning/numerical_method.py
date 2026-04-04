
#Lorenz Force Function

import numpy as np

def lorenz_force(q, v, B):
    """
    Calculate Lorentz force F = q * (v × B)
    
    Parameters:
    q: charge (C)
    v: velocity vector [vx, vy, vz] (m/s)
    B: magnetic field vector [Bx, By, Bz] (T)
    
    Returns:
    F: force vector [Fx, Fy, Fz] (N)
    """
    v = np.array(v)
    B = np.array(B)
    
    # Cross product
    v_cross_B = np.cross(v, B)
    
    # Lorentz force
    F = q * v_cross_B
    
    return F

# Example: Electron motion in magnetic field
q_electron = -1.6e-19  # Electron charge
v = [1e6, 0, 0]        # Velocity in x-direction
B = [0, 0, 1]          # Magnetic field in z-direction

force = lorenz_force(q_electron, v, B)
print(f"Lorentz Force: {force} N")  # Should get force in y-direction
