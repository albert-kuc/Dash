"""
This file was created following the YT video linked below posted by Charming Data
https://www.youtube.com/watch?v=acFOhdo_bxw

The content of this file is different than the one presented in the video, as some changes were introduced to discover
additional functionality. Nevertheless the core of the program remains similar. The key difference is that our generated
dashboard consists a dropdown list, which is linked here to individual data files, while the original video used various
data combinations from a single file. Additionally there is an exception handling empty data file error.

The initial Data Exploration section was commented out as not used in the final version. The reasoning behind the
decision to keep the section is to show what was used during the program development.
"""

import dash
import plotly.express as px
import pandas as pd
from pandas.errors import EmptyDataError
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input
import os

path = '_datasets/'
log_csv_files = [file for file in os.listdir(path) if file.endswith('.csv')]
print(log_csv_files)
#
# test = [{'label': x[:-4], 'value': x} for x in sorted(log_csv_files)]
# print(test)

# Data exploration with Pandas
# ----------------------------

# df = pd.read_csv('_datasets/record_df_data_only_01.csv', sep=';')
#
# print(df.head())
# print(df.tail())
# print(df['[Position]'])
# print(df['[Force]'])

# Data visualization with Plotly

# fig_scatter = px.scatter(x=df['[Position'], y=df['[Force]'])

# fig = px.line(df, x='[Position]', y='[Force]')
# fig.show()

# Interactive Graphing with Dash
# -----------------------------

app = dash.Dash(__name__)

app.layout = html.Div([
    # Title
    html.H1("Graph Analysis"),
    dcc.Dropdown(id='file_choice',
                 # options is always a list of dictionaries
                 options=[{'label': x[:-4], 'value': x}
                          for x in sorted(log_csv_files)],
                 value=log_csv_files[-1]
                 ),
    dcc.Graph(id='my-graph', figure={}
              )
])


# callback to make Dropdown interactive: decorator + function
@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    Input(component_id='file_choice', component_property='value')
)
def interactive_graphing(value_file):
    print(value_file)
    try:
        df = pd.read_csv(os.path.join('_datasets/', value_file), sep=';')
    except EmptyDataError:
        # print('empty')
        df = pd.DataFrame(columns=['[Position]', '[Force]'])

    fig = px.line(df, x='[Position]', y='[Force]')
    return fig


if __name__ == '__main__':
    app.run_server()
