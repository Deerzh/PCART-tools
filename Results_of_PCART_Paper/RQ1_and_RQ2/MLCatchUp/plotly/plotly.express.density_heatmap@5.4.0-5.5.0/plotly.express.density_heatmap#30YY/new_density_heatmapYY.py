import plotly.express as px
df = px.data.tips()
fig = px.density_heatmap(df, 'total_bill', 'tip', None, facet_row=None, facet_col=None, facet_col_wrap=0, text_auto=False)
