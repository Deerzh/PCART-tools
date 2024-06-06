import plotly.express as px
df = px.data.wind()
fig = px.line_polar(df, 'frequency', theta='direction', color='strength', symbol=None, symbol_sequence=None, symbol_map=None, markers=False)