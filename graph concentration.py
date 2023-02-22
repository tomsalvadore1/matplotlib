import matplotlib.pyplot as plt
import numpy as np

lambdamin=350
lambdamax=750
LO=np.arange(lambdamin, lambdamax, 1)
cmap=plt.get_cmap('turbo')

eau = [0.75, 0.5, 0.75, 1.5, 1, 0.5, 0.4, 0.4, 0.4, 0.3]
methanol = [0.75, 0.3, 0.3, 1.25, 1.75, 1, 0.2, 0.5, 0.2, 0]
tcf = [0.5, 0.1, 0.3, 1.25, 1.4, 0.5, 0, 0, 0, 0]
ethanol = [0.15, 0.1, 0.1, 0.1, 0.1, 0.2, 0.4, 1, 1.5, 0]
glycerol = [0.4, 0.2, 0.2, 0.75, 1, 0.5, 0.2, 0.1, 0.1, 0.1]
ordonne = [0,0,0,0,0,0,0,0,0,0]
abcisseeau = [0,0,0,0,0,0,0,0,0,0]
abcissemethanol = [0,0,0,0,0,0,0,0,0,0]
abcissetcf = [0,0,0,0,0,0,0,0,0,0]
abcisseethanol = [0,0,0,0,0,0,0,0,0,0]
abcisseglycerol = [0,0,0,0,0,0,0,0,0,0]
abcisse = []

print("ce programme vous permet de dessiner une courbe d'absorbance d'une solution contenant des concentrations données d'eau, de methanol, de tcf, d'ethanol, et de glycerol")

concentrationeau = float(input("quelle concentration d'eau met-on dans la solution (unité arbitraire) ?\n"))
concentrationmethanol = float(input("quelle concentration de methanol met-on dans la solution (unité arbitraire) ?\n"))
concentrationtcf = float(input("quelle concentration de tcf met-on dans la solution (unité arbitraire) ?\n"))
concentrationethanol = float(input("quelle concentration d'ethanol met-on dans la solution (unité arbitraire) ?\n"))
concentrationglycerol = float(input("quelle concentration de glycerol met-on dans la solution (unité arbitraire) ?\n"))

for i in range(10):

    abcisseeau[i] = eau[i] * concentrationeau
    abcissemethanol[i] = methanol[i] * concentrationmethanol
    abcissetcf[i] = tcf[i] * concentrationtcf
    abcisseethanol[i] = ethanol[i] * concentrationethanol 
    abcisseglycerol[i] = glycerol[i] * concentrationglycerol

for i in range(10):
    ordonne[i] = abcisseeau[i] + abcisseethanol[i] + abcisseglycerol[i] + abcissemethanol[i] + abcissetcf[i]
    abcisse.append(50*i)
    abcisse[i] = abcisse[i] + 300




print(ordonne)
print(abcisse)

plt.plot(abcisse,ordonne,marker='x',color = "black", markerfacecolor='red',markeredgecolor='#cc0000')
for L in LO:
     plt.vlines(L, ymin = -0.1, ymax = 0.0, color=cmap((L-350)/(750-350)))

plt.title("courbe d'absorbance de la solution crée")
plt.ylabel("unité arbitraire")
plt.xlabel("lambda")
plt.show()