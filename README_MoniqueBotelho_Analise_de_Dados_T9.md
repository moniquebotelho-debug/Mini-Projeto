ETAPA 1: PREPARANDO O COMPUTADOR

1.1 Após a instalação já realizada anteriormente do VS Code e do Python confira se deu certo através do terminal escrevendo: python --version

1.2 Criar e abrir a pasta do projeto:
- Criar uma pasta chamada Mini_projeto no computador;
- No VS Code, vá em Arquivo → Abrir Pasta... e escolha a pasta Mini_projeto;
- Abra o terminal do VS Code em Terminal → Novo Terminal (ou Ctrl+').

1.3 Criar o ambiente virtual (venv):
- No terminal do VS Code, dentro da pasta do projeto, crie o ambiente escrevendo: python -m venv .venv ;
- Depois, ative o ambiente escrevendo no terminal: ..venv\Scripts\Activate.ps1 ;
- O começo da linha do terminal deverá passar a mostrar (.venv).

1.4 Instalar as bibliotecas no terminal: pip install pandas; pip install rich .

ETAPA 2 - IMPORTAÇÃO DE DADOS

2.1 Realizar a importação dos dados na plataforma Kaggle (base_varejo.csv) para o IDE do VS Code, dentro da pasta Mini Projeto.

ETAPA 3 - CARREGAR OS DADOS
3.1 Criar a classe carrega_dados.py;
3.2 Carregar a bibilioteca pandas: import pandas as pd 
3.3 Criar um dicionário para "Renomear" as colunas para ficar mais legíveis;
3.4 if __name__ == "__main__": reutilize suas funções e classes em outros arquivos para evitar erros.
3.5 df = pd.read_csv(CAMINHO_CSV, sep=";") : Chama a função para carregamento de dados, lê o arquivo e separa com ponto e virgula.
3.6 df.columns: Acessa a lista com os nomes de todas as colunas do DataFrame.
3.7 str.strip(): Remove espaços em branco invisíveis no início ou no fim dos nomes das colunas
3.8 str.upper(): Transforma todas as letras dos nomes das colunas em MAIÚSCULAS.
3.9 df = df.rename(columns=RENOMEAR): Alter o nome das colunas como citado no dicionário.
3.10 df.head(): Exibe as 5 primeiras linhas do seu DataFrame no terminal. 