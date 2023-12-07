#explicação 
print("Cofre")
#Guarda o valor da senha
senha = 2002
#Pedir a senha e a entrada
tentativa = int(input("Digite a senha: "))
#Ver se a senha colocada pelo usuário é a senha correta, se não for, pedir para manda a senha novamente
while tentativa != senha:
    print("Senha Invalida")
    tentativa = int(input("Digite a senha: "))
#se a senha colocada pelo usuário for a senha correta  acabar o código
print("Acesso permitido")