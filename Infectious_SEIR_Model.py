# Succeptible Exposed Infected Recovered ==> SEIR Model

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# 0 = No social distancing
# 0.1 = Masks
# 0.2 = Masks and hybrid classes
# 0.3 = Masks and hybrid classes and online classes

u = 0.1   # Social Distancing Rate = (0-1)
t_incubation = 5.1
t_infective = 3.3
R0 = 2.4  # 
N = 33517 # student population
