# 1. Peça dois números e exiba o resultado das quatro operações básicas entre eles.
import operator

prompter_num1 = float(input('Digite o primeiro operando : '))
prompter_num2 = float(input('Digite o segundo operando : '))

def customSum(x, y):
    output = f'{x} + {y} = {operator.add(x, y)}'
    return output

def customSub(x, y):
    output = f'{x} - {y} = {operator.sub(x, y)}'
    return output

def customMul(x, y):
    output = f'{x} x {y} = {operator.mul(x, y)}'
    return output

def customDiv(x, y):
    output = f'{x} / {y} = {operator.truediv(x, y)}'
    return output

print(customSum(prompter_num1, prompter_num2))
print(customSub(prompter_num1, prompter_num2))
print(customMul(prompter_num1, prompter_num2))
print(customDiv(prompter_num1, prompter_num2))

# 2. Verifique se um número informado pelo usuário é par ou ímpar.
num_info = int(input('Digite o número: '))
if num_info % 2 == 1:
    print(f'O número {num_info} é ímpar.')
else:
    print(f'O número {num_info} é par.')

# 3. Solicite a idade de uma pessoa e verifique se ela tem entre 18 e 30 anos e se tem carteira de motorista (pergunte com input se sim ou não).
check_age = int(input('Informe sua idade: '))
if (check_age > 17) and (check_age < 31):
    check_have_license = input('Possui carteira de motorista? (sim/não): ').strip().lower()
    if check_have_license == 'sim':
        print("Ótimo ....")
    else:
        print("Você já pode tirar sua carteira de motorista.")
else:
    print(f'Obrigado pela informação!')
