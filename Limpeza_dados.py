"""Limpeza dos dados importados da base de varejo."""

import pandas as pd

class LimpezaDados:

    def __init__(self, df):
        self.df = df.copy()
        self.registros_iniciais = len(df)

    def remover_colunas_vazias(self):
        self.df = self.df.dropna(axis=1, how="all")        
        return self

    def remover_nulos(self): 
            self.df = self.df.dropna()       
            return self

    def remover_duplicados(self):        
            self.df = self.df.drop_duplicates().reset_index(drop=True)
            return self

    def executar(self): 
            self.remover_colunas_vazias().remover_nulos().remover_duplicados()      
            return self

    def salva_novo_csv(self, caminho):  
            self.df.to_csv(caminho, sep=";", index=False)      

    def mostrar_relatorio(self):
        print(f"Registros iniciais: {self.registros_iniciais}")
        print(f"Registros removidos: {self.registros_iniciais - len(self.df)}")
        print(f"Registros finais: {len(self.df)}")

if __name__ == "__main__":
      from Carregar_dados import CAMINHO_CSV, CAMINHO_CSV_ORIGINAL

      limpeza = LimpezaDados(pd.read_csv(CAMINHO_CSV, sep=";"))
      limpeza.executar()
      limpeza.mostrar_relatorio()
      limpeza.salva_novo_csv(CAMINHO_CSV_ORIGINAL)
      print(f"Base limpa salva em: {CAMINHO_CSV_ORIGINAL}")



