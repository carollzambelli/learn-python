import pandas as pd
import re
import logging
import datetime
import random
import sqlite3
from sklearn.preprocessing import StandardScaler
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=UserWarning)

logging.basicConfig(filename='data/flights_pipe.log', level=logging.INFO)
logger = logging.getLogger()


# Funções de Saneamento ----------------------------------------------------------------

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
        elif tipo == "string":
            data[col] = data[col].astype(str)
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


# Funções auxiliares -------------------------------------------

def padroniza_str(obs):
    return re.sub('[^A-Za-z0-9]+', '', obs.upper())

def classifica_hora(hra):
    if 0 <= hra < 6: return "MADRUGADA"
    elif 6 <= hra < 12: return "MANHA"
    elif 12 <= hra < 18: return "TARDE"
    else: return "NOITE"

def recupera_dist(origem, destinos, table, db):
    if (type(destinos) != str) & (len(destinos) > 1):
        destino = random.choices(population=destinos, k=1)[0]
    else:
        destino = destinos
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute(f"SELECT distancia FROM {table} \
            WHERE origem_formatted LIKE '{origem}' \
            AND destino_formatted = '{destino}' LIMIT 1 ")
    valor = c.fetchall()
    return valor[0][0]

# Funções de pré-processamento do modelo

def pre_process(df):
    categorical_cols = [c for c in ["origem_formatted","companhia_formatted",  "dia_semana", "horario"]]
    df_categorical = df[categorical_cols].copy()
    for col in categorical_cols:
        df_categorical = pd.get_dummies(df_categorical, columns=[col])
    num_cols = [c for c in  ["tempo_voo_esperado", "distancia"]]
    df_std = pd.DataFrame(StandardScaler().fit_transform(df[num_cols]),columns=num_cols)
    df_processed = pd.concat([df_std, df_categorical], axis=1)
    return df_processed
