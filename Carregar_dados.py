import pandas as pd
import os

CAMINHO_CSV = "Base_varejo.csv"

PASTA = os.path.dirname(os.path.abspath(__file__))
CAMINHO_CSV_ORIGINAL = os.path.join(PASTA, "Base_varejo_original.csv")  
CAMINHO_CSV = os.path.join(PASTA, "Base_varejo.csv")     

def Carregar_dados():
    df = pd.read_csv(CAMINHO_CSV, sep=";")
    return df

if __name__ == "__main__":
    df = Carregar_dados()
    print (f"{len(df)} registros carregados")
    print(df.head())