import plotly.express as px
df = px.data.tips()
fig = px.histogram(data_frame=df, x='total_bill', y=None, color=None, facet_row=None, pattern_shape=None, pattern_shape_sequence=None, pattern_shape_map=None)
