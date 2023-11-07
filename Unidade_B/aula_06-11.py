# interface grafica

import tkinter as tk


def mostrar_mensagem():
    label.config(text="Olá, IESGO! ")


def fechar_janela():
    janela.destroy()
    # fechar a janela. destroi a ação da janela


# criar uma janela
janela = tk.Tk()
janela.title("Exemplo de GUI em Python ")

# criar um rotulo
label = tk.Label(janela, text="Bem vindo á interface gráfica de usuário ")
label.pack(padx=10, pady=10)
label.config(width=100, height=20)

# criar um botao do tipo cta (call to action)
botao = tk.Button(janela, text="Click aqui!", command=mostrar_mensagem)
botao.pack(side=tk.LEFT, padx=10, pady=10)
# side=tk.left: No canto inferior esquerdo:
botao.config(width=10, height=0)

botao_fechar = tk.Button(janela, text="Fechar Janela", command=fechar_janela)
botao_fechar.pack(side=tk.RIGHT, padx=5, pady=5)
# side=tk.right: No canto inferior direito:
botao_fechar.config(width=10, height=0)


# iniciar a GUI em loop
janela.mainloop()
