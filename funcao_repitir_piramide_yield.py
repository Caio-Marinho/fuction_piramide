import time
def repetir(texto, n):
    resultado = ''
    for i in range(n):
        resultado += texto
    return resultado
    
def piramide(n):
    for i in range(1, n + 1):
        espaco = repetir('*', n - i)
        caracter = repetir(str(i), 2 * i - 1)
        yield espaco + caracter

n = int(input("Digite o tamanho da pirâmide: "))
for i in piramide(n):
    print(i)
    time.sleep(1)

input("\nPressione qualquer tecla para encerrar!")
