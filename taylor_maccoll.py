# Solving Taylor-Maccoll equation

import math
def taylor_maccoll_eqn(theta, gamma, V_r, V_theta):
     
     num = (gamma-1)/2.0*(1-V_r**2 - V_theta**2)*(2*V_r + V_theta/math.tan(theta)) - V_r*V_theta**2
     denom = V_theta**2 - (gamma-1)/2.0*(1 - V_r**2 - V_theta**2)
     num/denom

     return [V_theta, num/denom]

def euler_step_integration(theta, del_theta, gamma, V_r, V_theta):
     
     rhs = taylor_maccoll_eqn(theta, gamma, V_r, V_theta)
     V_r = V_r + rhs[0]*del_theta;
     V_theta = V_theta + rhs[1]*del_theta
     
     return [V_r, V_theta]




def rk4_step_integration(theta, del_theta, gamma, V_r, V_theta):
     
     #k1 = 

     #k2 = 

     #k3 =

     #k4 =

     return True



