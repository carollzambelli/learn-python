import sqlite3
import os
import pandas as pd
from dotenv import load_dotenv
from assets.utils import read_metadado, padroniza_str
import logging
import datetime


logging.basicConfig(filename='flights_pipe.txt', level=logging.INFO)
logger = logging.getLogger()
load_dotenv()

# Função de leitura dos dados
def read_data(data_path):
    df = pd.read_csv(data_path,index_col=0)
    df["data_voo"] = pd.to_datetime(df[['year', 'month', 'day']]) 
    return df

# Função de validação de nulos
def null_check(df, null_tolerance):
    for col in null_tolerance.keys():
        if  len(df.loc[df[col].isnull()])/len(df)> null_tolerance[col]:
            logger.warning(f'Muitos NULOS: {col} ;{datetime.datetime.now()}')

# Função para excluir de nulos
def null_exclude(df, cols_chaves):
    tmp = df.copy()
    for col in cols_chaves:
        tmp_df = tmp.loc[~df[col].isna()]
        tmp = tmp_df.copy()

# Função de seleção e rename
def select_rename(df,cols_originais, cols_renamed):
    df_work = df.loc[:, cols_originais].copy()
    columns_map = dict(zip(cols_originais,cols_renamed))
    df_work.rename(columns=columns_map, inplace = True)
    return df_work

# Função de tipagem
def convert_data_type(df, tipos_map):
    data =df.copy()
    for col in tipos_map.keys():
        tipo = tipos_map[col]
        if tipo == "int":
            tipo = data[col].astype(int)
        elif tipo == "float":
            data[col] = data[col].astype(float)
        elif tipo == "datetime":
            data[col] = pd.to_datetime(data[col])

# Função para tratar strings
def string_std(df, std_str):
    df_work = df.copy()
    for col in std_str:
        new_col = f'{col}_formatted'
        df_work[new_col] = df_work.loc[:,col].apply(lambda x: padroniza_str(x))
    return df_work

# Função para tratamento de horas
# Função de validação de chaves
# Novos campos
# Salvar no banco de dados


if __name__ == "__main__":
    logger.info(f'Inicio da execução ; {datetime.datetime.now()}')
    cols_originais, cols_renamed, tipos_originais, tipos_formatted, cols_chaves, null_tolerance, std_str  = read_metadado(os.getenv('META_PATH'))
    df= read_data(os.getenv('DATA_PATH'))
    print(cols_originais, cols_renamed, tipos_originais, tipos_formatted, cols_chaves, null_tolerance, std_str)
    print(df.head())