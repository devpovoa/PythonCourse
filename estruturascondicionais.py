# 1. Peça um número e diga se ele é positivo, negativo ou zero.
check_number = int(input('Digite um número: '))

if check_number < 0:
    print(f'valor {check_number} é negativo!')
elif check_number > 0:
    print(f'valor {check_number} é positivo!')
else:
    print(f'valor {check_number} inserido.')

# 2. Solicite a nota de um aluno e diga se ele foi aprovado (nota ≥ 7), em recuperação (nota entre 5 e 6.9) ou reprovado (abaixo de 5).
check_condition = float(input('informe sua nota final: '))
if check_condition < 5:
    print(f'Sua sua nota final: {check_condition}. Infelizmente esta reprovado.')
elif (check_condition >= 5) and (check_condition < 7):
    print(f'Sua nota final: {check_condition}. Esta em recuperação.')
else:
    print(f'Sua nota final: {check_condition}. Com você foi Aprovado!.')

# 3. Peça a idade e informe se a pessoa é criança (até 12), adolescente (13–17), adulto (18–59) ou idoso (60+).
check_age = int(input('informe sua idade: '))
if check_age < 0:
    print('Idade infomada inválida')
elif (check_age > 0) and (check_age <= 12):
    print('criança')
elif (check_age >= 13) and (check_age <= 17):
    print('adolecente')
elif (check_age >= 18) and (check_age <= 59):
    print('adulto')
else:
    print('idoso')
