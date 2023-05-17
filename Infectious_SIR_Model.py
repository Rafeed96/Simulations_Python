# Succeptible Infected Recovered ==> SIR Model

import scipy.integrate
import numpy
import matplotlib.pyplot as plt


def SIR_model(y, t, beta , gamma):
  S , I , R = y
  dS_dt = -beta*S*I
  dI_dt = beta*S*I - gamma*I
  dR_dt = gamma*I

  return([dS_dt, dI_dt, dR_dt,])