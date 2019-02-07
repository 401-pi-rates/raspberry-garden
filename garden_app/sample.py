"""This module defines the routes of stocks app."""
from . import app
from .auth import login_required

# 3rd Party Requirements
from flask import render_template, abort, redirect, url_for, session, g, request, flash
from sqlalchemy.exc import IntegrityError, DBAPIError

# Models
from .models import Company, db, Portfolio

# Forms
from .forms import StockSearchForm, CompanyAddForm, PortfolioCreateForm

# API Requests & Other
from json import JSONDecodeError
import requests as req
import json
import os

# Numpy & Charts
import numpy as np
from datetime import datetime
import pandas as pd
import numpy.polynomial.polynomial as poly
import bokeh.plotting as bk
from bokeh.models import HoverTool, Label, BoxZoomTool, PanTool, ZoomInTool, ZoomOutTool, ResetTool
from pandas.plotting._converter import DatetimeConverter
from bokeh.embed import components
from bokeh.layouts import gridplot
# import matplotlib
# import matplotlib.pyplot as plt


@login_required
@app.route('/stock_chart/<symbol>', methods=['GET', 'POST'])
def stock_chart(symbol):
    """To generate a stock chart of the chosen company."""

    res = req.get(f'https://api.iextrading.com/1.0/stock/{symbol}/chart/5y')
    data_5_year = res.json()

    df = pd.DataFrame(data_5_year)

    df['date_pd'] = pd.to_datetime(df.date)
    df['year'] = df.date_pd.dt.year

    year_num = df.year[int(len(df)-1)] - df.year[3]

    if year_num >= 5:

        # 5 YEARS OF HISTORY IS AVAILABLE

        # PASS DATA INTO DATAFRAME

        df['mid'] = (df.high + df.low) // 2

        def datetime(x):
            return np.array(x, dtype=np.datetime64)


        # PLOTTING THE CHART
        p1 = bk.figure(x_axis_type="datetime", title=f'Company: {symbol}', toolbar_location='above')
        p1.grid.grid_line_alpha=0.3
        p1.xaxis.axis_label = 'Date'
        p1.yaxis.axis_label = 'Dollar'


        # CHART LAYOUT
        p1.line(datetime(df['date']), df['open'], color='yellow', legend=f'{symbol}')
        p1.line(datetime(df['date']), df['close'], color='purple', legend=f'{symbol}')
        p1.line(datetime(df['date']), df['high'], color='red', legend=f'{symbol}')
        p1.line(datetime(df['date']), df['low'], color='green', legend=f'{symbol}')
        p1.line(datetime(df['date']), df['mid'], color='black', legend=f'{symbol}')

        p1.legend.location = "top_left"

        script, div = components(p1)

        return render_template("stock_chart.html", the_div=div, the_script=script)

    else:
        # 5-YEAR DATA IS NOT AVAILABLE
        flash('Company does not have a 5-year history.')
        return redirect(url_for('.portfolio_detail'))
