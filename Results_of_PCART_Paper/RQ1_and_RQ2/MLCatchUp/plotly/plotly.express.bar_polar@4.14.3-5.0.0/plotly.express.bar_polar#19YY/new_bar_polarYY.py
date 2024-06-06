import plotly.express as px
df = px.data.wind()
fig = px.bar_polar(df, 'frequency', theta='direction', color='strength', hover_name=None, pattern_shape=None, pattern_shape_sequence=None, pattern_shape_map=None)