import os
import tkinter as tk
from tkinter import filedialog

def caminhar_pela_pasta(pasta):
    #essa função, obviamente, vai caminhar pela pasta e pelas subpastas
    janela2 = tk.Tk()
    janela2.title("Resultado da Pesquisa")
    janela2.geometry("650x300")
    
    scrollbar = tk.Scrollbar(janela2)
    scrollbar.pack(side="right", fill="y")
    
    caixa_texto = tk.Text(janela2, yscrollcommand=scrollbar.set)
    caixa_texto.pack(expand=True, fill="both")
    
    scrollbar.config(command=caixa_texto.yview)
    
    for raiz, subpastas, arquivos in os.walk(pasta):
        caixa_texto.insert("end", f"Raiz: {raiz}\n")
        caixa_texto.insert("end", f"Subpastas: {subpastas}\n")
        caixa_texto.insert("end", f"Arquivos: {arquivos}\n\n")
        caixa_texto.see("end")
        janela2.update()
        
    caixa_texto.insert("end", "Varredura Concluída!\n")
    
        
        
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