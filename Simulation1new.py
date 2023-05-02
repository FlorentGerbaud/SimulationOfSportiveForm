###########################################                                        
# _____________ BIBLIOTHEQUES ___________ #
###########################################
import numpy as np
import time as time
import matplotlib.pyplot as plt

######### Méthode qui défini le nombre d'entrainement par semaine de l'athlète
def N(E_t):
    return E_t

#méthode qui défini la qualité d'entrainement de l'athlète
def E(E_t,N_t,alpha,beta):
    E_tSuiv=E_t+N_t*(alpha-beta)
    if(E_tSuiv>1):
        return 1
    if(E_tSuiv<-1):
        return -1
    else :
        return E_tSuiv

#méthode qui défini le niveau de confiance de l'athlète
def C(C_t,E_t):
    C_tSuiv=C_t+max(-C_t,E_t)
    if(C_tSuiv>1):
        return 1
    else :
        return C_tSuiv

############################# CI #####################
N0=3/20
E0=0.0
C0=0.0
############################## Param #####################
alpha=0.7
beta=0.5
########################## Valeur fonction ###############
nbSemaine=52

valN=np.zeros(nbSemaine)
valE=np.zeros(nbSemaine)
valC=np.zeros(nbSemaine)
valE[0]=E0
valN[0]=N0
valC[0]=C0

for dureePlan in range(1,nbSemaine):
    valN[dureePlan]=N0
    valE[dureePlan]=E(valE[dureePlan-1],valN[dureePlan-1],alpha,beta)
    valC[dureePlan]=C(valC[dureePlan-1],valE[dureePlan-1])
    
print(valE)
print(valC)
plt.plot(np.arange(0,nbSemaine,1),valE,label="qualité des entrainements",c="black")
plt.plot(np.arange(0,nbSemaine,1),valC,label="niveau de confiance",c="blue",linestyle="dashed")
plt.xlabel("Times in weeks")
plt.legend()
plt.grid()
plt.show()
