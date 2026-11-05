import json
import hashlib
import os
ARQUIVO_USUARIOS = 'usuarios.json'

new_User()

def criptografar_senha(new_senha):
    # Transforma a senha em um Hash SHA-256 (Padrão de mercado)
    return hashlib.sha256(new_senha.encode()).hexdigest()


def new_User():
    #new_cpf = input("Digite seu CPF: ")
    #new_birth = input("Digite sua data de nascimento: ")

    new_usuario = input("Digite seu email: ")
    new_senha = input("Digite sua senha: ")

    # 1. Tenta carregar os usuários que já existem no arquivo
    usuarios = {}
    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, 'r', encoding='utf-8') as arquivo:
            usuarios = json.load(arquivo)

    # 2. Verifica se o email já  está cadastrado
    if new_usuario in usuarios:
        print("Email já cadastrado!")
        return False

    # 3. Adiciona o novo usuário com senha criptografada
    usuarios[new_usuario] = {
        "senha" : criptografar_senha(new_senha),
        "saldo" : 0.0
    }

    # 4. Salva tido no arquivo JSON
    with open(ARQUIVO_USUARIOS, 'w', encoding='utf-8') as arquivo:
        # indent=4 deixa o arquivo formatado e bonito para leitura
        json.dump(usuarios, arquivo, indent=4)

    print("Usuario criado!")
    return True


