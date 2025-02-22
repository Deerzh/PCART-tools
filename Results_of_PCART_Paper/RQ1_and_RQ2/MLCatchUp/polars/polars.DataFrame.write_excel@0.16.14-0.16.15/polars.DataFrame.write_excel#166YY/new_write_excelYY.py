import polars as pl
from random import uniform
from datetime import date
df = pl.DataFrame({'dtm': [date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 3)], 'num': [uniform(-500, 500), uniform(-500, 500), uniform(-500, 500)], 'val': [10000, 20000, 30000]})
df.write_excel(None, column_widths=None, dtype_formats=None, has_header=True, autofilter=True, table_style=None, column_totals=None, sparklines=None, row_heights=None, column_formats=None, worksheet=None, position='A1', table_name=None, float_precision=3, conditional_formats=None)
