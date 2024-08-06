'''
O Código Morse é um sistema de representação de letras, algarismos e sinais de pontuação através
de um sinal codificado enviado de modo intermitente. Foi desenvolvido por Samuel Morse em 1837, 
criador do telégrafo elétrico, dispositivo que utiliza correntes elétricas para controlar eletroímãs 
que atuam na emissão e na recepção de sinais. 
O script tem a finalidade de decifrar uma mensagem em código morse e salvá-la em texto claro.
'''

import os
import datetime
import sys
import pandas as pd
from config import dict_morse, file_path

# from dotenv import load_dotenv # para variáveis de ambiente
# load_dotenv() # para carregar as variáveis de ambiente
# file_path = os.getenv("file_path")

def decode_morse(msg):
    '''
    input : mensagem em código morse com as letras separadas por espaços
    output : palavra escrito em letras e algarismos
    '''
    msg_lst = msg.split(" ")
    msg_claro = [] 
    for letter in msg_lst :
        msg_claro.append(dict_morse[letter])
    return "".join(msg_claro)


def save_clear_msg_csv_hdr(msg):
    '''
    input : mensagem em código morse com as letras separadas por espaços
    output : palavra escrito em letras e algarismos, salva em arquivo csv
    '''
    now = datetime.datetime.now()
    msg_claro = decode_morse(msg)
    df = pd.DataFrame([[msg_claro, now]], columns=["mensagem", "datetime"])
    hdr = not os.path.exists(file_path)
    df.to_csv(file_path, mode='a', index=False, header=hdr)


if __name__ == "__main__":
    save_clear_msg_csv_hdr(sys.argv[1])
    #print(save_clear_msg_csv_hdr.__doc__)
    #print(pd.to_pickle.__doc__)
