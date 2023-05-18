print("Neste algoritmo será realizado o calculo de quantas quilocalorias gastas.")
print("Desses exercicios: Natação, Caminhada, Corrida e Ciclismo, qual destas atividades você gostaria de saber?")
explicar = str(input(": "))
if explicar == "Natação" or explicar == "natação":
    print("A natação é um esporte no qual envolve o uso da água para os exercícios, muito bom para pessoas com sobrepeso")
elif explicar == "Caminhada" or explicar == "caminhada":
    print("Uma boa e velha caminhada, para pessoas que preferem apreciar a paisagem e se exercitar ao mesmo tempo")
elif explicar == "Corrida" or explicar == "corrida":
    print("Um pouco parecido a caminhada, correr é uma atividade mais intensa e que gasta mais calorias")
elif explicar == "Ciclismo" or explicar == "ciclismo":
    print("Ciclismo é um esporte que envolve o uso de bicicletas, muito bom para o condicionamento físico.")
else:
    print("Opção não existente!")


ativade = str(input("Qual dessas atividade você normalmente faz?: "))
tempo = int(input("E quantos tempo você pratica esse exercicio? (Em minutos): "))
calorias = 0
if tempo < 0:
    print("Tempo invalido!")
else:
    if ativade == "Natação" or ativade == "natação":
        calorias = 3.75 * tempo
        print("Você gastou", calorias,"calorias fazendo essa atividade!")
    elif ativade == "Caminhada" or "caminhada":
        calorias = 4.08 * tempo
        print("Você gastou", calorias, "calorias fazendo essa atividade!")
    elif ativade == "Corrida" or "corrida":
        calorias = 9.58 * tempo
        print("Você gastou", calorias, "calorias fazendo essa atividade!")
    elif ativade == "Ciclismo" or "ciclismo":
        calorias = 6.16 * tempo
        print("Você gastou", calorias, "calorias fazendo essa atividade!")
    else:
        print("Erro: Atividade não registrada!")