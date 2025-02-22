import polars as pl
from random import uniform
from datetime import date
df = pl.DataFrame({'dtm': [date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 3)], 'num': [uniform(-500, 500), uniform(-500, 500), uniform(-500, 500)], 'val': [10000, 20000, 30000]})
df.write_excel(column_widths=None, column_totals=None, table_name=None, table_style=None, position='A1', column_formats=None, conditional_formats=None, dtype_formats=None, row_heights=None)
