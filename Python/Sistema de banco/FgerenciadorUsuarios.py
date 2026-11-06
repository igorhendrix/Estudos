import json
import hashlib
import os

ARQUIVO_USUARIOS = 'usuarios.json'

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

def new_User():
    new_cpf = input("Digite seu CPF: ")
    new_birth = input("Digite sua data de nascimento: ")
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


new_User()