import plotly.express as px
df = px.data.wind()
fig = px.line_polar(df, 'frequency', 'direction', 'strength', None, None, None, custom_data=None, line_group=None, text=None, animation_frame=None, range_theta=None)