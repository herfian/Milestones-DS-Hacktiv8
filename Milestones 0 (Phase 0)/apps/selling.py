from numpy.core.fromnumeric import product
import plotly.express as px
import pandas as pd
import dash
# import dash_core_components as dcc
from dash import dcc
# import dash_html_components as html
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app

df = pd.read_csv('supermarket_clean.csv')
df.drop(['Invoice_id', 'Tax_5%', 'Time',
        'Cogs', 'Gross_margin_percent'], axis=1, inplace=True)
df['date'] = pd.to_datetime(df.date).dt.date
srt = df.sort_values('date', axis=0, ignore_index=True)

layout = html.Div([
    dbc.Container([
        dbc.Row(
            dbc.Col(
                dbc.Jumbotron(
                    [
                        html.H1("VISUALIZATION",
                                className="display-4 text-center font-weight-bold"),
                        html.Hr(className="my-2"),
                        html.H5(
                            "Visualisasi adalah rekayasa dalam membuat gambar, diagram atau animasi untuk tampilan informasi.",
                            className="text-center font-weight-light"
                        ),
                    ]
                ),
                width=12
            ),
        ),

        dbc.Spinner([
            dbc.Row([
                dbc.Col(
                    dcc.Dropdown(
                        id='product-filter',
                        options=[
                            {'label': Product_line, 'value': Product_line} for Product_line in df.Product_line.unique()
                        ],
                        value='Health and beauty'

                    ), md="6"
                ),
                dbc.Col(
                    dcc.Dropdown(
                        id='payment-filter',
                        options=[
                            {'label': pay, 'value': pay} for pay in df.Payment.unique()
                        ],
                        value='Ewallet'
                    )
                )
            ]),

            dbc.Row([
                    dbc.Col(dcc.Graph(id='graph-1'), width=6),
                    dbc.Col(dcc.Graph(id='graph-2'), width=6)
                    ]),

            dbc.Row([
                    dbc.Col(
                        dcc.Graph(
                            id='graph-3',
                            figure=px.scatter(
                                df, x='date', y='Gross_income', color='Product_line',
                                title='Gross Income by Product Line'
                            )
                        )
                    ),

                    dbc.Col(
                        dcc.Graph(
                            id='graph-4',
                            figure=px.bar(
                                srt,
                                x='date',
                                y='Gross_income',
                                color='City',
                                title='Gross Income by City'
                            )
                        )
                    )

                    ]),

            dbc.Row([
                dbc.Col([
                        html.P("Names:"),
                        dcc.Dropdown(
                            id='names',
                            value='Payment',
                            options=[{'value': x, 'label': x}
                                     for x in ['Payment', 'Customer_type', 'Gender', 'City']],
                            clearable=False
                        ),
                        ],
                        ),
                dbc.Col([
                    html.P("Values:"),
                    dcc.Dropdown(
                        id='values',
                        value='Gross_income',
                        options=[{'value': x, 'label': x}
                                 for x in ['Gross_income', 'sell', 'Total']],
                        clearable=False
                    ),

                ])
            ]),
            dbc.Spinner([
                dbc.Row([
                    dbc.Col([

                        dcc.Graph(id="pie-chart"),
                    ])
                ]),
            ], type="grow", color="warning"),
            # dbc.Row([dbc.Col(
            #     html.H5(
            #          "Gross Income by Product and Gender",
            #         className="text-left",
            #          ),
            #     className="mb-2 mt-5"
            # )]),
            # dbc.Row([
            #     dbc.Col(
            #         [
            #             dcc.Checklist(
            #                 id="checklist",
            #                 options=[{"label": x, "value": x}
            #                          for x in df.product_line.unique()],
            #                 value=df.product_line[:2],
            #                 labelStyle={'display': 'inline-block'}
            #             ),
            #             dcc.Graph(id="line-chart"),
            #         ]
            #     ),
            # ])

        ], type="grow", color="primary")
    ])
])


# @app.callback(
#     Output("line-chart", "figure"),
#     [Input("checklist", "value")])
# def update_line_chart(product_line):
#     #mask = df.groupby(['date', 'gender']).sum().reset_index()
#     mask = df.product_line.isin(product_line)
#     fig = px.line(
#         # mask,
#         df[mask],
#         x="date", y="sell", color='gender')
#     return fig


@app.callback(
    Output("pie-chart", "figure"),
    [Input("names", "value"),
     Input("values", "value")])
def generate_chart(names, values):
    fig = px.pie(df, values=values, names=names, hole=.3,
                 color_discrete_sequence=px.colors.sequential.RdBu)

    return fig


@ app.callback(
    Output('graph-1', 'figure'),
    Input('product-filter', 'value')
)
def update_graph1(Product_line):
    filtered = df[df.Product_line == Product_line]
    fig = px.bar(
        filtered,
        x='City',
        y='Gross_income',
        color='City',
        title=f'Gross income in {Product_line}'
    )
    return fig


@ app.callback(
    Output('graph-2', 'figure'),
    Input('payment-filter', 'value')
)
def update_graph2(pay):
    filtered = df[df.Payment == pay]
    fig = px.violin(
        filtered,
        x='Payment',
        y='Gross_income',
        color='Customer_type',
        title=f'Payment by {pay}'
    )
    return fig