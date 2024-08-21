import sqlite3
import os
import pandas as pd
from dotenv import load_dotenv
from assets.utils import read_metadado, padroniza_str
import logging
import datetime

logging.basicConfig(filename='flights_pipe_log.txt', level=logging.INFO)
logger = logging.getLogger()
load_dotenv()

def read_data(data_path):
    '''
    Função de leitura dos dados
    INPUT: Path do arquivo da base de dados
    OUTPUT: Pandas DataFrame
    '''
    df = pd.read_csv(data_path,index_col=0)
    return df

def null_check(df, null_tolerance):
    '''
    Função de validação de nulos
    INPUT: Pandas DataFrame, dicionário de colunas como chave e critério de nulo como valores
    OUTPUT: Pandas DataFrame
    '''
    for col in null_tolerance.keys():
        if  len(df.loc[df[col].isnull()])/len(df)> null_tolerance[col]:
            logger.error(
                f" {col} possui mais nulos do que o esperado; {datetime.datetime.now()} ")

def null_exclude(df, cols_chaves):
    '''
    Função de exclusao das observações nulas
    INPUT: Pandas DataFrame, lista de colunas que são chaves
    OUTPUT: Pandas DataFrame com as observações nulas excluidas
    '''
    tmp = df.copy()
    for col in cols_chaves:
        tmp_df = tmp.loc[~df[col].isna()]
        tmp = tmp_df.copy()
    return tmp_df

def select_rename(df, cols_originais, cols_renamed):
    '''
    Função de validação de nulos
    INPUT: Pandas DataFrame, lista dos nomes das colunas e lista dos novos nomes 
    OUTPUT: Pandas DataFrame com novos nomes
    '''
    df_work = df.loc[:, cols_originais].copy()
    columns_map = dict(zip(cols_originais,cols_renamed))
    df_work.rename(columns=columns_map, inplace = True)
    return df_work

def convert_data_type(df, tipos_map):
    '''
    Função de validação de nulos
    INPUT: Pandas DataFrame, dicionário de colunas como chave e seus tipos como valores
    OUTPUT: Pandas DataFrame com novos nomes
    '''
    data =df.copy()
    for col in tipos_map.keys():
        tipo = tipos_map[col]
        if tipo == "int":
            tipo = data[col].astype(int)
        elif tipo == "float":
            data[col] = data[col].astype(float)
        elif tipo == "datetime":
            data[col] = pd.to_datetime(data[col])
    return data


def string_std(df, std_str):
    '''
    Função de validação de nulos
    INPUT: Pandas DataFrame, lista das colunas que devem receber a padronização de strings
    OUTPUT: Pandas DataFrame com as colunas padronizadas
    '''
    df_work = df.copy()
    for col in std_str:
        new_col = f'{col}_formatted'
        df_work[new_col] = df_work.loc[:,col].apply(lambda x: padroniza_str(x))
    return df_work

# Criar função para tratamento de horas
# Criar função de validação de chaves
# Criar função para novos campos
# Função para para salvar no banco de dados
# exemplo: df.to_sql('mytable', con=conn, if_exists='replace')


if __name__ == "__main__":
    logger.info(f'Inicio da execução ; {datetime.datetime.now()}')
    metadados  = read_metadado(os.getenv('META_PATH'))
    df = read_data(os.getenv('DATA_PATH'))
    # função1
    # logger(tratamento 1 realizado)
    logger.info(f'Fim da execução ; {datetime.datetime.now()}')