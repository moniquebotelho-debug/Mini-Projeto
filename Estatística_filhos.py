import pandas as pd
from rich.panel import Panel
from Carregar_dados import Carregar_dados
from Limpeza_dados import LimpezaDados
from Formatacao_dados import console, numero_br

def mostrar_estatisticas_filhos(df):
    total_filhos = df["CL_FHL"].sum()
    media_filhos = df["CL_FHL"].mean()
    mediana_filhos = df["CL_FHL"].median()
    minimo_filhos = df["CL_FHL"].min()
    maximo_filhos = df["CL_FHL"].max()

    texto =(
        f"[bold] Número total de filhos: [/] { numero_br(total_filhos)}\n"
        f"[bold] Média de filhos: [/] { numero_br(media_filhos)}\n"
        f"[bold] Mediana de filhos: [/] { numero_br(mediana_filhos)}\n"
        f"[bold] Mínimo de filhos: [/] { numero_br(minimo_filhos)}\n"
        f"[bold] Máximo de filhos: [/] { numero_br(maximo_filhos)}\n"
    )

    console.print(Panel(texto, title="Estatísticas de Filhos", expand=False))

if __name__ == "__main__":
    # Carrega e limpa os dados de forma isolada neste arquivo
    df_bruto = Carregar_dados()
    limpador = LimpezaDados(df_bruto)
    limpador.executar()
    df_original = limpador.df
    
    # Executa apenas o painel de filhos
    mostrar_estatisticas_filhos(df_original)