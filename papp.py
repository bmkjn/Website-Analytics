

import pandas as pd
import dash
from dash import dcc
import dash_core_components as dcc
from dash import html
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

wdf = pd.read_csv('/Users/bhumikajain/Downloads/website_performance.csv')

line_chart = px.line(wdf, x='Month', y='Page_Load_Time', title='Page Load Time Trend Over Time')
line_chart.update_xaxes(title_text='Month')
line_chart.update_yaxes(title_text='Page Load Time (seconds)')

bar_chart = px.bar(wdf, x='Month', y=['Bounce_Rate', 'Conversion_Rate'],
                   title='Bounce Rate vs. Conversion Rate Across Months')
bar_chart.update_xaxes(title_text='Month')
bar_chart.update_yaxes(title_text='Percentage')

appp = dash.Dash(__name__)

appp.layout = html.Div([
    dcc.Graph(figure=line_chart),
    dcc.Graph(figure=bar_chart)
])

if __name__ == '__main__':
    appp.run_server(debug=True)
















