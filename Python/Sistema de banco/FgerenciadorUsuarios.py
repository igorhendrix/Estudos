import json
import hashlib
import os
from datetime import datetime

ARQUIVO_USUARIOS = 'usuarios.json'

def fazer_login():
    usuario = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    # 1. Verifica se o arquivo de usuários existe
    if not os.path.exists(ARQUIVO_USUARIOS):
        print("Nenhum usuário cadastrado no sistema.")
        return False

    # 2. Carrega os usuários
    with open(ARQUIVO_USUARIOS, 'r', encoding='utf-8') as arquivo:
        usuarios = json.load(arquivo)

    # 3. Verifica se o e-mail existe na base de dados
    if usuario not in usuarios:
        print("E-mail não cadastrado!")
        return False

    # 4. Compara o hash da senha digitada com a senha armazenada
    senha_hash = criptografar_senha(senha)
    if usuarios[usuario]["senha"] == senha_hash:
        print(f"\nLogin realizado com sucesso! Bem-vindo(a), {usuario}!")
        return True
    else:
        print("Senha incorreta!")
        return False

def criptografar_senha(new_senha):
    # Transforma a senha em um Hash SHA-256 (Padrão de mercado)
    return hashlib.sha256(new_senha.encode()).hexdigest()

def criptografar_cpf(new_cpf):
    # Transforma a senha em um Hash SHA-256 (Padrão de mercado)
    return hashlib.sha256(new_cpf.encode()).hexdigest()

def validar_cpf(cpf):
    # Remove caracteres não numéricos (pontos e traço)
    cpf = ''.join([c for c in cpf if c.isdigit()])

    # Verifica se tem 11 dígitos ou se todos os dígitos são iguais (ex: "11111111111")
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    # Validação do 1º dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10) % 11
    if digito1 == 10:
        digito1 = 0
    if digito1 != int(cpf[9]):
        return False

    # Validação do 2º dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10) % 11
    if digito2 == 10:
        digito2 = 0
    if digito2 != int(cpf[10]):
        return False

    return True

def validar_data(data_str):
    try:
        # Tenta converter a string "dd/mm/aaaa" em um objeto datetime real
        datetime.strptime(data_str, "%d/%m/%Y")
        return True
    except ValueError:
        # Se o formato estiver errado ou for uma data inexistente (ex: 30/02), cai aqui
        print("Data inválida, tente novamente.\n")
        return False
    
def new_User():
    new_cpf = input("Digite seu CPF: ")

    while True:
        new_birth = input("Digite sua data de nascimento: ")
        if validar_data(new_birth):
            break

    new_usuario = input("Digite seu email: ")
    new_senha = input("Digite sua senha: ")

    # 1. Tenta carregar os usuários que já existem no arquivo
    usuarios = {}
    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, 'r', encoding='utf-8') as arquivo:
            usuarios = json.load(arquivo)

    # 2. Verifica se as informações do usuario já  está cadastrado
    if new_usuario in usuarios:
        print("Email já cadastrado!")
        return False

    #2.1 Validação de CPF
    
    if not validar_cpf(new_cpf):
        print("CPF inválido!")
        return False
    
    # 2.2 Verifica se o CPF já está cadastrado no arquivo (comparando hashes)
    cpf_hash = criptografar_cpf(new_cpf)
    for dados_usuario in usuarios.values():
        if dados_usuario.get("cpf") == cpf_hash:
            print("CPF já cadastrado!")
            return False

    # 3. Adiciona o novo usuário com senha criptografada
    usuarios[new_usuario] = {
        "senha" : criptografar_senha(new_senha),
        "saldo" : 0.0,
        "cpf" : criptografar_cpf(new_cpf),
        "nascimento" : new_birth
    }

    # 4. Salva tido no arquivo JSON
    with open(ARQUIVO_USUARIOS, 'w', encoding='utf-8') as arquivo:
        # indent=4 deixa o arquivo formatado e bonito para leitura
        json.dump(usuarios, arquivo, indent=4)

    print("Usuario criado!")
    return True
