import plotly.express as px
df = px.data.wind()
fig = px.scatter_polar(df, 'frequency', 'direction', None, None, None, None, None, custom_data=None, text=None, animation_frame=None, animation_group=None, range_theta=None)
