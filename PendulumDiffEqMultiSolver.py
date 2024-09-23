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
import scipy
import scipy.integrate
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Define the pendulum model as a system of first-order differential equations
def dy2dt(t, y, L):
    theta, dthetadt = y
    d2thetadt2 = -(g/L) * np.sin(theta)
    return [dthetadt, d2thetadt2]

# Constants
g = 9.8  # Gravity (m/s^2)
L = 1.0  # Length of the pendulum (1 meter)

# List of initial angles in degrees to drop the pendulum from
angles = [5, 10, 15, 30, 45, 60, 90]
# Custom colors for plotting each angle
colors = ["#f04859", "#ec5b5b", "#e6775f", "#df9763", "#dd9c63", "#d9b366", "#d4c669"]

# Create a new Matplotlib figure
fig = plt.figure()

# Iterate through each angle and its corresponding color
for j, c in zip(angles, colors):
    # Define initial conditions: angle in radians, initial angular velocity
    theta0 = np.radians(j)  # Convert angle to radians
    dthetadt0 = 0.0  # Initial velocity (0 degrees/s)

    # Solve the system of ODEs using the Runge-Kutta 4,5 method (LSODA is default in latest SciPy)
    sol = scipy.integrate.solve_ivp(
        fun=lambda t, y: dy2dt(t, y, L),
        t_span=(0, 10),  # Time range (0 to 10 seconds)
        y0=[theta0, dthetadt0],  # Initial conditions
        method='RK45',  # Use Runge-Kutta 4,5 method
        max_step=0.01  # Time step
    )

    # Extract results: time points and corresponding theta values (converted to degrees)
    t = sol.t
    thetas = np.degrees(sol.y[0])  # Convert theta from radians to degrees

    # Plot theta(t) for the given initial angle
    plt.plot(t, thetas, color=c)

# Add legend and labels to the graph
plt.legend([f'{angle} deg' for angle in angles], loc="upper right")
plt.xlabel('Time (s)')
plt.ylabel('Theta(t) (degrees)')
plt.title('Pendulum Motion for Various Initial Angles')
plt.show()