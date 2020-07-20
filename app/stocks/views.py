from flask import (
    Blueprint,
    render_template,
    request,
)

import pandas as pd
import pandas_datareader as pdr

import pygal

blueprint = Blueprint(
    'stocks',
    __name__,
    url_prefix='/stocks',
)

@blueprint.route('/', methods=['GET', 'POST'])
def index():
    data = None
    chart = None
    if request.method == 'POST':
        symbol = request.form.get('symbol')
        source = request.form.get('source', 'yahoo')
        if symbol:
            df = pdr.DataReader(symbol, source, '2020-01-01')
            chart = make_chart(df, source, symbol, 30)
            data = df.to_html(classes='table table-striped table-hover')
    return render_template('stocks/index.html', data=data, chart=chart)


def make_chart(data_frame, stype, symbol, days):
    head = [pd.to_datetime(str(d)).strftime('%Y-%m-%d') \
        for d in data_frame[-days:].index.values]
    data = [d[-1 if stype == 'yahoo' else -2] \
        for d in data_frame[-days:].values]

    line_chart = pygal.Line(x_label_rotation=35)
    line_chart.title = f'Price of the last {days} trading days'
    line_chart.x_labels = head
    line_chart.add(symbol, data)
    return line_chart.render_data_uri()
