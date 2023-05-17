# Succeptible Infected Succeptible ==> SIS Model

import matplotlib.pylab as plt

N = 10000  # Total population
S = N - 1  # Initial susceptible Population
I = 1  # Initial infected population
beta = 0.2  # Describes the infection rate of the disease.
gamma = 0.04  # Describes recovery rate.
T = 365  # Number Of Days



#Compartments
susceptible = [] 
infected = []

def funcSIS(S, I, N, T):
    for t in range (0, T):
        S,I = S - (beta*S*I/N) + gamma * I , I + (beta*S*I/N) - gamma * I

        susceptible.append(S)
        infected.append(I)



funcSIS(S, I, N , T)


plt.plot(susceptible,color = 'darkblue',label = 'Susceptible')
plt.plot(infected,color = 'red',label = 'infected')
plt.title('SIS Model')
plt.legend()
plt.xlabel('Day')
plt.ylabel('Population')
plt.show()