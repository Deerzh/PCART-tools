import plotly.express as px
df = px.data.carshare()
fig = px.scatter_mapbox(df, 'centroid_lat', 'centroid_lon', 'peak_hour', text=None, center=None, mapbox_style=None)