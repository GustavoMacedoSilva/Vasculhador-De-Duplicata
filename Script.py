import os
import tkinter as tk
from tkinter import filedialog

def caminhar_pela_pasta(pasta):
    #essa função, obviamente, vai caminhar pela pasta e pelas subpastas
    
    for raiz, subpastas, arquivos in os.walk(pasta):
        print (f"Raiz: {raiz}")
        if subpastas != None:
            print (f"subpasta: {subpastas}")
        else:
            print ("Não há subpastas")
        if arquivos != None:
            print (f"Arquivos: {arquivos}")
        else:
            print ("Não há arquivos")
        print ("-"*50)
        
        
def selecionar_root():
    raiz = filedialog.askdirectory()
    label1 = tk.Label(text="Pasta selecionada: " + raiz).pack()
    label2 = tk.Label(text="Deseja pesquisar nela? Ou deseja selecionar outra Root?").pack()
    botao_confirmar = tk.Button(janela, text="Pesquisar", command=lambda: caminhar_pela_pasta(raiz)).pack(pady=5)
    botao_selecionar_dnv = tk.Button(janela, text="Selecionar outra Root", command=selecionar_root).pack(pady=5)
    
# Cria a janela principal
janela = tk.Tk()
janela.title("Selecionar Root")
janela.geometry("450x300")

# Cria um botão para selecionar a pasta
button1 = tk.Button(janela, text="Selecionar a pasta Root", command=selecionar_root)
button1.pack(pady=20)

# Cria um botão para sair
button2 = tk.Button(janela, text="Sair", command=janela.quit)
button2.pack(pady=20)

# Labels que serão atualizados
label1 = tk.Label(janela, text="")
label1.pack()

label2 = tk.Label(janela, text="")
label2.pack()

# Inicia o loop principal da interface gráfica
janela.mainloop()