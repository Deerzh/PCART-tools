import plotly.express as px
df = px.data.tips()
fig = px.density_contour(df, 'total_bill', 'tip', None, None, None, None, None, None, None, None, {}, {}, None, {}, None, None, None, None, False, False, None, None, None, None, nbinsx=None, nbinsy=None, title=None, template=None, width=None, facet_col_wrap=0)