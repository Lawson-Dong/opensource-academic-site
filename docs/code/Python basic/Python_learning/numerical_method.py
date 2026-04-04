import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def kinetic_energy(mass, velocity):
    """Calculate the kinetic energy of an object."""
    return 0.5 * mass * velocity ** 2

m = input("Enter the mass of the object (in kg): ")
v = input("Enter the velocity of the object (in m/s): ")


mass = float(m)
velocity = float(v)
ke = kinetic_energy(mass, velocity)
print(f"The kinetic energy of the object is: {ke} Joules")
