import plotly.graph_objects as go
import plotly.io as pio
fig = go.Figure(data=[go.Bar(y=[2, 3, 1])], layout_title_text='A Bar Chart')
pio.write_html(fig=fig, file='bar_chart.html', config=None, auto_play=True, include_plotlyjs=True, div_id=None)
