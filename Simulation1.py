###########################################                                        
# _____________ BIBLIOTHEQUES ___________ #
###########################################
import numpy as np
import time as time
import matplotlib.pyplot as plt

def E(E0):
    return E0

def C(C_t,E_t, alpha):
    return C_t+max(-C_t,alpha*E_t)

def F(F_t, C_t, E_t,beta):
    # return F_t+C_t+E_t-beta*E_t
    return F_t+max(-F_t-C_t,E_t*(1-beta))+C_t

def fatigue(E_t):
    return E_t*beta

############################# CI #####################
E0=3.0 #3 training by week
C0=1.0
F0=1.0
########################## Valeur fonction ###############
nbSemaine=52
valF=np.zeros(nbSemaine)
valC=np.zeros(nbSemaine)
valE=np.zeros(nbSemaine)
valFatigue=np.zeros(nbSemaine)
alpha=0.8 #séance réussite
beta=30.0
valC[0]=C0
valE[0]=E0
valF[0]=F0
valFatigue[0]=E0*beta
for dureePlan in range(1,nbSemaine):
    valE[dureePlan]=E0
    valF[dureePlan]=F(valF[dureePlan-1],valC[dureePlan-1],valE[dureePlan-1],beta)
    valC[dureePlan]=C(valC[dureePlan-1],valE[dureePlan-1],alpha)
    valFatigue[dureePlan]=fatigue(valE[dureePlan-1])
    

plt.plot(np.arange(0,nbSemaine,1),valF,label="Forme de l'athlète",c="blue")
plt.plot(np.arange(0,nbSemaine,1),valC,linestyle='dashed',label="Confiance de l'athlète",c="green")
plt.plot(np.arange(0,nbSemaine,1),valFatigue,label="fatigue",c="black")
plt.xlabel("times in weeks")
plt.legend()
plt.grid()
plt.title("Athlète avec beaucoup de confiance et une bonne forme qui récupère très mal")
plt.show()
# plt.plot(np.arange(0,nbSemaine,1),valE,':')
# plt.show()