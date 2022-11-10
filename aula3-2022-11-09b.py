#criaçaõ de funções

preco = 1999.90

#Calculsr 5% de imposto, guardar na variável imposto e exibir
imposto = preco * 0.05
print(imposto)

preco2 = 100
imposto2 = preco2 * 0.05
print(imposto2)

#criar uma função calcular_Imposto() que calcula um imposto de 5% e retorna a quem pediu...
#Isso é a declaração da função(como ela funciona)
def calcular_Imposto(preco_produto):
  imposto = preco_produto * 0.07
  return imposto

#Aqui é o uso...aqui é o imposto a calcular...e exibir na tela
preco = 299
imposto = calcular_Imposto(preco)
print(f"Esse aqui é com a função (7%):{imposto}")

#Eplicação de variavel local x global
print(preco)
preco_produto = 100
print(preco_produto)

#Agora calcular imposto a alíquota agora é 7%
valores = [1.99, 25.50, 78.27, 1515.5]
#se eu quiser calcular o iposto destes quatro valores... e exibir na tela assim: "O imposto de ....é..."(1°. preço, 2°. imposto)
for valor in valores:
  print(f"O imposto de {valor} é {calcular_Imposto(valor)}")