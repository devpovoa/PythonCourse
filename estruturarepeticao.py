# 1. Imprima os números de 1 a 10 usando for.
for x in range(1, 11):
    print(x, end=", ")

# 2. Peça um número e exiba a tabuada dele de 1 a 10 usando while.
request_number = int(input('Informe um número: '))
contador = 1
while contador <= 10:
    print(f'{request_number} x {contador} = {request_number * contador}')
    contador += 1

# 3. Crie uma lista com 5 nomes e use for para imprimir um por linha.
namelist = []
counter = 1
while counter <= 5:
    namelist.append(input(f'Informe o {counter}. nome: '))
    counter += 1

print(f'{"=" * 10} Lista de Nomes {"=" * 10}')

for names in namelist:
    print(names.title().strip())
