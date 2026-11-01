# atividade 1

dia = 4
mes = 4
ano = 2003

print(f"Eu nasci em 0{dia}/0{mes}/{ano}")

# atividade 2
from datetime import datetime

def obter_hora_atual():
    agora = datetime.now() # data e hora atual
    hora_atual = agora.strftime("%H") 
    minuto_atual = agora.strftime("%M")
    ano_atual = agora.strftime("%Y")

    print(f"Agora são {hora_atual} horas e {minuto_atual} minutos")
    print(ano_atual)

obter_hora_atual()

# atividade 3

pi = 3.14159265359

def print_pi():
    print(f"PI é igual a: {pi:.5f}")

print_pi()