import pandas as pd
import re

def read_metadado(meta_path):
    meta = pd.read_excel(meta_path)
    metadados = {
        "cols_originais" : list(meta["cols_originais"]), 
        "cols_renamed" : list(meta["cols_renamed"]),
        "tipos_originais" : dict(zip(list(meta["cols_originais"]),list(meta["tipo_original"]))),
        "tipos_formatted" : dict(zip(list(meta["cols_renamed"]),list(meta["tipo_formatted"]))),
        "cols_chaves" : list(meta.loc[meta["key"] == 1]["cols_originais"]),
        "null_tolerance" : dict(zip(list(meta["cols_originais"]), list(meta["raw_null_tolerance"]))),
        "std_str" : list(meta.loc[meta["std_str"] == 1]["cols_renamed"])
        }
    return metadados

def padroniza_str(obs):
    return re.sub('[^A-Za-z0-9]+', '', obs.lower())


def corrige_hora(hr_str, dct_hora = {1:"000?",2:"00?",3:"0?",4:"?"}):
    if hr_str == "2400":
        return "00:00"
    elif (len(hr_str) == 2) & (int(hr_str) <= 12):
        return f"0{hr_str[0]}:{hr_str[1]}0"
    else:
        hora = dct_hora[len(hr_str)].replace("?", hr_str)
        return f"{hora[:2]}:{hora[2:]}"


#meta_path  = "C://Users//Carolina//OneDrive//Github//learn-python//PROJETOS//db-pipeline//assets//work_metadado_flights.xlsx"
#cols_originais, cols_renamed, tipos_originais, tipos_formatted, cols_chaves, null_tolerance, std_str = read_metadado(meta_path)
#print(cols_originais, cols_renamed, tipos_originais, tipos_formatted, cols_chaves, null_tolerance, std_str)