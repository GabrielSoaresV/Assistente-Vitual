from arduino import enviar
from voz import ouvir

print("Assistente iniciado")
print("Comandos:")
print("- digite: ligar luz | apagar luz | sair")
print("- ou diga: ligar luz / apagar luz")

while True:
    modo = input("\nDigite 'c' para comando ou 'v' para voz: ").lower()

    if modo == "c":
        entrada = input("> ").lower().strip()

    elif modo == "v":
        entrada = ouvir()

    else:
        print("Modo inválido")
        continue

    if entrada == "sair":
        break

    elif "ligar" in entrada:
        print(enviar("LED_ON"))

    elif "apagar" in entrada:
        print(enviar("LED_OFF"))

    else:
        print("Comando desconhecido")
