import plotly.express as px
df = px.data.tips()
fig = px.density_contour(df, 'total_bill', 'tip', None, None, None, None, None, None, None, None, {}, {}, None, {}, None, marginal_y=None, trendline=None, trendline_color_override=None, facet_col_wrap=0)
