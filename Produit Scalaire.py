print("Programme de calcul d'un produit scalaire de deux vecteurs.")
print()

V1= []
V2= []

N= int(input("Entrer la taille de vos veteurs: "))


print(f"Entrer {N} elements de votre veteur V1: ")
for i in range(N):
    V1.append(int(input("")))

print(f"Entrer {N} elements de votre veteur V2: ")
for i in range(N):
    V2.append(int(input("")))

Produit_scalaire= 0
for i in range(N):
    Produit_scalaire += V1[i]*V2[i]

print(f"Le Produit Scalaire est {Produit_scalaire}")