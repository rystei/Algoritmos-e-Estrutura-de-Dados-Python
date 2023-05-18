usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario == senha or senha.strip() == "":
    print("Acesso negado.")
else:
    print("Aaceso permitido.")