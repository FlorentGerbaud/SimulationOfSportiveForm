###########################################                                        
# _____________ BIBLIOTHEQUES ___________ #
###########################################
import numpy as np
import time as time
import matplotlib.pyplot as plt

###########################################
# _____________ FONCTIONS _____________ #
###########################################

# Fonction qui renvoie le nombre d'entrainement par semaine
#param: E0 (float) : durée du plan en semaine
def E(E0):
    return E0

# Fonction qui renvoie la confiance de l'athlète
#param: C_t (float) : confiance de l'athlète à la semaine t
#param: E_t (float) : nombre d'entrainement de l'athlète à la semaine t
#param: alpha (float) : nombre d'entrainement de l'athlète réussie à la semaine t
def C(C_t,E_t, alpha,Vseuil,Ce,beta):
    if(E_t*beta>Vseuil):
        return C_t+max(-C_t,alpha*E_t)
    elif (E_t*beta<=Vseuil):
        print("ici")
        return max(C_t-Ce,0)

def F(F_t, C_t, E_t,beta):
    # return F_t+C_t+E_t-beta*E_t
    return F_t+max(-F_t-C_t,E_t*(1-beta))+C_t

def fatigue(E_t):
    return E_t*beta

############################# CI #####################
E0=4.0 #3 training by week
C0=1.0
F0=1.0
########################## Valeur fonction ###############
nbSemaine=52
valF=np.zeros(nbSemaine)
valC=np.zeros(nbSemaine)
valE=np.zeros(nbSemaine)
valFatigue=np.zeros(nbSemaine)
alpha=0.8 #séance réussite
beta=2.0
valC[0]=C0
valE[0]=E0
valF[0]=F0
Vseuil=6
Ce=0.03
valFatigue[0]=E0*beta
for dureePlan in range(1,nbSemaine):
    valE[dureePlan]=E0
    valF[dureePlan]=F(valF[dureePlan-1],valC[dureePlan-1],valE[dureePlan-1],beta)
    valC[dureePlan]=C(valC[dureePlan-1],valE[dureePlan-1],alpha,Vseuil,Ce,beta)
    valFatigue[dureePlan]=fatigue(valE[dureePlan-1])
    
print(valE[0]*beta)
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

