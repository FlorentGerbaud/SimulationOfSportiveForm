###########################################                                        
# _____________ BIBLIOTHEQUES ___________ #
###########################################
import numpy as np
import time as time
import matplotlib.pyplot as plt

######### Méthode qui défini le nombre d'entrainement par semaine de l'athlète
#param: E_t (float) : nombre d'entrainement de l'athlète à la semaine t
#return: nombre d'entrainement de l'athlète à la semaine t+1
def N(E_t):
    return E_t

#méthode qui défini la qualité d'entrainement de l'athlète
#param: E_t (float) : qualité des entrainement de l'athlète à la semaine t
#param: N_t (float) : nombre d'entrainement de l'athlète à la semaine t
#param: alpha (float) : nombre d'entrainement de l'athlète réussie à la semaine t
#param: beta (float) : fatigue/difficulté à récupérer d'un entrainement à la semaine t
#return: qualité des entrainement de l'athlète à la semaine t+1
def E(E_t,N_t,alpha,beta):
    E_tSuiv=E_t+N_t*(alpha-beta)
    if(E_tSuiv>1):
        return 1
    if(E_tSuiv<-1):
        return -1
    else :
        return E_tSuiv

#méthode qui défini le niveau de confiance de l'athlète
#param: C_t (float) : confiance de l'athlète à la semaine t
#param: E_t (float) : qualité des entrainement de l'athlète à la semaine t
#return: niveau de confiance de l'athlète à la semaine t+1
def C(C_t,E_t):
    C_tSuiv=C_t+max(-C_t,E_t)
    if(C_tSuiv>1):
        return 1
    else :
        return C_tSuiv

#méthode qui défini le niveau de succès des séances de l'athlète pour chaque semaine
#param: nbSeance (float) : nombre de séance par semaine
#param: p (float) : probabilité de réussite de toutes les séances
#param: nbSemaine (int) : nombre de semaine
#return: tableau avec le nombre de séance réussie chaque semaine
def fAlpha(nbSeance,p,nbSemaine):
    return np.random.binomial(nbSeance, p, size=nbSemaine)/nbSeance #permet d'obtenir le pourcentage de séance réussie

#méthode qui défini le niveau de fatigue de l'athlète pour une semaine
#param: niveauFatigueMoyen (float) : niveau de fatigue moyen de l'athlète
#return: niveau de fatigue de l'athlète pour une semaine
def fBeta(niveauFatigueMoyen):
    niveauFatigue = np.random.binomial(n=1, p=0.9)

    if niveauFatigue == 1:
        niveauFatigue = np.random.uniform(niveauFatigueMoyen-0.02, niveauFatigueMoyen+0.02)  # si succès, tirer un nombre uniformément entre 0 et 1
    else:
        niveauFatigue = np.random.uniform(0.0, 1.0)  # si échec, tirer un autre nombre uniformément entre 0 et 1
    return niveauFatigue

############################# CI #####################
nbSeance=3
N0=nbSeance/20.0
E0=0.5
C0=0.3
############################## Param #####################
nbSemaine=52
#param loi alpha(t)
moySeanceValide=0.7
valAlpha=fAlpha(nbSeance,moySeanceValide,nbSemaine)
#param loi beta(t)
niveauFatigueMoyen=0.5
valBeta=np.zeros(nbSemaine)
########################## Valeur fonction ###############

valN=np.zeros(nbSemaine)
valE=np.zeros(nbSemaine)
valC=np.zeros(nbSemaine)
valE[0]=E0
valN[0]=N0
valC[0]=C0
valBeta[0]=fBeta(niveauFatigueMoyen)

for dureePlan in range(1,nbSemaine):
    valBeta[dureePlan]=fBeta(niveauFatigueMoyen)
    valN[dureePlan]=N0
    valE[dureePlan]=E(valE[dureePlan-1],valN[dureePlan-1],valAlpha[dureePlan-1],valBeta[dureePlan-1])
    valC[dureePlan]=C(valC[dureePlan-1],valE[dureePlan-1])
    
####################### Affichage #####################

# Créer la figure et les deux axes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Tracer la première courbe sur le premier axe
ax1.plot(np.arange(0,nbSemaine,1),valE,label="qualité des entrainements",c="black")
ax1.plot(np.arange(0,nbSemaine,1),valC,label="niveau de confiance",c="blue",linestyle="dashed")
ax1.set_xlabel('Times in weeks')
ax1.legend()

# Tracer la deuxième courbe sur le deuxième axe
ax2.plot(np.arange(0,nbSemaine,1),valBeta,label="Fatigue générée par les entrainements",c="blue",linestyle="dashed")
ax2.plot(np.arange(0,nbSemaine,1),valAlpha,label="Réussite des séances",c="red")
ax2.set_xlabel('Times in weeks')
ax2.legend()


plt.show()





