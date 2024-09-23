"""
                                MMMMMMMMM                             
                             MMMMh                                    
                           MMM                                        
                          MM                                          
                         MM        mM`                                
                         M      MM                                    
                         M     M     MMMMMMM                          
                              s             MMM                       
                                              MMMM                    
                                                MMMy                  
           M                                     -MMMM                
          MM                                       MMMMMMMs           
         MMM                                         /MMMM            
         MMMM                                         MMMM            
          MMMM                                        MMMy            
           MMMMM                                      mMMM            
            MMMMMM                  the                MMM            
             MMMMMM/             Code Beats            MMM            
               MMMMMM       http://codebeats.net       MMM            
                MMMMM                                  MMM            
                 MMMMM                                 MMM            
                  MMMM                                 MM             
                   MMM                                 MM             
                   MM                                  M              
                   MMMMMMMMMMM                        M               
                   MMMNNMMMMMMMMM                    M                
                               MMMMM                M                 
                                   mMM            m                   
                                        :                             

Code downloaded from: http://codebeats.net
by: "Tomás Jaramillo Quintero"
License: This code is under a Creative Commons Attribution 3.0 Unported License
License URL: http://creativecommons.org/licenses/by/3.0/
"""
# Import necessary libraries
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

# Create a new Matplotlib figure
fig = plt.figure()

# Constants
g = 9.8  # Gravity (m/s^2)

# Initialize empty abscissæ and ordinates vectors
x = []
Ts = []
Ts_Tsh = []

# Loop over angles from 0 to 90 degrees
for i in range(91):
    # Convert degrees to radians
    theta0 = np.radians(i)
    l = 1  # Length of the pendulum (1 meter)
    
    # Define function f and calculate its integral over the [0, theta0] interval
    f = lambda x: 1 / np.sqrt(np.cos(x) - np.cos(theta0))
    F, erri = integrate.quad(f, 0, theta0)  # Integrate numerically
    
    # Calculate the period (T) using the integral and other constants
    T = 4 * np.sqrt(l / g) * F
    
    # Calculate the simple harmonic period for comparison
    Ths = 2 * np.pi * np.sqrt(l / g)
    TsTsh = T / Ths  # Period / Simple Harmonic Period
    
    # Append current values to the vectors
    x.append(i)       # Angle in degrees
    Ts.append(T)      # Period in seconds
    Ts_Tsh.append(TsTsh)  # Ratio of Period to Simple Harmonic Period

# Add labels and plot the results
plt.xlabel('Theta_o (degrees)')
plt.ylabel('[Period/Simple Harmonic Period] OR Period (seconds)')

# Plot period and ratio of period to simple harmonic period
plt.plot(x, Ts, color="#f04859", linewidth=4, label="Period (seconds)")
plt.plot(x, Ts_Tsh, color="#d4c669", linewidth=4, label="Period/Simple Harmonic Period")

# Add legend and show the plot
plt.legend()
plt.show()