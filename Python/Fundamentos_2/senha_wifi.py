import subprocess  

# 1. PROCURANDO AS INFORMAÇÕES DA REDE CONECTADA
interfaces = subprocess.run(
    'netsh wlan show interfaces',
    capture_output=True,
    text=True,
    encoding="utf-8",
    shell=True
)

print(f"PRINTANDO INTERFACE {interfaces.stdout} \n\n ACABA AQUI")

# 2. PROCURANDO E SALVANDO O NOME DA REDE NAS INFORMAÇÕES
nome_rede = None

for linha in interfaces.stdout.splitlines():
    if "Perfil" in linha:
        nome_rede = linha.split(":")[1].strip()
        break

if nome_rede:
    print(f"Rede conectada {nome_rede}")

    
r = subprocess.run(
    f'netsh wlan show profile name="{nome_rede}" key=clear',
    capture_output=True,
    text=True,
    encoding="utf-8",
    shell=True)

for linha in r.stdout.splitlines():
    if "Conteúdo da Chave" in linha:
        print(linha.strip())


 