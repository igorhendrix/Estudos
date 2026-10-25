import subprocess  
import time
import os


intervalo_segundos = 0.5

while True:       
    # 1. PROCURANDO AS INFORMAÇÕES DA REDE CONECTADA
    interfaces = subprocess.run(
        'netsh wlan show interfaces',
        capture_output=True,
        text=True,
        encoding="utf-8",
        shell=True
    )

    nome_rede = None
    download_vel = None
    update_vel = None
    sinal = None

    for linha in interfaces.stdout.splitlines():
        if "Taxa de recepção (Mbps)" in linha:
            download_vel = linha.split(":")[1].strip()
            break
    for linha in interfaces.stdout.splitlines():
        if "Taxa de transmissão (Mbps)" in linha:
            update_vel = linha.split(":")[1].strip()
            break
    for linha in interfaces.stdout.splitlines():
        if "Sinal" in linha:
            sinal = linha.split(":")[1].strip()
            break
    
    os.system('cls')    
    
    print(f"D: {download_vel}Mbps")
    print(f"U: {update_vel}Mbps")
    print(f"S: {sinal}") 

    time.sleep(intervalo_segundos)