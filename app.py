from dash import Dash, html, dcc, callback, Input, Output
import dash_ag_grid as grid
from process_data import process_data
import plotly.express as px

app = Dash()

data = process_data()
app.layout = [
    html.H1(children="Daily Sales of Pink Morsels", style={'textAlign': 'center'}),
    html.Br(),
    grid.AgGrid(
        rowData=data.to_dict('records'),
        columnDefs=[{"field":i} for i in data.columns]
    ),
    html.Br(),
    dcc.RadioItems(options=['region','date'], value='date', inline=True, id='controls-and-radio-item'),
    dcc.Graph(figure={}, id='controls-and-graph')
]

@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(data, x=col_chosen, y='sales')
    return fig

if __name__ == '__main__':
    app.run(debug=True)