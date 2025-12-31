for i in range(1, 11):
    print("le table de multiplication de", i)
    print(" -------------------------")
    for j in range(1, 11):
        print(end=" | ")
        print(i, "x", j, "=", i * j)
    print(" ")