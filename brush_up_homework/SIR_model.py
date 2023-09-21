import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''Instruction: Modeling the spread of a disease (Covid).

The model has been designed to showcase the time that will take, for a group of people (10), 
to spread an infectious disease to the rest of the population (1000). 

Parameters & Assumptions:
Mandatory:
* Infection rate : 3 people / day
* probability of infection: 0.05
Additional:
* Adjusted propagation (Proportionally decreasing the susceptible population to the increase of the infected base)
* SIR Model: Recovered (6 days after infected, 90%) , dead(10%), Susceptible
* hospital avg capacity index : 2.96 beds per 1000 people --> 338 available beds

SIR Methodology: 
The SIR model shows the transition of people across multiple conditions/states resulting in a more accurate representation 
of the effects of a infectious disease in a given population.

1. Balance the increasing number of infections with recovery and death to yield a more realistic evolution of the disease.
2. Estimate the potential volume of dead people.
3. Estimate the time for the infection to end.
'''
# Infection Simulation

pop = 1000
base = 10
recovered = 0
days = 0
inf_dict = {'date':[0],'infected':[10]}
while base < 1000:
    infected = math.ceil((0.05*3)*base*(pop - base)/(pop))
    base = base + infected
    days = days + 1
    # Append values to dictionary
    inf_dict['date'].append(days)
    inf_dict['infected'].append(base)

df = pd.DataFrame(inf_dict)
df








## SIR MODEL / without Vaccine

#recovers = inf_dict['infected']
days = 7
inf_diction = {'date':[0,1,2,3,4,5,6],'recovers':[0,0,0,0,0,0,10],'dead':[0,0,0,0,0,0,1]}
recovers = 9
base = 10
dead = 1
while recovers <= 1000 :
    infected = math.ceil((0.05*3)*base*(pop - base)/(pop))
    recovery = math.ceil((0.05*3)*base*(pop - base)/(pop)*0.90)
    recovers = recovers + recovery
    deads  = math.ceil((0.05*3)*base*(pop - base)/(pop)*0.10)
    dead = dead + deads
    base = base + infected - deads
    days = days + 1
    inf_diction['date'].append(days)
    inf_diction['recovers'].append(recovers)
    inf_diction['dead'].append(dead)


#Generate Data Frame
df2 = pd.DataFrame(inf_diction)

## Join DataFrames
df_merge = df2.merge(df, on='date', how='left', indicator=True)
df_merge.tail(20)

#Calculate infection curve
df_merge['infect'] = df_merge['infected'] - df_merge['recovers'] - df_merge['dead']
# Add Susceptible population
df_merge['test'] = 1000 - df_merge['infected'] - df_merge['dead']
# Make infection curve higher than zero
df_merge['infect_n'] = np.where(df_merge['infect'] <0, 0, df_merge['infect'])
# Make susceptible curve higher than zero
df_merge['Susceptible'] = np.where(df_merge['test'] <0, 0, df_merge['test'])



#Final Plot


#plot both curves same chart
plt.plot(df_merge['date'], df_merge['infect_n'], color='r', label='infected')
plt.plot(df_merge['date'], df_merge['recovers'], color='g', label='recovers')
plt.plot(df_merge['date'], df_merge['dead'], color='b', label='dead')
plt.plot(df_merge['date'], df_merge['Susceptible'], color='y', label='susceptible')

# Naming the x-axis and y-axis
plt.xlabel("Date")
plt.ylabel("Infected,Recovers and Dead")

# Adding a title to the graph
plt.title("Covid Simulation")

# Adding a legend, which helps recognize the curve according to its color
plt.legend()

# Displaying the plot
plt.show()



