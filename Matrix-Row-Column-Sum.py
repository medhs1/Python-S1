l = int(input("Entrer le nombre des lignes: "))
c = int(input("Entrer le nombre des colonnes: "))

tab = []

for i in range(l):
    ligne =[]
    for j in range(c): 
        x = int(input(f"Entrer la valeur de ligne {i+1} colone {j+1} : "))
        ligne.append(x)
    tab.append(ligne)

print("\nRésultat:")
for i in range(l):
    for j in range(c):
        print(tab[i][j], end="\t") 
    print()

print("\n")

suml = 0
for i in range(l):
    for j in range(c):
        suml += tab[i][j]
    print(f"La somme de ligne {i+1} est: {suml} ")
    suml = 0

print("\n")

sumc = 0
for j in range(c):
    for i in range(l):
        sumc += tab[i][j]
    print(f"La somme de colonne {j+1} est: {sumc} ")
    sumc = 0