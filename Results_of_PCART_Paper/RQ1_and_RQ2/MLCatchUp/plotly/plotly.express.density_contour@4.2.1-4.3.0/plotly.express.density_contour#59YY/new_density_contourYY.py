import plotly.express as px
df = px.data.tips()
fig = px.density_contour(df, 'total_bill', 'tip', None, None, None, None, hover_name=None, hover_data=None, animation_frame=None, facet_col_wrap=0)
