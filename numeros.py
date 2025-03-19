intervalo0_25 = 0
intervalo26_50 = 0
intervalo51_75 = 0
intervalo76_100 = 0


num=float(input("Digite um numero, ou um numero negativo para finalizar"))

#cria o laço de repetição, enquanto o numero for maior do que 0, ele segue um loop infinito
while num >= 0:


#Ja diz que caso o numero for menor do que 0, o programa termina 
    if num < 0:
        break

    if 0 <= num <= 25:
        intervalo0_25 += 1
    elif 26 <= num <= 50:
        intervalo26_50 += 1
    elif 51 <= num <= 75:
        intervalo51_75 += 1
    elif 76 <= num <= 100:
        intervalo76_100 += 1

    num=float(input("Digite um numero, ou um numero negativo para finalizar"))

print("quantidade de numero da saida (0,25)", intervalo0_25)
print("quantidade de numero da saida (26,50)", intervalo26_50)
print("quantidade de numero da saida (51,75)", intervalo51_75)
print("quantidade de numero da saida (76,100)", intervalo76_100)
        
    