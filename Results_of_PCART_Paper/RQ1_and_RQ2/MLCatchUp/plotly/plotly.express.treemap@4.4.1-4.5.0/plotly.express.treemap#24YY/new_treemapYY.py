import plotly.express as px
df = px.data.tips()
fig = px.treemap(df, None, 'total_bill', None, ids=None, color=None, path=None)