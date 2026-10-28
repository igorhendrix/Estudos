import subprocess  
import time
import os


intervalo_segundos = 1
primeira_execucao = True

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
            download_vel = linha.split(":")[-1].strip()
        elif "Taxa de transmissão (Mbps)" in linha:
            update_vel = linha.split(":")[-1].strip()
        elif "Sinal" in linha:
            sinal = linha.split(":")[-1].strip()
            break
    
    #os.system('cls')    
    
    if not primeira_execucao:
        print("\033[3A", end="")
    else:
        primeira_execuao = False


    print(f"D: {download_vel:<6} Mbps\033[K")
    print(f"U: {update_vel:<6} Mbps\033[K")
    print(f"S: {sinal:<6}\033[K", flush=True)

    time.sleep(intervalo_segundos)