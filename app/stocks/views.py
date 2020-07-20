from flask import (
    Blueprint,
    render_template,
    request,
)

import pandas as pd
import pandas_datareader as pdr


blueprint = Blueprint(
    'stocks',
    __name__,
    url_prefix='/stocks',
)

@blueprint.route('/', methods=['GET', 'POST'])
def index():
    data = None
    if request.method == 'POST':
        symbol = request.form.get('symbol')
        source = request.form.get('source', 'yahoo')
        if symbol:
            df = pdr.DataReader(symbol, source, '2020-01-01')
            data = df.to_html(classes='table table-striped table-hover')
    return render_template('stocks/index.html', data=data)
