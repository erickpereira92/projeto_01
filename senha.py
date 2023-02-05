usuarios = {
    "jorge": "12345",
    "usuario2": "senha2",
    "usuario3": "senha3"
}

def autenticar():
    tentativas = 3
    while tentativas > 0:
        username = input("Digite seu nome de usuário: ")
        password = input("Digite sua senha: ")
        if username in usuarios and usuarios[username] == password:
            print("Autenticação bem-sucedida.")
            break
        else:
            print("Nome de usuário ou senha inválidos.")
            tentativas -= 1
    if tentativas == 0:
        print("Você excedeu o número máximo de tentativas de login.")

autenticar()