import random
cont = 0
while True:
    escolha = input('Escolha PAR ou IMPAR: ').strip().upper()
    numero = int(input('Escolha um número de 0 a 10: '))
    pc = random.randint(0, 10)
    print(pc)
    tot = pc + numero
    if escolha == 'PAR' and tot % 2 == 0 or escolha == 'IMPAR' and tot % 2 != 0:
        print('Vc venceu o computador!')
        cont += 1
    else:
        break
print(f'vc venceu {cont} vezes')
