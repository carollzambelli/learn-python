import pandas as pd
import re

def read_metadado(meta_path):
    meta = pd.read_excel(meta_path)
    cols_originais = list(meta["cols_originais"])
    cols_renamed = list(meta["cols_renamed"])
    tipos_originais = dict(zip(cols_originais,list(meta["tipo_original"])))
    tipos_formatted = dict(zip(cols_renamed,list(meta["tipo_formatted"])))
    cols_chaves = list(meta.loc[meta["key"] == 1]["cols_originais"])
    null_tolerance = dict(zip(cols_originais,list(meta["raw_null_tolerance"])))
    std_str = list(meta.loc[meta["std_str"] == 1]["cols_renamed"])
    return cols_originais, cols_renamed, tipos_originais, tipos_formatted, cols_chaves, null_tolerance, std_str

def padroniza_str(obs):
    return re.sub('[^A-Za-z0-9]+', '', obs.lower())

def corrige_hora(hr_str):
     if len(hr_str) == 1:
          return '00:'+ '0' + hr_str
     elif len(hr_str) == 2:
         if int(hr_str) <= 12:
            return '0' + hr_str[0] + ':' + hr_str[1]+'0'
         else:
            return  "00:"+hr_str
     elif len(hr_str) == 3:
         return "0" + hr_str[0] + ':' + hr_str[1:]
     elif len(hr_str) == 4:
         if hr_str == "2400":
             return "00:00"
         else:
             return hr_str[0:2] + ':' + hr_str[2:]
     else:
        return "ERROR"


#meta_path  = "C://Users//Carolina//OneDrive//Github//learn-python//PROJETOS//db-pipeline//assets//work_metadado_flights.xlsx"
#cols_originais, cols_renamed, cols_tipos, cols_chaves, null_tolerance, std_str = read_metadado(meta_path)
#print(cols_originais, cols_renamed, cols_tipos, cols_chaves, null_tolerance)