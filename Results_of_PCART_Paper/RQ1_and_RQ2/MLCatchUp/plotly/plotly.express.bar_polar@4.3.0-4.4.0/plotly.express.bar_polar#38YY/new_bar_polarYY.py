import plotly.express as px
df = px.data.wind()
fig = px.bar_polar(df, 'frequency', 'direction', 'strength', None, None, None, animation_frame=None, range_theta=None)
