import sqlite3

# Conectando/Criando um SQLite database
conn = sqlite3.connect("../data/NyflightsDB.db")

# Criando um cursos
c = conn.cursor()

# Create a table
query = '''
    CREATE TABLE IF NOT EXISTS nyflights (
        id INTEGER PRIMARY KEY,
        data_voo DATETIME NOT NULL,
        companhia_formatted TEXT NOT NULL,
        id_aeronave_formatted TEXT,
        datetime_partida_formatted DATETIME NOT NULL,
        datetime_chegada_formatted DATETIME NOT NULL,
        origem_formatted TEXT NOT NULL,
        destino_formatted TEXT NOT NULL,
        tempo_voo FLOAT,
        distancia FLOAT,
        tempo_voo_esperado FLOAT,
        tempo_voo_hr FLOAT,
        atraso FLOAT,
        dia_semana TEXT NOT NULL,
        horario TEXT NOT NULL,
        flg_status TEXT NOT NULL
    )
    '''

c.execute(query)
conn.commit()
conn.close()