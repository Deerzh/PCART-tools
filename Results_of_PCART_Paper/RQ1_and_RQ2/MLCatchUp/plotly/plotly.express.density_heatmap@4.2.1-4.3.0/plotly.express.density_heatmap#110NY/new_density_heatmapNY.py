import plotly.express as px
df = px.data.tips()
fig = px.density_heatmap(df, 'total_bill', 'tip', None, None, None, None, None, None, None, category_orders={}, labels={}, color_continuous_scale=None, range_color=None, facet_col_wrap=0)
