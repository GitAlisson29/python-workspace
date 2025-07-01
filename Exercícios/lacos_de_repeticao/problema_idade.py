print("Dados da primeira pessoa:")
nome = input("Nome: ")
idade = int(input("Idade: "))

print("Dados da segunda pessoa:")
segundo_nome = input("Nome: ")
segundo_idade = int(input("Idade: "))

media = (idade + segundo_idade) / 2

print("A idade média de ", nome, " e ", segundo_nome, " é de ", "{:.1f}".format(media), " anos ")
