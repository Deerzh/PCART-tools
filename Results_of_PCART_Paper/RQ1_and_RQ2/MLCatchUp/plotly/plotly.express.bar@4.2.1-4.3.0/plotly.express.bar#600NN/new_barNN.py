import plotly.express as px
data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, 'year', 'pop', None, None, None, None, None, None, None, None, None, None, None, None, None, {}, {}, None, {}, None, None, None, None, 'v', 'relative', False, False, None, None, title=None, template=None, width=None, height=None, facet_col_wrap=0)