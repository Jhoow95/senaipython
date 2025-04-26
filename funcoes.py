def soma(a, b):
    return a + b 

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):    
    resultado = 0
    for _ in range(b):
        resultado = soma(resultado, a)
    return resultado

def potencia(a, b):
    resultado = 1
    for _ in range(b):
        resultado = multiplicacao(resultado, a)
    return resultado