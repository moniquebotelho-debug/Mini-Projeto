OBJETIVO DO MINI-PROJETO:
Automatizar o carregamento, a limpeza e a formatação de uma base de dados de varejo para garantir relatórios 100% confiáveis e prontos para tomada de decisão.

O QUE O PROBLEMA RESOLVE?
• Decisões erradas: Elimina dados nulos ou vazios que distorcem os resultados.
• Faturamento inflado: Remove registros duplicados que repetem vendas por erro do sistema.
• Erros de leitura: Converte números do padrão americano para o padrão brasileiro (R$ 1.250,50).
• Auditoria lenta: Transforma relatórios técnicos em um painel visual limpo e rápido de entender no terminal.

QUAIS AS TECNOLOGIAS USADAS?
Python (linguagem base) com as bibliotecas Pandas (para manipulação e limpeza dos dados) e Rich (para criação das caixas e tabelas visuais no terminal). O desenvolvimento é feito no VS Code com ambiente virtual (venv) e o código é controlado e salvo via Git e GitHub.

MÉTODOS APLICADOS:

ETAPA 1: PREPARANDO O COMPUTADOR

1.1 Após a instalação já realizada anteriormente do VS Code e do Python verifique se deu certo através do terminal escrevendo: python --version

1.2 Criar e abrir a pasta do projeto: • Criar uma pasta chamada Mini_projeto no computador; • No VS Code, vá em Arquivo → Abrir Pasta... e escolha a pasta Mini_projeto; • Abra o terminal do VS Code em Terminal → Novo Terminal (ou Ctrl+').

1.3 Criar o ambiente virtual (venv): • No terminal do VS Code, dentro da pasta do projeto, crie o ambiente escrevendo: python -m venv .venv ; • Depois, ativo o ambiente escrevendo no terminal: ..venv\Scripts\Activate.ps1 ; • O começo da linha do terminal deverá passar a mostrar (.venv).

1.4 Instalar as bibliotecas no terminal: pip install pandas; pip install rich .

ETAPA 2 - IMPORTAÇÃO DE DADOS

2.1 Realizar a importação dos dados na plataforma Kaggle (base_varejo.csv) para o IDE do VS Code, dentro da pasta Mini Projeto.

ETAPA 3 - CARREGAR OS DADOS

3.1 Criar uma classe Carregado_dados.py; 
3.2 Carregar a biblioteca pandas: importar pandas como pd 
3.3 PASTA = os.path.join(PASTA, 'Base_varejo_original.csv'): Junta o caminho da PASTA com o nome do arquivo (Base_varejo_original.csv). 
3.4 CAMINHO_CSV: Faz exatamente o mesmo para o segundo arquivo (Base_varejo.csv). 
3.5 def Carregar_dados():Cria uma função chamada Carregar_dados para organizar a lógica de leitura do arquivo. • df = pd.read_csv(CAMINHO_CSV, sep=';'): Usa a função read_csv do Pandas para abrir o arquivo cujo caminho está armazenado na variável CAMINHO_CSV, definindo o ponto e vírgula (;) como o caractere que separa as colunas. O resultado é salvo na variável df. 
3.6 if name == " main ": reutilizar suas funções e classes em outros arquivos para evitar erros. 
3.7 print(f'{len(df)} registros carregados'): Exibe na tela a quantidade total de linhas (registros) que existem na tabela. 
3.8 print(df.head()) : Mostra as 5 primeiras linhas da tabela no console para você conferir se os dados foram lidos do jeito certo.

ETAPA 4 - FORMATAÇÃO DOS DADOS

4.1 Criar uma classe Formatacao_dados.py; 
4.2 from rich.console import Console : Importa a classe Console da biblioteca Rich, que serve para exibir textos coloridos, tabelas e formatações no terminal/console do Python. 
4.3 importar pandas como pd : Importa a biblioteca Pandas. 
4.4 console = Console() : Cria uma instância (um objeto) do Console do Rich. 
4.5 def numero_br(valor, casas=0): Define uma função chamada numero_br que formata os números no padrão brasileiro. 
4.6 texto = f"{valor:,.{casas}f}" :Usa uma f-string do Python para formatar o número no padrão internacional (americano): 
• O : inicia a formatação. 
• A , (vírgula) faz o Python colocar vírgulas como separador de milhar. 
• O .{casas}f define quantas casas decimais (f de float) o número vai ter, pegando o valor da variável casas. 
4.7 texto = texto.replace(',', 'X') : Substitui temporariamente a vírgula (que era o separador de milhar no padrão gringo) pela letra X para não bagunçar as próximas trocas. 
4.8 texto = texto.replace('.', ',') : Substitui o ponto decimal (padrão americano) por uma vírgula (padrão brasileiro). 
4.9 texto = texto.replace('X', '.') : Pega o X que citado antes e transforma em ponto, que agora passa a ser o separador de milhar no Brasil. 4.10 return texto: Devolve uma string formatada.

ETAPA 5 - LIMPEZA DE DADOS

5.1 Criar a classe Limpeza_dados.py; 
5.2 importar pandas como pd: Importe a biblioteca Pandas. 
5.3 init (self, df): O construtor da classe. Ele recebe um DataFrame (df), cria uma cópia de segurança dele (self.df = df.copy()) para não modificar o arquivo original por acidente, e guarda a quantidade inicial de linhas (self.registros_iniciais). 
5.4 remove_colunas_vazias(self): Remove do DataFrame todas as colunas que estão completamente vazias (how="all"). O return self permite o encadeamento de métodos. 
5.5 remove_nulos(self): Remove qualquer linha que contenha pelo menos um valor nulo (vazio). 
5.6 remove_duplicados(self): Remove linhas idênticas e redefine o índice do DataFrame (reset_index(drop=True)) para que a numeração das linhas fique sequencial de 0 a N novamente. 
5.7 executar(self): Junta os três métodos de limpeza anteriores em uma única linha. Como cada método retorna o próprio objeto (self), eles podem ser chamados em sequência. 
5.8 salva_novo_csv(self, caminho): Salva o DataFrame limpo em um arquivo CSV no caminho especificado, utilizando o ponto e vírgula (;) como separador e sem salvar a coluna de índices (index=False). 
5.9 mostrar_relatorio(self): Exibe no terminal um resumo com o total de linhas antes da limpeza, quantas foram apagadas e quantas restauradas.

ETAPA 6 - RESUMO DE DADOS

6.1 Criar uma classe Resumo_dados.py; 
6.2 importar pandas como pd: Importe a biblioteca Pandas. 
6.3 Painel de importação rich.panel: Usado para criar caixas visuais e estilizadas no terminal. 
6.4 Carregar_dados: Função própria (de um arquivo local) que busca/carrega a base de dados bruta. 
6.5 LimpezaDados: Classe própria para tratar e limpar os dados brutos. 
6.6 console, numero_br: Ferramentas locais para exibir o texto no console e formatar os números no padrão brasileiro (com pontos e vírgulas). 
6.7 mostrar_resultado(df): Essa função obtém uma tabela (df), calcula estatísticas e monta um painel visual: 
• len(df): Conta o total de linhas (registros) na tabela. 
• nunique(): Conta quantos valores diferentes (únicos) existem em cada coluna. • texto: Organiza todas essas informações em uma lista com texto em negrito ([bold]), formatando os números com a função numero_br. 
• console.print(Panel(...)): Imprima tudo dentro de uma caixinha bonita no terminal com o título "Painel do Varejo". 
6.8 O Fluxo Principal (if name == ' main ':) : É o ponto onde o script realmente começa a rodar quando você o executa: 
• Carrega os dados brutos: df_bruto = Carregar_dados() 
• Executa a limpeza: Cria o objeto de limpeza e limpa roda.executar() 
• Pega a tabela limpa: df_original = limpar.df 
• Mostra o painel: Roda mostrar_resultado(df_original) para exibir o resumo na tela.

ETAPA 7 - ESTATÍSTICA FILHOS

7.1 Criar uma classe Estatística_filhod.py;
7.2 Os Cálculos (Pandas):
• sum(): Soma o total de filhos de todas as linhas.
• mean(): Calcula a média aritmética de filhos por pessoa.
• median(): Encontra a mediana (o valor central que divide os dados ao meio).
• min(): Identifica o menor número de filhos registrado (geralmente 0).
• max(): Identifica o maior número de filhos registrado em uma única linha.

ETAPA 8 - INSERÇÃO DOS ARQUIVOS DO MINI PROJETO NO GITHUB

8.1 Clique no ícone de Controle de Código Fonte e em Iniciar o Repositório; 
8.2 Fazer Commit e Sincronizar, adicionar uma mensagem de commit, clicar no botão de confirmação e utilizar a opção de sincronizar para enviar os dados para a plataforma Github.
