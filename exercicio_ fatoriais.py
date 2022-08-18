def fatorial(x: int, y: int):
    lista: list = [x]
    lista2: list = [y]
    """criação de listas para armazenar os fatoriais dos numeros e facilitar a multiplicaçao deles"""
    while x > 1 and y > 1:
        x -= 1
        lista.append(x)
        y -= 1
        lista2.append(y)
    produto1: int = 1
    for n in lista:
        produto1 *= n
    produto2: int = 1
    for a in lista2:
        produto2 *= a
    """criação de laços para multiplicar os fatoriais dos numeros informados que estão dentro das listas"""
    total: int = produto1 + produto2
    """finalizando o exercício com a soma das multiplicações dos fatoriais dos dois numeros"""
    return total


print('=' * 50)
num1 = int(input('informe um inteiro para o caculo do fatorial: '))
print('=' * 50)
num2 = int(input('informe outro inteiro para o calculo do fatorial: '))

resultado: int = fatorial(num1, num2)
print('=' * 50)
print(f'a soma dos fatoriais dos dois numeros ficou em {resultado}')
print('=' * 50)


