def somaImposto(taxaDeImposto,custo):
    imposto = custo * (taxaDeImposto /100)
    custo_total = custo + imposto
    return custo_total

taxa = float(input("Digite a taxa de imposto sobre as vendas (em %): "))
valor_item = float(input("digite o custo do item: "))

valor_total = somaImposto(taxa, valor_item)
print("o valor total do item, com o imposto é: ", valor_total)