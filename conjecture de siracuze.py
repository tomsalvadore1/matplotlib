import matplotlib.pyplot as plt

print("choisi ton nombre")
nombredebase = int(input())
abscisse = []
ordoné = []
j = [0]
i = [0]


while nombredebase != 1 :
    
    j[0] = j[0] + 1
    i[0] = nombredebase
    abscisse.extend(j)
    ordoné.extend(i)
    if nombredebase%2 == 0:
        nombredebase = nombredebase/2
        ordoné.extend
        print(nombredebase)
    elif nombredebase%2 ==1:
        nombredebase = (nombredebase*3) + 1
        print(nombredebase)
    if nombredebase == -5:
        break
    if nombredebase == -17:
        break
    if nombredebase == -1:
        break
plt.plot(abscisse,ordoné)
plt.show()