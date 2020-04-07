import pandas as pd
import numpy as np
from datetime import datetime as dt


SYSTEMS=['AEDAS', 'AKEPSAS', 'BEDAS', 'BEPSAS', 'CEDAS', 'CEPESAS']

def read():
    print('Reading data ...')
    columns = ['plan', 'start', 'end', 'duration', 'system', 'day', 'date']
    df = pd.DataFrame(columns=columns)

    for system in SYSTEMS:
        sheets_dict = pd.read_excel(f"./data/{system}.xlsx", sheet_name=None)
        for name, sheet in sheets_dict.items():
            sheet.columns = map(str.lower, sheet.columns)
            sheet['system'] = system
            sheet['date'] = dt.strptime(name, '%d%m%Y')
            sheet['day'] = pd.DatetimeIndex(sheet.date).strftime("%Y-%m-%d")
            df = df.append(sheet)


    df['duration'] = df['duration'].astype('int')
    df['average'] = df.groupby(['plan', 'system'])['duration'].transform('mean').apply(np.ceil)

    return df


