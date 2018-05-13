# Oblique shock wave properties

import math

def oblique_shock_wave_properties(M_1, beta, gamma):
    
    beta = beta*math.pi/180

    # Flow deflection angle
    tan_theta = (2/math.tan(beta))*(M_1**2*(math.sin(beta))**2 - 1)/(M_1**2*(gamma + math.cos(2*beta)) + 2) 
    theta = math.atan(tan_theta)

    # Normal components
    M_n1 = M_1*math.sin(beta)
    M_n2 = math.sqrt((M_n1**2*(gamma - 1) + 2)/(2*gamma*M_n1**2 - (gamma - 1)))
    M_2 = M_n2/math.sin(beta - theta)

    return [M_2, theta, beta];


if __name__ == "__main__": 
   M_1 = float(input("Enter the value of freestream Mach number: "))
   gamma = float(input("Enter the value of gamma: "))
   beta = float(input("Enter the value of shock wave angle (in degrees): "))

   [M_2, theta, beta]  = oblique_shock_wave_properties(M_1, beta, gamma)
   theta = theta*180/math.pi
   print("M_2= " + str(M_2))
   print("theta = " + str(theta))

