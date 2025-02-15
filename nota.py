nota= int(input('Digite uma nota: '))

if nota > 10:
    print('Número invalido') 
elif nota >= 5: 
    print('Você foi aprovado')
elif nota >= 3:
    print('Você está de recuperação')
else:
    print('Você foi reprovado')

