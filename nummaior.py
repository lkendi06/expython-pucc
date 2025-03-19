bigger = 0
secondbig = 0

for x in range (0,10):
    n=int(input("Digite um numero"))
    if n > bigger:
        secondbig = bigger
        bigger = n
    elif n > secondbig:
        secondbig = n
print("o maior numero é", bigger, "e o segundo maior é o",secondbig)