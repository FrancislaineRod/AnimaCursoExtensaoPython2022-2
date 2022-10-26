# comando input(): quero permitir que o usuário digite algo...
nome = input("Digite seu nome: ")
#pedir idade...
idade = int(input("Digite a sua idade: "))

#comando de saída...exibir na tela
print(f"Boa Noite,seu nome é {nome}")
#mostrar idade...
print("Sua idade é {}".format(idade))

#e se eu quisesse mostrar o DOBRO  da idade informada?
dobro = idade * 2
print("O dobro da idade informada é {}".format(dobro))