import math

print("Donner trois nombres a,b et c pour calculer l'equation ax² + bx + c = 0")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

delta = b**2 - 4*a*c

if delta < 0:
    print("Pas de solution reelle")
elif delta == 0:
    x = -b / (2*a)
    print(f"Une solution reelle: x = {x:.2f}")
else:
    x1 = (-b - math.sqrt(delta)) / (2*a)
    x2 = (-b + math.sqrt(delta)) / (2*a)
    print(f"Deux solutions reelles: x1 = {x1:.2f}, et x2 = {x2:.2f}")