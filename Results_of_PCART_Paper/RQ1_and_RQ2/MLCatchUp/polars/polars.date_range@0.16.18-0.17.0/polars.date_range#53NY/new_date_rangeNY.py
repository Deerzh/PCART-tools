import polars as pl
from datetime import date
pl.date_range(date(2022, 1, 1), closed='both', interval='1mo', end=date(2022, 3, 1))