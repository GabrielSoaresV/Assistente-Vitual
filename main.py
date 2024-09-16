import tkinter as tk
from tkinter import messagebox
import openai

# Substitua pela sua chave da API OpenAI
openai.api_key = 'sk-svcacct-_Rdn8iHwuFxcEAG1u96xRxVXZeN1BvNd-Vjrk9DYpk9dXT3BlbkFJ9qHtBVZLq5o5kf1NyqehZ8dt_soaP9obAUxhHFc5uTwKQA'

def enviar_mensagem():
    mensagem = entry.get()
    if mensagem:
        label.config(text="Aguarde, enviando mensagem...")
        resposta = obter_resposta_gpt(mensagem)
        label.config(text=f"ChatGPT: {resposta}")
        entry.delete(0, tk.END)
    else:
        print("Aviso", "Por favor, insira uma mensagem.")

def obter_resposta_gpt(pergunta):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Alterando para o modelo mais recente
            messages=[{"role": "user", "content": pergunta}],
            max_tokens=150
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return print(f"Erro ao se comunicar com o ChatGPT: {str(e)}")


# Criação da janela Tkinter
janela = tk.Tk()
janela.title("Enviar Mensagem para ChatGPT")

# Layout da janela
label = tk.Label(janela, text="Envie sua mensagem para o ChatGPT:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(janela, width=50)
entry.pack(pady=5)

botao_enviar = tk.Button(janela, text="Enviar", command=enviar_mensagem)
botao_enviar.pack(pady=10)

# Loop da interface gráfica
janela.mainloop()
