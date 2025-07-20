# 1. Peça ao usuário que digite seu nome e exiba uma mensagem de boas-vindas com o nome.
from itertools import count

prompter_user = input('Digite seu nome: ').strip().title()
message = f'Boa-vindas {prompter_user}!'
print(message)

# 2. Solicite dois números e exiba a soma deles.
prompter_value1 = float(input('Digite o primeira valor: '))
prompter_value2 = float(input('Digite o segunda valor: '))

soma = sum([prompter_value1, prompter_value2])

print(f'A soma dos valor de {prompter_value1} + {prompter_value2} = {soma}')

# 3. Receba a idade do usuário e exiba quantos anos ele terá em 10 anos.
prompter_age = int(input('Digite a idade: '))

prevision = sum((prompter_age, 10))
print(f'Sua idade em 10 anos: {prevision}')