import requests
import datetime
import pandas as pd
from dotenv import load_dotenv
import os
import pickle
import json
from sklearn.linear_model import LinearRegression
from assets.config import api_metadados, routes, cols_modelo, cols_pre_proc
import assets.utils as utils

load_dotenv()
origem = "EWR"
destino = "IAH"
#destino = routes[origem]

def ingest_api(metadados, key, origem, destino):
   '''
   api_result = requests.get(
      metadados["path"],
      params = {
        'access_key': key,
        "dep_iata" : origem,
        "arr_iata" : destino
        "limit" : 5
      })
   api_response = api_result.json()
   '''
   with open('data/amostra.json', 'r') as file:
      api_response = json.loads(file.read())

   df = pd.json_normalize(api_response["data"])
   return df

def data_clean(df, metadados):
    df = utils.select_rename(df, metadados["cols_originais"], metadados["cols_renamed"])
    df = utils.convert_data_type(df, metadados["tipos_map"])
    df = utils.string_std(df, metadados["std_str"])
    return df

def feat_eng(df, origem, destino, table, db):
   data = df.copy()
   data["tempo_voo_esperado"] = (data["datetime_chegada_formatted"] - \
                                 data["datetime_partida_formatted"]
                                 ) / pd.Timedelta(hours=1)
   data["dia_semana"] = data["data_voo"].dt.day_of_week 
   data["distancia"] = utils.recupera_dist(origem, destino, table, db)
   data["horario"] = data.loc[:,"datetime_partida_formatted"]\
                         .dt.hour.apply(lambda x: utils.classifica_hora(x))
   return data[cols_pre_proc]

def aplica_modelo(df, filename):
   df_processed = utils.pre_process(df)
   cols_missing = set(cols_modelo) - set(df_processed.columns)
   for col in cols_missing: df_processed[col] = False
   df_processed = df_processed[cols_modelo]
   clf_reg = pickle.load(open(filename, 'rb'))
   predict = clf_reg.predict(df_processed)
   return predict


if __name__ == "__main__":
   df = ingest_api(api_metadados, os.getenv('ACCESS_KEY'), origem, destino)
   df = data_clean(df, api_metadados)
   df = feat_eng(df, origem, destino, "nyflights", "data/NyflightsDB.db")
   pred = aplica_modelo(df, "assets/reg_model.sav")
   print(pred)
