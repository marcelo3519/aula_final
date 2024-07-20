import tkinter as tk
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt

# Conectar ao banco de dados (será criado se não existir)
conexao = sqlite3.connect('meu_banco_de_.db')
cursor = conexao.cursor()

# Criar a tabela se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pessoas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        cidade TEXT NOT NULL
    )
''')
conexao.commit()



# criar a extrutura que mostrara o banco de dados
def inserir_dados():
    nome = entrada_nome.get()
    idade = entrada_idade.get()
    cidade = entrada_cidade.get()

    if nome and idade.isdigit() and cidade:
       cursor.execute('''
              INSERT INTO pessoas(nome, idade, cidade)
              VALUES (?, ?, ?)
              ''',(nome, idade, cidade))

       conexao.commit()  
       messagebox.showinfo('showinfo','Dados Inseridos')
       entrada_nome.delete(0,tk.END)
       entrada_idade.delete(0,tk.END)
       entrada_cidade.delete(0,tk.END)
    else:
       messagebox.showwarning('showwarning', 'Algo deu Errado')



# Função para exibir dados em um gráfico
def exibir_grafico():
    cursor.execute('SELECT nome, idade FROM pessoas')
    dados = cursor.fetchall()
    
    if dados:
        nomes = [dado[0] for dado in dados]
        idades = [dado[1] for dado in dados]

        plt.figure(figsize=(10, 5))
        plt.bar(nomes, idades, color='skyblue')
        plt.xlabel('Nome')
        plt.ylabel('Idade')
        plt.title('Idade das Pessoas')
        plt.show()
    else:
        messagebox.showwarning("Erro", "Nenhum dado encontrado para exibir.")





# Criar a janela principal
janela = tk.Tk()
janela.title("Cadastro de Pessoas")

# Rótulos e campos de entrada
tk.Label(janela, text="Nome:").grid(row=0, column=0, padx=10, pady=5)
entrada_nome = tk.Entry(janela)
entrada_nome.grid(row=0, column=1, padx=10, pady=5)

tk.Label(janela, text="Idade:").grid(row=1, column=0, padx=10, pady=5)
entrada_idade = tk.Entry(janela)
entrada_idade.grid(row=1, column=1, padx=10, pady=5)

tk.Label(janela, text="Cidade:").grid(row=2, column=0, padx=10, pady=5)
entrada_cidade = tk.Entry(janela)
entrada_cidade.grid(row=2, column=1, padx=10, pady=5)

# Botões
btn_inserir = tk.Button(janela, text="Inserir Dados", command=inserir_dados)
btn_inserir.grid(row=3, column=0, columnspan=2, pady=10)

btn_grafico = tk.Button(janela, text="Exibir Gráfico", command=exibir_grafico)
btn_grafico.grid(row=4, column=0, columnspan=2, pady=10)

# Iniciar o loop da aplicação
janela.mainloop()

# Fechar a conexão ao banco de dados quando a janela for fechada
conexao.close()
