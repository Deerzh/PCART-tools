import plotly.express as px
df = px.data.wind()
fig = px.bar_polar(df, 'frequency', 'direction', 'strength', None, None, None, None, None, None, None, None, None, None, None, None, None, None, barmode='relative', pattern_shape=None, pattern_shape_sequence=None, pattern_shape_map=None)
