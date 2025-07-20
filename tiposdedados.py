# 1. Crie três variáveis com os seguintes valores: um número inteiro, um número decimal e uma string. Use type() para imprimir o tipo de cada uma.
from decimal import Decimal

def customPress(value):
    print(f'{value} é do Type: {type(value)}')


numInt: int = 10
numDecimal = Decimal('3.14159')
nameString: str = "Thiago"
print(f'{"=" * 10} Tipos de variáveis {"=" * 10}')
for iterador in numInt, numDecimal, nameString:
    customPress(iterador)

# 2. Escreva um código que armazene True em uma variável e verifique seu tipo com type().
condBoolean: bool = True
customPress(condBoolean)

# 3. Crie um dicionário chamado pessoa com as chaves nome, idade e altura. Atribua valores e imprima o conteúdo.
personName: str = "Thiago"
personAge: int = 39
personHeight: float = 1.72

person = {
    'name': personName, 'age': personAge, 'height': personHeight,
}

print(f'{"=" * 10} Dicionários {"=" * 10}')
for key, value in person.items():
    print(f'{key}: {value}')
