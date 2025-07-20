# 1. Armazene seu nome, idade e cidade em três variáveis diferentes e imprima uma frase usando esses dados.
name: str = 'Thiago'
age: int = 39
city: str = 'Rio de Janeiro'
message = (f'Olá {name}, hoje o clima no {city} '
           f'está perfeito para uma caminhada a beira da praia, '
           f'vamos fazer valer esses {age} anos.')
print(message)


# 2. Troque os valores de duas variáveis entre si (ex: a = 10, b = 20 → a = 20, b = 10).
def customPress(x, y):
    print(f'Valor atual de a = {x} e de b = {y}')


a: int = 10
b: int = 20
customPress(a, b)

# aux: int = a
# a = b
# b = aux
# customPress(a, b)

a, b = b, a
customPress(a, b)

# 3. Crie uma variável com o valor 100, depois aumente esse valor em 25 e imprima o novo resultado.
numValue = 100
print(f'Valor atual {numValue}')
numValue += 25
print(f'O novo valor é {numValue}')

