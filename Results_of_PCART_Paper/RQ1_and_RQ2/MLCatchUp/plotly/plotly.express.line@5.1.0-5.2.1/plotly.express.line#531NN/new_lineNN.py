import plotly.express as px
df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, 'year', 'lifeExp', None, None, None, None, None, None, None, None, None, 0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, log_x=False, log_y=False, range_x=None, range_y=None, symbol=None, symbol_sequence=None, symbol_map=None, markers=False)