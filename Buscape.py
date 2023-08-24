import random  # importamos a função random para gerar valores aleatórios.

print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= PROJETO DE PROCESSAMENTO DA INFORMAÇÃO =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

valor_frete = []                     # lista vazia para receber os fretes
valor = []                           # lista vazia para receber os preços
soma = []  # criamos uma variável para receber os valores da soma
s_total = []  # criamos para podermos depositar os todas as somas e poder realizar a consulta futuramente
selecao = []


lojas = ["Americanas", "Magazine Luiza", "Amazon", "Casas Bahia", "KaBuM",
         "Shopee", "Aliexpress", "Mercado Livre", "Fast Shop", "Nagem", "JbL"]

for i in range(0, 10):
    preco = random.uniform(60, 200)
    frete = random.uniform(0, 50)

    # random.choice(lojas) para fazer as escolhas dentro da lista(lojas) a cada interação(10) é armazenada na variável escolha
    escolha = random.choice(lojas)
    lojas.remove(escolha)
    # em seguida esse valor escolhido é removido da lista para que na próx interação ele não exista mais
    selecao.append(escolha)

    valor.append(preco)              # adicionar os preços em uma lista (valor)
    # adicionar os preços do frete em uma lista (valor_frete)
    valor_frete.append(frete)

    # colocamos [i] para que o loop percorra todos os índices da lista para realizar a soma, após isso adicionamos esse valor a váriavel soma
    soma = valor[i] + valor_frete[i]

    if soma != 0:  # já que todo resultado será diferente de 0 ele adicionarar todos os valores na lista s_total
        s_total.append(soma)
        print("Loja {} : {} - Caixa de Som - Preço:(R$:{:.2f}) - Frete:(R$:{:.2f}) - Total:(R$:{:.2f})".format
              (i+1, escolha, preco, frete, s_total[i]))
# (.format) com condição 2f para formatar apenas em duas casas decimais!
# (i+1) para a contagem de itens terminar em 10 e não 9
# frete,s_total[i] para que ele format todos os items da lista(s_total

print("\nO item que deseja foi encontrado nessas lojas:")
print(selecao)


# aqui recebemos o parametro de comparação, no caso o primeiro item da lista
menor_valor = s_total[0]
result = []

# criamos um loop do tamanho da lista/ utilizo a função Enumerate() para obter tanto o valor quanto o índice dele
for i, valor in enumerate(s_total):
    if valor < menor_valor:  # o loop irá percorrer todos os elementos da lista fazendo uma comparação
        menor_valor = valor             # e a cada interação ele é atualizado
        result = selecao[i]


print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("\n                             A Loja -", result,"Oferece o Melhor Preço! - R$: ({:.2f})".format(menor_valor))
print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
