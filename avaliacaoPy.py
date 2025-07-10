from compileall import compile_file

print (" HBO MAX \n Planos a partir de R$18,90/mês")
print (" ESCOLHA O MELHOR PLANO PARA VOCÊ \n ")
print (" Básico com Anúncios \n ------------------ \n 2 dispositivos ao mesmo tempo \n Resolução Full HD \n 12x R$18,90/mês I Preço total anual R$226,80 \n")
print (" Standard \n ------------------ \n 2 dispositivos ao mesmo tempo \n Resolução Full HD \n 30 downloads para curtir off-line \n 12x R$29,90/mês I Preço total anual R$358,80 \n ")
print (" Platinum \n ------------------ \n 4 dispositivos ao mesmo tempo \n Resolução Full HD e 4K Ultra HD \nAúdio Dolby Atmos \n 100 downloads para curtir off-line \n 12x R$39,90/mês I Preço total anual R$478,80 \n")
# Dados e pagamento
print ("Escolha 1 para: Básico com Anúncios.")
print ("Escolha 2 para: Standart.")
print ("Escolha 3 para: Platinum.")
opcao = int(input("Digite um número para selecionar o plano desejado: \n "))
if opcao == 1:
    email = input("Endereço de e-mail: \n")
    nome = input("Digite seu nome: \n")
    cpf = int(input("Digite seu cpf: \n"))
    pagamento = input("digite a forma de pagamento(Débito,Crédito ou Pix):")

elif opcao == 2:
    email = input("Endereço de e-mail: \n")
    nome = input("Digite seu nome: \n")
    cpf = int(input("Digite seu cpf: \n"))
    pagamento = input("Digite a forma de pagamento: \n Débito \n Crédito \n Pix):")

else:
    email = input("Endereço de e-mail: \n")
    nome = input("Digite seu nome: \n")
    cpf = int(input("Digite seu cpf: \n"))
    pagamento = input("digite a forma de pagamento(Débito,Crédito ou Pix): \n")


print("Confirmação:", nome, " \n ", email," \n ", cpf, " \n ", pagamento, " \n ", " Pressione qualquer tecla para confirmar o plano!: " )














