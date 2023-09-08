tinggi_piramida = 10

for i in range(1, tinggi_piramida + 1):
    for j in range(tinggi_piramida - i):
        print(" ", end="")
    
    for k in range(2 * i - 1):
        print("*", end="")
    print()