n= int(input("entrer la taille de tableau T: "))
T= []

print(f"Remplir le tableau T par {n} valeurs entières:")
for i in range(n):
    x= int(input())
    T.append(x)
print(f"Les Valeurs De Tableau T Sont: {T}")

T.sort()
print(f"La Valeur Maximale De Tableau T est: {T[-1]}")
print(f"La Valeur Minimale De Tableau T est: {T[0]}")


paire= []
impaire= []

for i in range(n):
    if T[i]>0 and T[i]%2==0:
        paire.append(T[i])
    elif T[i]>0 and T[i]%2==1:
        impaire.append(T[i])

print(f"le nombre d'éléments strictement positifs et pairs est: {len(paire)}")
print(f"le nombre d'éléments strictement positifs et impairs est: {len(impaire)}")

TPOS= []
TNEG= []

for i in range(n):
    if T[i]>0:
        TPOS.append(T[i])
    else:
        TNEG.append(T[i])

print(f"le tableau TPOS: {TPOS}")
print(f"le tableau TNEG: {TNEG}")

p= int(input("entrer le nouveau nombre: "))
T.append(p)
T.sort()
print(T)

div= []

for i in range(n+1):
    if T[i]%3==0 and T[i]%5==0:
        continue
    elif T[i]%3==0:
        div.append(T[i])
    elif T[i]%5==0:
        div.append(T[i])

print(div)