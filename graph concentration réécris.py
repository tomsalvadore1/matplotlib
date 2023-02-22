import matplotlib.pyplot as plt
import numpy as np

class bdd :
    def __init__(self): #initialisation de la base de données  
        self.eau = [0.75, 0.5, 0.75, 1.5, 1, 0.5, 0.4, 0.4, 0.4, 0.3]
        self.methanol = [0.75, 0.3, 0.3, 1.25, 1.75, 1, 0.2, 0.5, 0.2, 0]
        self.tcf = [0.5, 0.1, 0.3, 1.25, 1.4, 0.5, 0, 0, 0, 0]
        self.ethanol = [0.15, 0.1, 0.1, 0.1, 0.1, 0.2, 0.4, 1, 1.5, 0]
        self.glycerol = [0.4, 0.2, 0.2, 0.75, 1, 0.5, 0.2, 0.1, 0.1, 0.1]
        self.concentrationeau = None
        self.concentrationmethanol = None
        self.concentrationtcf = None
        self.concentrationethanol = None
        self.concentrationglycerol = None
        self.ordonneeeau = [0]*10
        self.ordonneemethanol = [0]*10
        self.ordonneetct = [0]*10
        self.ordonneeethanol = [0]*10
        self.ordonneeglycerol = [0]*10
        self.ordonnetotale = [0]*10

    def concentration(self): #input de l'utilisateur sur les 5 concentrations 
        self.concentrationeau = float(input("quelle concentration d'eau met-on dans la solution (unité arbitraire) ?\n"))
        self.concentrationmethanol = float(input("quelle concentration de methanol met-on dans la solution (unité arbitraire) ?\n"))
        self.concentrationtcf = float(input("quelle concentration de tcf met-on dans la solution (unité arbitraire) ?\n"))
        self.concentrationethanol = float(input("quelle concentration d'ethanol met-on dans la solution (unité arbitraire) ?\n"))
        self.concentrationglycerol = float(input("quelle concentration de glycerol met-on dans la solution (unité arbitraire) ?\n"))

    def ordonnée(self): #calcul des absorbances en fonction des concentrations données par l'utilisateur 
        for i in range(10):# d'abord pour chaque substance une par une 
            self.ordonneeeau[i] = self.eau[i] * self.concentrationeau
            self.ordonneemethanol[i] = self.methanol[i] * self.concentrationmethanol
            self.ordonneetct[i] = self.tcf[i] * self.concentrationtcf
            self.ordonneeethanol[i] = self.ethanol[i] * self.concentrationethanol 
            self.ordonneeglycerol[i] = self.glycerol[i] * self.concentrationglycerol

        for i in range(10):#maintenant on additionne toute les absorbances pour avoir l'absorbance de la solution
            self.ordonnetotale[i] = self.ordonneeeau[i] + self.ordonneemethanol[i] + self.ordonneetct[i] + self.ordonneeethanol[i] + self.ordonneeglycerol[i]

class plot :
    def __init__(self) :
        self.abcisse = range(300,800,50)#l'axe des abcisses 
        self.lambdamin=350# tout ca c'est pour la bande de couleur 
        self.lambdamax=800
        self.LO=np.arange(self.lambdamin, self.lambdamax, 1)
        self.cmap=plt.get_cmap('turbo')

    def tracage(self,n):
        plt.plot(self.abcisse,n,marker='x',color = "black", markerfacecolor='red',markeredgecolor='#cc0000')#parametres "reels" du plot
        for L in self.LO:#bande de couleur 
            plt.vlines(L, ymin = -0.1, ymax = 0.0, color=self.cmap((L-350)/(750-350)))
        plt.title("courbe d'absorbance de la solution crée")
        plt.ylabel("unité arbitraire de concentration")
        plt.xlabel("lambda")
        plt.show()


print ("ce programme a pour but de creer un spectre d'absorbtion a partir de données de concentrations données par l'utilisateur")
print("ma base de donnée est une simple image trouvée sur google dont je n'ai pas vérifié l'exactitude ")
ordonnee = bdd()
ordonnee.concentration()
ordonnee.ordonnée()
n = ordonnee.ordonnetotale
print(n)
graph = plot()
graph.tracage(n)