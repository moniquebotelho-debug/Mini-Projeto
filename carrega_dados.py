import pandas as pd

CAMINHO_CSV = "base_vendas.csv"

RENOMEAR = {
    "DATA": "data_compra",
    "CO_ID": "codigo_de_compra",
    "CL_ID": "codigo_de_cliente",
    "CL_GENERO": "genero",
    "CL_EC": "estado_civil",
    "CL_FHL": "dependentes",
    "PR_CAT": "categoria",
}

def carregar_dados():
    df = pd.read_csv(CAMINHO_CSV, sep=";")
    return df

if __name__ == "__main__":
    df = carregar_dados()
    df.columns = df.columns.str.strip().str.upper()
    df = df.rename(columns=RENOMEAR)
    print(df.head())