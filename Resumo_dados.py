import pandas as pd
from rich.panel import Panel
from Carregar_dados import Carregar_dados
from Limpeza_dados import LimpezaDados
from Formatacao_dados import console, numero_br

"""FUNÇÕES: def = cria uma função; df = dataframe (é uma estrutura em formato de tabela, lembra um excel); len = lê quantas linhas tem no datafreme; sum = soma itens; nunique: conta o nº de valores únicos; bold: imprime o texto em negrito"""

def mostrar_resultado(df):
    total_registros = len(df)
    total_codigo_de_cliente = df["CL_ID"].nunique()
    total_genero = df["CL_GENERO"].nunique()
    total_estado_civil = df["CL_EC"].nunique()
    total_categorias_produtos = df["PR_CAT"].nunique()
    total_nomes_produtos = df["PR_NOME"].nunique()

    texto =(
        f"[bold] Registros: [/] { numero_br(total_registros)}\n"
        f"[bold] Códigos de Cliente: [/] { numero_br(total_codigo_de_cliente)}\n"
        f"[bold] Gêneros: [/] { numero_br(total_genero)}\n"
        f"[bold] Estados Civis: [/] { numero_br(total_estado_civil)}\n"
        f"[bold] Categorias de Produtos: [/] { numero_br(total_categorias_produtos)}\n"
        f"[bold] Nomes de Produtos: [/] { numero_br(total_nomes_produtos)}\n"
    )

    console.print(Panel(texto, title="Painel do Varejo", expand=False))

if __name__ == "__main__":
  df_bruto = Carregar_dados()
  limpador = LimpezaDados(df_bruto)
  limpador.executar()
  df_original = limpador.df
  mostrar_resultado(df_original)  