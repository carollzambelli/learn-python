
api_metadados = {
    "path" : 'https://api.aviationstack.com/v1/flights',
    "cols_originais" : ['flight_date', 'departure.iata', 'arrival.iata','airline.iata', 'departure.estimated', 'arrival.estimated'],
    "cols_renamed" : ['data_voo', 'origem', 'destino', 'companhia', 'datetime_partida_formatted', "datetime_chegada_formatted"],
    "tipos_map" : {
        'data_voo': "datetime",
        'origem' : "string",
        'destino': "string",
        'companhia': "string",
        'datetime_partida_formatted': "datetime",
        'datetime_chegada_formatted': "datetime"
    },
    "std_str" : ['origem', 'destino', 'companhia']
}

cols_pre_proc = [
    "data_voo",
    "tempo_voo_esperado",
    "datetime_partida_formatted",
    "origem_formatted","companhia_formatted", 
    "dia_semana",
    "distancia",
    "horario"]

cols_modelo =  [
    'distancia',
    'companhia_formatted_9E',
    'companhia_formatted_AA',
    'companhia_formatted_AS',
    'companhia_formatted_B6',
    'companhia_formatted_DL',
    'companhia_formatted_EV',
    'companhia_formatted_F9',
    'companhia_formatted_FL',
    'companhia_formatted_HA',
    'companhia_formatted_MQ',
    'companhia_formatted_OO',
    'companhia_formatted_UA',
    'companhia_formatted_US',
    'companhia_formatted_VX',
    'companhia_formatted_WN',
    'companhia_formatted_YV',
    'origem_formatted_EWR',
    'origem_formatted_JFK',
    'origem_formatted_LGA',
    'dia_semana_0',
    'dia_semana_1',
    'dia_semana_2',
    'dia_semana_3',
    'dia_semana_4',
    'dia_semana_5',
    'dia_semana_6',
    'horario_MADRUGADA',
    'horario_MANHA',
    'horario_NOITE',
    'horario_TARDE'
]

routes = {
    "EWR" : ['IAH', 'ORD', 'FLL', 'SFO', 'LAS', 'PBI', 'MIA', 'ATL', 'PHX',
       'MSP', 'LAX', 'CLT', 'IAD', 'SNA', 'TPA', 'RSW', 'SEA', 'DFW',
       'DEN', 'MCO', 'BOS', 'JAX', 'CHS', 'MEM', 'MYR', 'JAC', 'RDU',
       'DTW', 'SAN', 'MDW', 'CLE', 'EGE', 'DCA', 'AVL', 'STL', 'BUF',
       'IND', 'MKE', 'PWM', 'SAV', 'SYR', 'CMH', 'ROC', 'BWI', 'BTV',
       'DAY', 'HOU', 'ALB', 'BDL', 'SLC', 'PIT', 'HNL', 'MHT', 'MSN',
       'GSO', 'CVG', 'AUS', 'RIC', 'GSP', 'GRR', 'MCI', 'BNA', 'SAT',
       'SDF', 'PDX', 'OMA', 'TYS', 'PVD', 'DSM', 'ORF', 'TUL', 'OKC',
       'MSY', 'XNA', 'CAE', 'PHL', 'HDN', 'BZN', 'MTJ', 'SJU', 'BQN',
       'STT', 'SBN', 'TVC', 'ANC'],
    "JFK" : ['MCO', 'PBI', 'TPA', 'LAX', 'BOS', 'ATL', 'SFO', 'RSW', 'PHX',
       'BUF', 'LAS', 'MSY', 'SLC', 'FLL', 'ROC', 'SYR', 'SRQ', 'SEA',
       'MIA', 'RDU', 'CLT', 'MSP', 'PIT', 'SAN', 'DCA', 'JAX', 'ORD',
       'DTW', 'BWI', 'HNL', 'AUS', 'BTV', 'IAD', 'PWM', 'HOU', 'LGB',
       'BUR', 'CLE', 'IND', 'CMH', 'BNA', 'DFW', 'CVG', 'PHL', 'DEN',
       'EGE', 'ORF', 'PDX', 'SJC', 'CHS', 'OAK', 'SMF', 'SAT', 'MEM',
       'RIC', 'PSP', 'PSE', 'BQN', 'SJU', 'ACK', 'IAH', 'MCI', 'ABQ',
       'MVY', 'STT', 'STL', 'JAC', 'SDF', 'MKE', 'BHM'],
    "LGA" : ['IAH', 'ATL', 'IAD', 'ORD', 'DFW', 'FLL', 'MSP', 'DTW', 'MIA',
       'BWI', 'MCO', 'DEN', 'PBI', 'XNA', 'MKE', 'RSW', 'TPA', 'CLT',
       'CMH', 'CLE', 'STL', 'RDU', 'BNA', 'PHL', 'MDW', 'SRQ', 'DCA',
       'CAK', 'MSY', 'BOS', 'MEM', 'BUF', 'PIT', 'MCI', 'CRW', 'CVG',
       'RIC', 'ROC', 'TYS', 'BHM', 'PWM', 'GRR', 'EYW', 'GSO', 'HOU',
       'JAX', 'BTV', 'CHS', 'SAV', 'IND', 'DAY', 'BGR', 'MSN', 'ORF',
       'OMA', 'DSM', 'GSP', 'ILM', 'SYR', 'SDF', 'SBN', 'LEX', 'MHT',
       'CAE', 'CHO', 'AVL', 'TVC', 'MYR']
}

