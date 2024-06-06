import plotly.express as px
df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, 'year', 'lifeExp', line_group=None, symbol=None, symbol_sequence=None, symbol_map=None, markers=False)