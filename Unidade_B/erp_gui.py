# classes em lib tkinter

import tkinter as tk
from tkinter import messagebox
import pesquisar_produto


def abrir_janela(mensagem):
    nova_janela = tk.Toplevel()
    nova_janela.title("Ação qualquer...")

    label = tk.Label(nova_janela, text=mensagem, padx=20, pady=20)
    label.pack()

    botao_fechar = tk.Button(nova_janela, text="Sair",
                             command=nova_janela.destroy)
    botao_fechar.pack(padx=20, pady=10)

# funções para as diferente funcionalidades do sistema ERP


def pesquisar_produto():
    abrir_janela("pesquisar Produto")


def chercar_estoque():
    abrir_janela("Checar estoque")


def acrescentar_estoque():
    abrir_janela("Acrescentar estoque")


def remover_estoque():
    abrir_janela("Remover do estoque")


def cadastrar_produto():
    abrir_janela("Cadastrar produto")

# criar a janela princiapal


janela_princial = tk.Tk()
janela_princial.title("Sistema ERP IESGO")
janela_princial.attributes('-fullscreen', False)
janela_princial.attributes('-disabled', False)


janela_princial.attributes()

# configurar icones do menu
# iconfinder site
icon_pesquisar = tk.PhotoImage(file="pesquisar.png")
icon_estoque = tk.PhotoImage(file="estoque.png")
icon_acrescentar = tk.PhotoImage(file="acrescentar.png")
icon_remover = tk.PhotoImage(file="remover.png")
icon_cadastrar = tk.PhotoImage(file="cadastrar.png")
# icon_check = tk.PhotoImage(file="checar.png")

# criar botoes com icones
botao_pesquisar = tk.Button(
    janela_princial, image=icon_pesquisar, command=pesquisar_produto)

botao__estoque = tk.Button(
    janela_princial, image=icon_estoque, command=chercar_estoque)

botao_acrescentar = tk.Button(
    janela_princial, image=icon_acrescentar, command=acrescentar_estoque)

botao_remover = tk.Button(
    janela_princial, image=icon_remover, command=remover_estoque)

botao_cadastrar = tk.Button(
    janela_princial, image=icon_cadastrar, command=cadastrar_produto)


# exibir os botoes na janela
botao_pesquisar.pack()

botao__estoque.pack()

botao_acrescentar.pack()

botao_remover.pack()

botao_cadastrar.pack()

# loop da janela princiapl
janela_princial.mainloop()
