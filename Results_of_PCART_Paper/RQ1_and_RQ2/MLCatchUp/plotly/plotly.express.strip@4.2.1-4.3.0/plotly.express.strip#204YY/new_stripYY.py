import plotly.express as px
df = px.data.tips()
fig = px.strip(df, 'total_bill', 'day', None, None, None, hover_name=None, hover_data=None, custom_data=None, animation_frame=None, animation_group=None, category_orders={}, labels={}, color_discrete_sequence=None, color_discrete_map={}, orientation='v', stripmode='group', log_x=False, log_y=False, facet_col_wrap=0)