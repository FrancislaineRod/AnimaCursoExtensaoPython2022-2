# comando input(): quero permitir que o usuário digite algo...
nome = input("Digite seu nome: ")
#pedir idade...
idade = int(input("Digite a sua idade: "))
#pedir o gênero
genero = input("Informe o seu gênero M-masculino, F-feminino, O-outros: ")

#comando de saída...exibir na tela
print(f"Boa Noite,seu nome é {nome}")
#mostrar idade...
print("Sua idade é {}".format(idade))
#mostrar gênero
print("Seu gênero é {}".format(genero))

#e se eu quisesse mostrar o DOBRO  da idade informada?
dobro = idade * 2
print("O dobro da idade informada é {}".format(dobro))

#estrutura condicional "se"(if)
#se a pessoa for maior de idade, mostre "você é maior de idade,ótimo!Já pode beber ou dirigir"
if idade>=18 and genero=="M":
  print("você é maior de idade,ótimo!Já pode beber ou dirigir e você também precisa/precisou prestar o serviço militar obrigatório")
elif idade>=18 and (genero=="F" or genero=="O"):
   print("você é maior de idade,ótimo!Já pode beber ou dirigir")
else:
  print("Você é xóven ainda,xóven ainda...")


print("vai ser execultado de qualquer jeito")