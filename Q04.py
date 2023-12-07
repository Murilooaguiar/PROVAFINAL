#explicação
print("Descubra de onde é seu DDD\n")
#Pedir o número de telefone do usuário
numero = int(input(f"Digite seu número de telefone(Brasileiro) \nObs: Não utilize espaços e nem sinais: "))
#Salvar os dois primeiros dígitos do número de telefone na variável numero
numero = int(str(numero)[:2])
#Compara os dois primeiros dígitos do número de telefone e identifica seu DDD
if numero == 61:
    print("Brasília")
elif numero == 71:
    print("Salvador")
elif numero == 11:
    print("São Paulo")
elif numero == 21:
    print("Rio de Janeiro")
elif numero == 32:
    print("Juiz de Fora")
elif numero == 19:
    print("Campinas")
elif numero == 27:
    print("Vitória")
elif numero == 31:
    print("Belo Horizonte")
else:
    print("DDD não cadastrado")