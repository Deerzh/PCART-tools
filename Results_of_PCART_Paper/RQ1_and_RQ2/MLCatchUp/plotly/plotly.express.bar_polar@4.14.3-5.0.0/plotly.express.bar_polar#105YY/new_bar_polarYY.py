import plotly.express as px
df = px.data.wind()
fig = px.bar_polar(data_frame=df, r='frequency', theta='direction', color='strength', hover_name=None, hover_data=None, custom_data=None, base=None, animation_frame=None, animation_group=None, category_orders=None, labels=None, color_discrete_sequence=None, pattern_shape=None, pattern_shape_sequence=None, pattern_shape_map=None)
