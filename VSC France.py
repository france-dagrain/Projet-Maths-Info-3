#Chargement des dépendances
import numpy as np
import math
import matplotlib as plt

#Discrétisation
A=0
B=500
N=101
Delta=(B-A)/(N-1)
discretization_indexes=np.arange(N)
discretization= discretization_indexes*Delta

#Paramètres du modèle
mu=-5
a=50
sigma2=12

#Données
observation_indexes=[0,20,40,60,80,100]
depth = np.array([0,-4,-12.8,-1,-6.5,0])

#Indices des composantes correspondant aux observations et aux componsantes non observées

unknown_indexes=list(set(discretization_indexes)-set(observation_indexes))


print(discretization_indexes)




