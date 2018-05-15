#*************************************************************************************#
#                                                                                     #
#                               SUPERSONIC FLOW OVER A CONE                           #
#                                                                                     #
#                            (by solving Taylor-Maccoll equation)                     #
#                                                                                     #
#*************************************************************************************#

#********************************* DESCRIPTION ***************************************



#*********************************** INPUT *******************************************

T0 = 300.0 # Total freestream temperature (K)
C_p = 1005.0 # Specific heat at constant pressure (J/kg/K)
beta = 40.0 # Wave angle (degrees)
M_inf = 2.0 # Freestream Mach number 
gamma = 1.4 # Adiabatic constant

#***************************** IMPORTING PACKAGES ************************************
# Standard packages
from matplotlib.pyplot import *
import numpy as np
import math

# User-defined packages
from oblique_shock import *
from taylor_maccoll import *

#******************************** COMPUTATION ****************************************

V_max = math.sqrt(C_p*T0) # Max theoretical velocity (m/s)
[M_2, delta, beta] = oblique_shock_wave_properties(M_inf, beta, gamma)

# Setting up initial conditions
V = math.pow(2/((gamma - 1)*M_2**2) + 1, -0.5)
V_r = [V*math.cos(beta - delta)]
V_theta = [V*math.sin(beta - delta)]


# Starting computations
del_theta = 10**-5
err = 1.0
tol = 10.0**-8

theta = [beta]
i = 0

print("Starting computation")
while err>tol:
      [V_r_local, V_theta_local] = euler_step_integration(theta[i], del_theta, gamma, V_r[i], V_theta[i])
      V_theta += [V_theta_local]
      V_r += [V_r_local]
      err = V_theta[i]
      print(err)
      i += 1
      theta = theta + [beta - i*del_theta]
      print("Ran incremental step : "+str(i))
      
print("Semi-apex angle of the cone is "+ str(theta[-1]*180/math.pi))

# Checking









# Writing to data files (preferably .vtk files)
plot(np.array(theta)*180/math.pi, V_theta)
xlabel("Theta (in degrees)")
ylabel("V_theta")
show()


















