import pandas as pd

def adjust_decimal_format(column: pd.Series):
    try:
        new_column = column.apply(lambda x: float(str(x).replace(',', '.').replace('nan', '0')))
        return new_column
    
    except:
        return new_column