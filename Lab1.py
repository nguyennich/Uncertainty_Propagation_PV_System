from os import P_ALL
from select import PIPE_BUF
from turtle import write_docstringdict
from uncertainties import ufloat
from uncertainties import umath
import numpy
import math
#from uncertainties.umath import 
p_d = ufloat(.0325, .0001)
p_m = ufloat(.035, .0006)
ac_d = ufloat(.0448, .00025)
ac_l = ufloat(.1125, .00025)
ah_d = ufloat(.0033, .00025)
ah_l = ufloat(.457, .001)
h_a = .025
h_b = .022
h_c = .065
h_d = .068
h_ap = .026
p_atm = 101325.0
p_nmass = p_m*9.81
p_mass = (.1+p_m)*9.81


V_ahac = (math.pi*((ac_d/2)**2)*ac_l) + (math.pi*((ah_d/2)**2)*ah_l)

V_a = V_ahac + math.pi*((p_d/2)**2)*h_a
P_a = p_atm+p_nmass

V_b = V_ahac + math.pi*((p_d/2)**2)*h_b
P_b = p_atm+p_mass

V_c = V_ahac + math.pi*((p_d/2)**2)*h_c
P_c = p_atm+p_mass

V_d = V_ahac + math.pi*((p_d/2)**2)*h_d
P_d = p_atm+p_nmass

V_ap = V_ahac + math.pi*((p_d/2)**2)*h_ap
P_ap = p_atm+p_nmass

#Thermodynamic work
W_ab = P_a*V_a*umath.log(((V_b)/V_a), math.e)
W_bc = P_b*(V_c - V_b)
W_cd = P_c*V_c*umath.log(((V_d)/V_c), math.e)
W_dap = P_d*(V_ap - V_d)
W_net = W_ab + W_bc + W_cd + W_dap
#print(W_ab)
#print(W_bc)
#print(W_cd)
#print(W_dap)
#print(W_net)

#Mechanical Work
F_ad = P_a*math.pi*((p_d/2)**2)
F_bc = P_b*math.pi*((p_d/2)**2)
MW_ab = F_ad*(h_b - h_a)
MW_bc = F_bc*(h_c - h_b)
MW_cd = F_bc*(h_d - h_c)
MW_dap = F_ad*(h_ap - h_d)
MW_net = MW_ab + MW_bc + MW_cd + MW_dap
print(MW_ab)
print(MW_bc)
print(MW_cd)
print(MW_dap)
print(MW_net)




