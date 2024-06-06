import plotly.express as px
df = px.data.wind()
fig = px.line_polar(df, 'frequency', 'direction', 'strength', None, None, range_theta=None)