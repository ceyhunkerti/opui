import pandas as pd
from datetime import datetime as dt


SYSTEMS=['AEDAS', 'AKEPSAS', 'BEDAS', 'BEPSAS', 'CEDAS', 'CEPESAS']

def read():
    columns = ['plan', 'start', 'end', 'duration', 'system', 'day', 'date']
    df = pd.DataFrame(columns=columns)

    for system in SYSTEMS:
        sheets_dict = pd.read_excel(f"./data/{system}.xlsx", sheet_name=None)
        for name, sheet in sheets_dict.items():
            sheet.columns = map(str.lower, sheet.columns)
            sheet['system'] = system
            sheet['day'] = name
            sheet['date'] = dt.strptime(name, '%d%m%Y')
            df = df.append(sheet)

    return df

print('Reading data ...')
df = read()