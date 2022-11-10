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
  imposto = preco_produto * 0.05
  return imposto

#Aqui é o uso...aqui é o imposto a calcular...e exibir na tela
preco = 299
imposto = calcular_Imposto(preco)
print(imposto)