import dash_bootstrap_components as dbc
from dash import dcc
# import dash_core_components as dcc
# import dash_html_components as html
from dash import html
from dash.dependencies import Input, Output
from dash_html_components import Img

from app import app
from app import server

from apps import home, selling, hypo

app.layout = html.Div([
    dbc.NavbarSimple(
        brand="DASHBOARD",
        brand_href="/apps/home",
        sticky='top',
        color="navy",
        dark=True,
        children=[
            dbc.ButtonGroup(
                [
                    dbc.Button("Visualization",  href='/apps/visual'),
                    dbc.Button("Hypothesis", href='/apps/hypo'),
                    dbc.DropdownMenu(
                        [dbc.DropdownMenuItem('DATASET', href='https://www.kaggle.com/aungpyaeap/supermarket-sales'),
                         dbc.DropdownMenuItem("GITHUB", href='https://github.com/herfian')],
                        label="Data",
                        group=True,
                    ),
                ]
            ),
        ]
    ),

    dcc.Location(id='url'),
    html.Div(id='page-content', children=[]),
    html.Div(
        dbc.Row(dbc.Col(html.Div("© Copyright by Herfian"), className="text-center"),
                align="center",
                justify="center"
                ),
        className="p-4  bg-primary text-white"
    )

])

# Show page content below the navbar using callback


@app.callback(
    Output(component_id='page-content', component_property='children'),
    [Input(component_id='url', component_property='pathname')])
def display_page(pathname):
    if pathname == '/apps/visual':
        return selling.layout
    elif pathname == '/apps/hypo':
        return hypo.layout
    else:
        return home.layout


if __name__ == '__main__':
    app.run_server(debug=True)