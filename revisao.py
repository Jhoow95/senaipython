# Entrada
numero1 = (input('Digite um número: '))
numero2 = (input('Digite outro nuúmero: '))
print('Qual operação você deseja? Digite ')
print('A - Adição')
print('S - Subtração')
print('M - Multiplicação')
print('D - Divisão')
print('E - Exponenciação')
operacao = input('Qual sua escolha? ')

# Processamento
resultado = 0
if(operacao.upper() == 'A'):
    resultado = float(numero1) + float(numero2)

elif (operacao.upper() == 'S'):
    resultado = float(numero1) - float(numero2)

elif(operacao.upper() == 'M'):
    resultado = float(numero1) * float(numero2)

elif(operacao.upper() == 'D'):
    resultado = float(numero1) / float(numero2)

elif(operacao.upper() == 'E'):
    resultado = float(numero1) ** float(numero2)
else:
    print('Opção invalida')
# Saída
print('O resultado é: ',resultado)
