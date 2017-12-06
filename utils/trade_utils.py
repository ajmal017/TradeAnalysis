'''
    This will contain required functions/utilities used by all  modules
'''
import math
import os
import re
from conf import constants
import fpdf
import csv
import datetime
import pandas as pd
import requests


from Templates import open_high_low_templ
import xlsxwriter as xlsx

def generate_gann_square(price):
    ''' This will give list of all Gann Values for the specified stock value '''
    sqrt_price = int(math.sqrt(price)-1)
    gann_square = [round((sqrt_price+gann_quot)**2, constants.NUM_DECIMAL_PLACES)
                   for gann_quot in constants.GANN_QUOTIENTS]
    return gann_square

def generate_pdf_olh_intra(olh_trade_class_list,pdf_file_name):
    '''
    This will create pdf file
    :param olh_trade_class_list:
    :param pdf_file_name:
    :return:
    '''
    pdf_fh = fpdf.FPDF()
    pdf_fh.add_page()
    pdf_header_string = constants.HEADER_OPEN_HIGH_LOW
    pdf_fh.set_font('Courier', size=9)
    pdf_fh.write(5, txt=pdf_header_string)

    for index,olh_trade_class in enumerate(olh_trade_class_list):

        pdf_string = ''
        pdf_fh.add_page()
        if olh_trade_class.trade_str.find(constants.SELL_STRING) != constants.STR_NOT_FOUND_VALUE:
            pdf_fh.set_font('Courier',size=7)
            oh_string = open_high_low_templ.OH_STRING
            oh_string = str(index+1)+" . "+oh_string
            pdf_fh.set_text_color(255,0,0)
            print(oh_string)
            oh_string = oh_string.replace('#SCRIPT#', str(olh_trade_class.script))
            oh_string = oh_string.replace('#CMP#', str(olh_trade_class.ltp))

            if olh_trade_class.ltp < olh_trade_class.atp:
                oh_string = oh_string.replace('#TRADE_ATP#', "YES")
            else:
                oh_string = oh_string.replace('#TRADE_ATP#', "NO")

            if olh_trade_class.ltp < olh_trade_class.ipivot:
                oh_string = oh_string.replace('#TRADE_PIVOT#', "YES")
            else:
                oh_string = oh_string.replace('#TRADE_PIVOT#', "NO")

            if olh_trade_class.ltp < olh_trade_class.pclose:
                oh_string = oh_string.replace('#TRADE_PCLOSE#', "YES")
            else:
                oh_string = oh_string.replace('#TRADE_PCLOSE#', "NO")

            oh_string = oh_string.replace('#SL#', str(olh_trade_class.sl))
            oh_string = oh_string.replace('#ENTRY3#', str(olh_trade_class.entry3))
            oh_string = oh_string.replace('#ENTRY2#', str(olh_trade_class.entry2))
            oh_string = oh_string.replace('#ENTRY1#', str(olh_trade_class.entry1))

            oh_string = oh_string.replace('#TARGET1#', str(olh_trade_class.target1))
            oh_string = oh_string.replace('#TARGET2#', str(olh_trade_class.target2))
            oh_string = oh_string.replace('#TARGET3#', str(olh_trade_class.target3))
            oh_string = oh_string.replace('#TARGET4#', str(olh_trade_class.target4))
            oh_string = oh_string.replace('#TARGET5#', str(olh_trade_class.target5))

            oh_string = oh_string.replace('#LOW_MADE#', str(olh_trade_class.low))

            reg_exp = re.compile(constants.NSE_STRING+"-(.*?),")
            nse_signal = reg_exp.search(olh_trade_class.trade_str)
            print ("NSE_SIGNAL",nse_signal.groups()[0])

            reg_exp = re.compile(constants.BSE_STRING + "-(.*?)_")
            bse_signal = reg_exp.search(olh_trade_class.trade_str)
            print ("BSE_SIGNAL",bse_signal.groups()[0])
            oh_string = oh_string.replace('#NSE_SIGNAL#', nse_signal.groups()[0])
            oh_string = oh_string.replace('#BSE_SIGNAL#', bse_signal.groups()[0])
            pdf_string = oh_string
        elif olh_trade_class.trade_str.find(constants.BUY_STRING) != constants.STR_NOT_FOUND_VALUE :
            pdf_fh.set_font('Courier',size=7)
            ol_string = open_high_low_templ.OL_STRING
            ol_string = str(index+1) + " . "+ol_string
            pdf_fh.set_text_color(0,0,255)
            ol_string = ol_string.replace('#SCRIPT#', str(olh_trade_class.script))
            ol_string = ol_string.replace('#CMP#', str(olh_trade_class.ltp))

            if olh_trade_class.ltp > olh_trade_class.atp:
                ol_string = ol_string.replace('#TRADE_ATP#', "YES")
            else:
                ol_string = ol_string.replace('#TRADE_ATP#', "NO")

            if olh_trade_class.ltp > olh_trade_class.ipivot:
                ol_string = ol_string.replace('#TRADE_PIVOT#', "YES")
            else:
                ol_string = ol_string.replace('#TRADE_PIVOT#', "NO")

            if olh_trade_class.ltp > olh_trade_class.pclose:
                ol_string = ol_string.replace('#TRADE_PCLOSE#', "YES")
            else:
                ol_string = ol_string.replace('#TRADE_PCLOSE#', "NO")

            ol_string = ol_string.replace('#SL#', str(olh_trade_class.sl))
            ol_string = ol_string.replace('#ENTRY3#', str(olh_trade_class.entry3))
            ol_string = ol_string.replace('#ENTRY2#', str(olh_trade_class.entry2))
            ol_string = ol_string.replace('#ENTRY1#', str(olh_trade_class.entry1))

            ol_string = ol_string.replace('#TARGET1#', str(olh_trade_class.target1))
            ol_string = ol_string.replace('#TARGET2#', str(olh_trade_class.target2))
            ol_string = ol_string.replace('#TARGET3#', str(olh_trade_class.target3))
            ol_string = ol_string.replace('#TARGET4#', str(olh_trade_class.target4))
            ol_string = ol_string.replace('#TARGET5#', str(olh_trade_class.target5))

            ol_string = ol_string.replace('#HIGH_MADE#', str(olh_trade_class.high))

            reg_exp = re.compile(constants.NSE_STRING + "-(.*?),")
            nse_signal = reg_exp.search(olh_trade_class.trade_str)
            print("NSE_SIGNAL", nse_signal.groups()[0])

            reg_exp = re.compile(constants.BSE_STRING + "-(.*?)_")
            bse_signal = reg_exp.search(olh_trade_class.trade_str)
            print("BSE_SIGNAL", bse_signal.groups()[0])
            ol_string = ol_string.replace('#NSE_SIGNAL#', nse_signal.groups()[0])
            ol_string = ol_string.replace('#BSE_SIGNAL#', bse_signal.groups()[0])
            pdf_string = ol_string

        #pdf_fh.text(x=10,y=20,txt = oh_string)
        pdf_fh.write(5, txt = pdf_string)

    pdf_fh.output(pdf_file_name, "F")


def generate_excel_olh_intra(olh_trade_class_list,xls_file_name):
    '''
    This will create pdf file
    :param olh_trade_class_list:
    :param pdf_file_name:
    :return:
    '''
    columns = [
                  'SCRIPT', 'NSE', 'BSE', 'TRADE'
               , 'ENTRY1','ENTRY2', 'ENTRY3', 'SL'
               , 'TARGET1', 'TARGET2', 'TARGET3'
               , 'TARGET4', 'TARGET5'
    ]
    workbook = xlsx.Workbook(xls_file_name)
    format_blue = workbook.add_format({'bold': True, 'font_color': 'blue'})
    format_red = workbook.add_format({'font_color': 'red'})
    format_green = workbook.add_format({'font_color': 'green'})

    worksheet = workbook.add_worksheet('Open=High-Low')
    for index,column in enumerate(columns):
        worksheet.write(constants.START+constants.ROWS_SKIP, index, column,format_blue)
    for index,olh_trade_class in enumerate(olh_trade_class_list):
        if olh_trade_class.trade_str.find(constants.SELL_STRING) != constants.STR_NOT_FOUND_VALUE:
            pass
        elif olh_trade_class.trade_str.find(constants.BUY_STRING) != constants.STR_NOT_FOUND_VALUE:
            pass

    workbook.close()


def get_google_finance_intraday(ticker, period=60, days=1,exchange="NSE"):
    """
    Retrieve intraday stock data from Google Finance.
    Parameters
    ----------
    ticker : str
        Company ticker symbol.
    period : int
        Interval between stock values in seconds.
    days : int
        Number of days of data to retrieve.
    Returns
    -------
    df : pandas.DataFrame
        DataFrame containing the opening price, high price, low price,
        closing price, and volume. The index contains the times associated with
        the retrieved price values.
    """
    uri = "https://finance.google.com/finance/getprices?p={days}d&i={period}&f=d,o,h,l,c,v&q={ticker}&x={exch}".format(
        days=days, period=period, ticker=ticker,exch=exchange)
    response = requests.get(url=uri)
    # print(type(response))
    # print (type(response.content))
    # print (response.text)
    #
    reader = csv.reader((response.content.decode("utf-8")).splitlines())
    print(type(reader))
    rows = []
    columns = ['Close', 'High', 'Low', 'Open', 'Volume']
    times = []
    # Skip first 7 rows as it contains header info
    for row in reader:
        print (row)
        if re.match('^[a\d]', row[0]):
            if row[0].startswith('a'):
                start = datetime.datetime.fromtimestamp(int(row[0][1:]))
                times.append(start)
            else:
                times.append(start+datetime.timedelta(seconds=period*int(row[0])))
            rows.append(map(float, row[1:]))
    if len(rows):
        return pd.DataFrame(rows, index=pd.DatetimeIndex(times, name='Date'),
                            columns=columns)
    else:
        return pd.DataFrame(rows, index=pd.DatetimeIndex(times, name='Date'))

