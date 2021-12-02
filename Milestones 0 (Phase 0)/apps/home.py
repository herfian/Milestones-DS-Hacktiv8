from dash_bootstrap_components._components.Row import Row
# import dash_html_components as html
from dash import html
import dash_bootstrap_components as dbc

# Basic homepage with two cards and two buttons
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                dbc.Jumbotron(
                      html.H1("WELCOME TO DASHBOARD",
                              className="display-4 text-center font-weight-bold")
                  
                  ),

            )
        ]),

        dbc.Row([
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                html.H4("VISUALIZATION",
                                        className="card-title text-center"),
                                dbc.CardImg(
                                    src="/assets/img/analysis.png", top=True,),
                                html.P(
                                    "Visualization data with violin, bar, scatter, and pie chart",
                                    className="card-text text-center",
                                ),
                                dbc.Button(
                                    "Go Visualization", className="text-center btn-lg", block=True, color="primary", href="/apps/visual"),
                            ]
                        ),
                    ],
                    style={"width": "80%"},
                ),
                width=4, className="mb-6",
            ),


            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                html.H4("HYPOTHESIS",
                                        className="card-title text-center"),
                                dbc.CardImg(
                                    src="/assets/img/machine-learning.png", top=True,),
                                html.P(
                                    "Hypothesis with Two Sample Test",
                                    className="card-text text-center",
                                ),
                                dbc.Button(
                                    "Go Hypothesis", className="text-center btn-lg", block=True, color="primary", href="/apps/hypo"),
                            ]
                        ),
                    ],
                    style={"width": "80%"},
                ),
                width=4, className="mb-6",
            ),
        ],
            justify="around",
            align="end",
            className="mb-5"
        ),
    ], fluid=True)

])