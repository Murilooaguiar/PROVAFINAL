#explicação
print("Descubre o valor do seu aumento.")
#Pedir para digitar o salario e a entrada
salario = float(input("Qual seu salário atual: "))
#Se o valor for menor que 0 pedir que o usuário digite o salario e a entrada novamente
while salario < 0:
    print('\nDigite um valor válido!')
    salario = float(input("Qual seu salário atual: "))
#Ver se o valor está entre 0 e 400 e fazer as ações necessárias.
if salario <= 400:
    print(f"Novo salário: {salario+(salario*(15/100)):.2f} \nReajuste ganho: {salario*(15/100):.2f} \nEm percentual: 15 %")
#Ver se o valor está entre 400R$ e 800R$ e fazer as ações necessárias.
elif salario > 400 and salario <= 800:
    print(f"Novo salário: {salario+(salario*(12/100)):.2f} \nReajuste ganho: {salario*(12/100):.2f} \nEm percentual: 12 %")
#Ver se o valor está entre 800R$ e 1200R$ e fazer as ações necessárias.
elif salario > 800 and salario <= 1200:
    print(f"Novo salário: {salario+(salario*(10/100)):.2f} \nReajuste ganho: {salario*(10/100):.2f} \nEm percentual: 10 %")
#Ver se o valor está entre 1200R$ e 2000R$ e fazer as ações necessárias.
elif salario > 1200 and salario <= 2000:
    print(f"Novo salário: {salario+(salario*(7/100)):.2f} \nReajuste ganho: {salario*(7/100):.2f} \nEm percentual: 7 %")
#Ver se o valor é maior do que 2000 e fazer as ações necessárias.
else:
    print(f"Novo salário: {salario+(salario*(4/100)):.2f} \nReajuste ganho: {salario*(4/100):.2f} \nEm percentual: 4 %")