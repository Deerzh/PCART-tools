import plotly.express as px
data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, 'year', 'pop', None, None, None, None, hover_data=None, custom_data=None, text=None, error_x=None, error_x_minus=None, facet_col_wrap=0)
