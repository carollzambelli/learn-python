import sqlite3
import os
import pandas as pd
from dotenv import load_dotenv
import assets.utils as utils
from assets.utils import logger
from assets.config import api_metadados, routes, cols_modelo, cols_pre_proc
import datetime

load_dotenv()

def data_clean(df, metadados):
    '''
    Função principal para saneamento dos dados
    INPUT: Pandas DataFrame, dicionário de metadados
    OUTPUT: Pandas DataFrame, base tratada
    '''
    df["data_voo"] = pd.to_datetime(df[['year', 'month', 'day']]) 
    df = utils.null_exclude(df, metadados["cols_chaves"])
    df = utils.convert_data_type(df, metadados["tipos_originais"])
    df = utils.select_rename(df, metadados["cols_originais"], metadados["cols_renamed"])
    df = utils.string_std(df, metadados["std_str"])

    df.loc[:,"datetime_partida"] = df.loc[:,"datetime_partida"].str.replace('.0', '')
    df.loc[:,"datetime_chegada"] = df.loc[:,"datetime_chegada"].str.replace('.0', '')

    for col in metadados["corrige_hr"]:
        lst_col = df.loc[:,col].apply(lambda x: utils.corrige_hora(x))
        df[f'{col}_formatted'] = pd.to_datetime(df.loc[:,'data_voo'].astype(str) + " " + lst_col)
    
    logger.info(f'Saneamento concluído; {datetime.datetime.now()}')
    return df

def feat_eng(df):
    '''
    Cria novas colunas
    '''

    df = df.dropna(subset=['tempo_voo'])
    df['tempo_voo_esperado'] = df['tempo_voo'].astype(int).apply(lambda x: f"{x // 100:02d}:{x % 100:02d}")
    df['tempo_voo_hr'] = df['tempo_voo_esperado'].apply(lambda x: int(x.split(':')[0]) + int(x.split(':')[1]) / 60)
    df['atraso'] = (pd.to_datetime(df['datetime_chegada_formatted'], format='%d/%m/%Y %H:%M:%S') - pd.to_datetime(df['datetime_partida_formatted'], format='%d/%m/%Y %H:%M:%S')).dt.total_seconds() / 60 - df['tempo_voo']
    df['atraso'] = df['atraso'].apply(lambda x: max(x, 0))
    df['dia_semana'] = pd.to_datetime(df['data_voo'], format='%Y-%m-%d').dt.day_name()
    df['horario'] = pd.Timestamp.now()
    df['flg_status'] = pd.to_datetime(df['datetime_chegada_formatted'], format='%Y-%m-%d %H:%M:%S').apply(lambda x: 'Em trânsito' if x > pd.Timestamp.now() else 'Chegou ao destino')

    logger.info(f'Iplementação feat_eng; {datetime.datetime.now()}')
    return df
   

def save_data_sqlite(df):
    try:
        conn = sqlite3.connect("data/NyflightsDB.db")
        logger.info(f'Conexão com banco estabelecida ; {datetime.datetime.now()}')
    except:
        logger.error(f'Problema na conexão com banco; {datetime.datetime.now()}')
    c = conn.cursor()
    df.to_sql('nyflights', con=conn, if_exists='replace')
    conn.commit()
    logger.info(f'Dados salvos com sucesso; {datetime.datetime.now()}')
    conn.close()

def fetch_sqlite_data(table):
    try:
        conn = sqlite3.connect("data/NyflightsDB.db")
        logger.info(f'Conexão com banco estabelecida ; {datetime.datetime.now()}')
    except:
        logger.error(f'Problema na conexão com banco; {datetime.datetime.now()}')
    c = conn.cursor()
    c.execute(f"SELECT * FROM {table} LIMIT 5")
    print(c.fetchall())
    conn.commit()
    conn.close()


if __name__ == "__main__":
    logger.info(f'Inicio da execução ; {datetime.datetime.now()}')
    metadados  = utils.read_metadado(os.getenv('META_PATH'))
    df = pd.read_csv(os.getenv('DATA_PATH'),index_col=0)
    df = data_clean(df, metadados)
    print(df.head())
    utils.null_check(df, metadados["null_tolerance"])
    utils.keys_check(df, metadados["cols_chaves"])
    df = df.head(10)
    df = feat_eng(df)
    df.to_excel('seu_arquivo.xlsx', index=False)
    save_data_sqlite(df)
    fetch_sqlite_data('nyflights')
    logger.info(f'Fim da execução ; {datetime.datetime.now()}')