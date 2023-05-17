# Succeptible Infected Recovered ==> SIR Model

import scipy.integrate
import numpy
import matplotlib.pyplot as plt


def SIR_model(y, t, beta, gamma):
    S, I, R = y
    dS_dt = -beta*S*I
    dI_dt = beta*S*I - gamma*I
    dR_dt = gamma*I

    return ([dS_dt, dI_dt, dR_dt,])


# Initial Conditions
S0 = 0.99
I0 = 0.01
R0 = 0.0
beta = 0.35
gamma = 0.1


# Time vector
t = numpy.linspace(0, 100, 10000)

# result
solution = scipy.integrate.odeint(
    SIR_model, [S0, I0, R0], t, args=(beta, gamma))
solution = numpy.array(solution)



#plot
plt.figure(figsize=[6, 4])
plt.plot(t, solution[:, 0], label="S(t)")
plt.plot(t, solution[:, 1], label="I(t)")
plt.plot(t, solution[:, 2], label="R(t)")

plt.legend()
plt.xlabel("Time")
plt.ylabel("Proportion")
plt.show()