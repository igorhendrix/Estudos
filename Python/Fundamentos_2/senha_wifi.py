import subprocess  

nome = "Correia_5G"

r = subprocess.run(
    f'netsh wlan show profile name="{nome}" key=clear',
    capture_output=True,
    text=True,
    encoding="utf-8",
    shell=True)

print(r.stdout)

for linha in r.stdout.splitlines():
    if "Conteúdo da Chave" in linha:
        print(linha.strip())


 