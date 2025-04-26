from funcoes import soma

print('Sistema Matemática')
num1 = input('Digite um numero: ')
num2 = input('Digite um numero: ')

resultado = soma(int(num1),int(num2))

print(f'A soma de {num1} e {num2} é {resultado}')