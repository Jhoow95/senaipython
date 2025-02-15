# 1) Definir a variável da tabuada
# 2) Definir uma variável de contador - variar de 1 a 10
# 3) Criar um loop
# 4) Multiplicar as variáveis e guardar o resultado
# 5) Mostrar o resultado
# 6) Somar 1 ao valor do contador

tabuada   = 2
contador  = 1
resultado = 0

while resultado < 100 :
    resultado = tabuada * contador
    print(tabuada,'x',contador,'=',resultado)
    contador += 1

    if contador > 10:
        tabuada  += 1
        contador = 1
        print("")