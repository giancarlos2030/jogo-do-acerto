import tkinter as tk
from tkinter import messagebox
import random

janela = tk.Tk()
janela.title("Jogo do Acerto - Bem-vindo ao jogo.")


# Define o tamanho fixo da janela (500 pixels de largura por 400 pixels de altura)
janela.geometry("500x400")


# Variáveis para armazenar o nível escolhido
nivel = tk.IntVar()  # Usamos IntVar para armazenar um valor inteiro

# ... (funções iniciar_jogo e chutar)
def iniciar_jogo():
    global nivel, num_tentativas, numerosecreto, tentativas

    # Obtém o nível escolhido
    nivel_escolhido = nivel.get()

    try:
        num_tentativas = int(entry_tentativas.get())
        if nivel_escolhido not in (1, 2, 3) or num_tentativas <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida. Verifique o nível de dificuldade e o número de tentativas.")
        return

    if nivel_escolhido == 1:
        intervalo_min = 1
        intervalo_max = 10
    elif nivel_escolhido == 2:
        intervalo_min = 1
        intervalo_max = 50
    else:
        intervalo_min = 1
        intervalo_max = 100

    numerosecreto = random.randint(intervalo_min, intervalo_max)
    tentativas = 0
    label_resultado.config(text="")

def chutar():
    global tentativas
    try:
        chute = int(entry_chute.get())
    except ValueError:
        messagebox.showerror("Erro", "Chute inválido. Digite um número.")
        return

    tentativas += 1
    if chute == numerosecreto:
        label_resultado.config(text=f"Parabéns! Você acertou em {tentativas} tentativas.")
        botao_chutar.config(state=tk.DISABLED)
    elif tentativas == num_tentativas:
        label_resultado.config(text=f"Você perdeu! O número era {numerosecreto}.")
        botao_chutar.config(state=tk.DISABLED)
    elif chute > numerosecreto:
        label_resultado.config(text="Seu chute foi maior.")
    else:
        label_resultado.config(text="Seu chute foi menor.")

def reiniciar_jogo():
    # Limpa as entradas
    entry_tentativas.delete(0, tk.END)
    entry_chute.delete(0, tk.END)

    # Desmarca os radiobuttons
    nivel.set(0)

    # Limpa o label de resultado
    label_resultado.config(text="")

    # Habilita o botão "Iniciar"
    botao_iniciar.config(state=tk.NORMAL)


# ... (elementos da interface)
# Labels
label_nivel = tk.Label(janela, text="Nível de dificuldade:")
label_tentativas = tk.Label(janela, text="Tentativas (digite o número):")
label_chute = tk.Label(janela, text="Seu Chute:")
label_resultado = tk.Label(janela, text="Resultado")

# Entradas
entry_nivel = tk.Entry(janela)
entry_tentativas = tk.Entry(janela)
entry_chute = tk.Entry(janela)

# Radiobuttons para os níveis
facil_radio = tk.Radiobutton(janela, text="Fácil", variable=nivel, value=1)
medio_radio = tk.Radiobutton(janela, text="Médio", variable=nivel, value=2)
dificil_radio = tk.Radiobutton(janela, text="Difícil", variable=nivel, value=3)

# Botões
botao_iniciar = tk.Button(janela, text="Iniciar", command=iniciar_jogo)
botao_chutar = tk.Button(janela, text="Chutar", command=chutar)
botao_reiniciar = tk.Button(janela, text="Reiniciar", command=reiniciar_jogo)

# Layout (posicionando os elementos na janela)
label_nivel.grid(row=0, column=0)
facil_radio.grid(row=0, column=1)
medio_radio.grid(row=0, column=2)
dificil_radio.grid(row=0, column=3)
label_tentativas.grid(row=1, column=0)   # Linha 2, Coluna 0
entry_tentativas.grid(row=1, column=1)   # Linha 2, Coluna 2
label_chute.grid(row=2, column=0)        # Linha 3, Coluna 0
entry_chute.grid(row=2, column=1)        # Linha 3, Coluna 2
botao_iniciar.grid(row=3, column=0, columnspan=2)  # Linha 5, Coluna 0 (ocupa 2 colunas)
botao_chutar.grid(row=4, column=0, columnspan=2)   # Linha 6, Coluna 0 (ocupa 2 colunas)
botao_reiniciar.grid(row=5, column=0, columnspan=2)
label_resultado.grid(row=6, column=0, columnspan=2) # Linha 7, Coluna 0 (ocupa 2 colunas)


janela.mainloop()