import plotly.express as px
df = px.data.wind()
fig = px.bar_polar(df, 'frequency', 'direction', 'strength', None, None, None, None, animation_frame=None, animation_group=None, category_orders=None, labels=None, pattern_shape=None, pattern_shape_sequence=None, pattern_shape_map=None)