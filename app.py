import base64
import io

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State

app = Dash(__name__)


def get_img_path(img_path: str) -> str:
    """Fix issues with local pngs not showing in dash's html.Img"""
    encoded_image = base64.b64encode(open(img_path, 'rb').read())
    return f"data:image/png;base64,{encoded_image.decode()}"


description = """Bokeda is designed to be a secure and locally hosted personal bookkeeper. Upload your bank 
statements at the end of the financial year, and it will automatically categorise your transactions before creating a 
dashboard for you to summarise and analyse your finances. At first, Bokeda will not know how to categorise your 
transactions, so you will be training it by selecting the category that you believe is most relevant to the 
transaction. Eventually, Bokeda will learn patterns in the transactions so that everything is automated (other than 
data it's never seen before)."""

app.layout = html.Div([
    html.Div([
        html.A(
            [
                html.Img(
                    src=get_img_path("images/GitHub-Mark-Light-120px-plus.png"),
                    alt="Github Repo Page",
                    draggable="false"
                )
            ], href="https://github.com/Zenoix/Bokeda", target="_blank", rel="noopener noreferrer", draggable="false")
    ], className="github_link"),

    html.Div([
        html.Div([
            html.H1([
                "Welcome to ", html.Span([
                    "Bokeda"
                ], id="name")
            ]),
            html.H2(["Automatic Bookkeeping Program"]),
            html.P([description]),
            html.H4([
                "Bokeda is completely locally hosted so no information will be transmitted through the "
                "internet unless your local machine is compromised."])
        ], className="info container"),
        dcc.Upload(
            id='drop_zone',
            children=html.Div([
                'Drag and Drop or ',
                html.A('Select Files')
            ]),

            # Allow multiple files to be uploaded
            multiple=True,
            accept=".csv, .tsv, .xlsx, .xls, .txt"
        ),
        html.Div(id='output-data-upload'),
    ], className="container")
])


def parse_contents(filename):
    return html.Div([
        html.H5(filename)
    ])


@app.callback(Output('output-data-upload', 'children'),
              Input('drop_zone', 'contents'),
              State('drop_zone', 'filename'))
def update_output(list_of_contents, list_of_names):
    if list_of_contents is not None:
        return [parse_contents(file_name) for file_name in list_of_names]


if __name__ == '__main__':
    app.run_server(debug=True)
