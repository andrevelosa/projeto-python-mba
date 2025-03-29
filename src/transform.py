import pandas as pd
from datetime import datetime

'''
def calc_horas(coluna_tempo_voo):
    return coluna_transformada_hora


def classifica_turno(coluna_data_hora):
    
    Regra de classificação:
    06:00 - 12:00 : MANHÃ
    12:00 - 18:00 : TARDE
    18:00 - 00:00 : NOITE
    00:00 - 06:00 : MADRUGADA
    return coluna_turno
'''

def calc_horas(coluna_tempo_voo):
    """
    Converte o tempo de voo de minutos para horas.
    
    :param coluna_tempo_voo: Tempo de voo em minutos (float ou int)
    :return: Tempo de voo em horas (float) ou None se for NaN
    """
    if pd.isna(coluna_tempo_voo):  # Verifica se é NaN
        return None  # Retorna None (ou poderia retornar 0, dependendo do seu caso)

    return coluna_tempo_voo / 60  # Converte de minutos para horas


def classifica_turno(coluna_data_hora):
    """
    Classifica o turno da partida do voo com base no horário informado.
    
    Regra de classificação:
    06:00 - 12:00 : MANHÃ
    12:00 - 18:00 : TARDE
    18:00 - 00:00 : NOITE
    00:00 - 06:00 : MADRUGADA
    
    :param coluna_data_hora: Horário da partida (string no formato 'HH:MM' ou datetime)
    :return: Turno correspondente (manhã, tarde, noite, madrugada)
    """
    if isinstance(coluna_data_hora, str):
        coluna_data_hora = datetime.strptime(coluna_data_hora, "%H:%M").time()
    elif isinstance(coluna_data_hora, datetime):
        coluna_data_hora = coluna_data_hora.time()
    
    if 6 <= coluna_data_hora.hour < 12:
        return "MANHÃ"
    elif 12 <= coluna_data_hora.hour < 18:
        return "TARDE"
    elif 18 <= coluna_data_hora.hour < 24:
        return "NOITE"
    else:
        return "MADRUGADA"