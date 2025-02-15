senha = 'abcd1234'
senhaDigitada = ""

while senhaDigitada != senha:
    senhaDigitada = input('Digite a senha:')
    if senhaDigitada != senha:
        print('Senha incorreta')
        

print('Senha correta')