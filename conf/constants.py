'''
Constants used in all modules

'''
# Constants for Intra day for google sheets.
# START COLUMN FOR READING OLH DATA

import os

START = 0
INTRA_OLH_END_INDEX = 12
NSE_SIGNAL_INDEX = 10
BSE_SIGNAL_INDEX = 11
INTRA_GOOGLE_SHEET_NAME = 'My OLH Intra System'

NSE_LTP_INDEX = 1
NSE_OPEN_INDEX = 2
NSE_HIGH_INDEX = 3
NSE_LOW_INDEX = 4
NSE_PCLOSE_INDEX = 5
NSE_VOLUME_INDEX = 6

BSE_LTP_INDEX = 8
BSE_OPEN_INDEX = 9
BSE_HIGH_INDEX = 10
BSE_LOW_INDEX = 11
BSE_PCLOSE_INDEX = 12
BSE_VOLUME_INDEX = 13


DATA_SKIP_ROWS = 3
NUM_DECIMAL_PLACES = 2

RESISTANCE_FILTER = 0.9995
SUPPORT_FILTER = 1.0005
BUY_SL_FILTER = 0.0006
SELL_SL_FILTER = 0.0006
BUY_ENTRY3_FILTER = 1.0003
SELL_ENTRY3_FILTER = 0.9997

GANN_QUOTIENTS = [
    0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 1
    , 1.125, 1.25, 1.375, 1.5, 1.625, 1.75, 1.875, 2
    , 2.125, 2.25, 2.375, 2.5, 2.625, 2.75, 2.875, 3
]
STR_NOT_FOUND_VALUE = -1

BUY_STRING = "BUY"
SELL_STRING = "SELL"

NSE_STRING = "NSE"
BSE_STRING = "BSE"

SUCCESS = 1
FAIL = 0

ROWS_SKIP = 5
HEADER_OPEN_HIGH_LOW = '''
    Once Trade Got Executed, Part Book at T2
    can see some bounce from T2
    Use Trialing SL for every next levels.
'''

ALL_SYMBOLS = ['ACC', 'ADANIENT', 'ADANIPORTS', 'ADANIPOWER', 'ABIRLANUVO', 'AJANTPHARM', 'ALBK', 'AMARAJABAT',
              'AMBUJACEM', 'ANDHRABANK', 'APOLLOHOSP', 'APOLLOTYRE', 'ARVIND', 'ASHOKLEY', 'ASIANPAINT', 'AUROPHARMA',
              'AXISBANK', 'BAJAJ-AUTO', 'BAJFINANCE', 'BANKBARODA', 'BANKINDIA', 'BATAINDIA', 'BEML', 'BEL',
              'BHARATFIN', 'BHARATFORG', 'BHEL', 'BPCL', 'BHARTIARTL', 'INFRATEL', 'BIOCON', 'BOSCHLTD', 'BRITANNIA',
              'CADILAHC', 'CAIRN', 'CANBK', 'CASTROLIND', 'CEATLTD', 'CENTURYTEX', 'CESC', 'CIPLA', 'COALINDIA',
              'COLPAL', 'CONCOR', 'CROMPGREAV', 'CUMMINSIND', 'DABUR', 'DHFL', 'DISHTV', 'DIVISLAB', 'DLF', 'DRREDDY',
              'EICHERMOT', 'ENGINERSIN', 'EXIDEIND', 'GAIL', 'GLENMARK', 'GMRINFRA', 'GODREJCP', 'GODREJIND',
              'GRANULES', 'GRASIM', 'HAVELLS', 'HCLTECH', 'HDFCBANK', 'HEROMOTOCO', 'HEXAWARE', 'HINDALCO', 'HINDPETRO',
              'HINDUNILVR', 'HINDZINC', 'HDIL', 'HDFC', 'ICICIBANK', 'IDBI', 'IDEA', 'IDFC', 'IFCI', 'IBULHSGFIN',
              'IBREALEST', 'IOC', 'ICIL', 'IGL', 'INDUSINDBK', 'INFY', 'IRB', 'ITC', 'JISLJALEQS', 'JPASSOCIAT',
              'JETAIRWAYS', 'JINDALSTEL', 'JSWENERGY', 'JSWSTEEL', 'JUBLFOOD', 'JUSTDIAL', 'KSCL', 'KOTAKBANK', 'KPIT',
              'LT', 'LICHSGFIN', 'LUPIN', 'MARICO', 'MARUTI', 'MCLEODRUSS', 'MINDTREE', 'MOTHERSUMI', 'MRF', 'NCC',
              'NHPC', 'NIITTECH', 'NMDC', 'NTPC', 'ONGC', 'OIL', 'OFSS', 'ORIENTBANK', 'PAGEIND', 'PCJEWELLER',
              'PETRONET', 'PIDILITIND', 'PFC', 'POWERGRID', 'PTC', 'PNB', 'RELCAPITAL', 'RCOM', 'RELIANCE', 'RELINFRA',
              'RPOWER', 'RECLTD', 'SRTRANSFIN', 'SIEMENS', 'SINTEX', 'SRF', 'SBIN', 'SAIL', 'STAR', 'SUNPHARMA',
              'SUNTV', 'SYNDIBANK', 'TATACHEM', 'TATACOMM', 'TCS', 'TATAELXSI', 'TATAGLOBAL', 'TATAMOTORS',
              'TATAMTRDVR', 'TATAPOWER', 'TATASTEEL', 'TECHM', 'FEDERALBNK', 'INDIACEM', 'KTKBANK', 'SOUTHBANK',
              'TITAN', 'TORNTPHARM', 'TV18BRDCST', 'TVSMOTOR', 'ULTRACEMCO', 'UNIONBANK', 'UNITECH', 'UBL',
              'MCDOWELL-N', 'UPL', 'VEDL', 'VOLTAS', 'WIPRO', 'WOCKPHARMA', 'YESBANK', 'ZEEL']




PERCENT_ONE = 1
PERCENT_TWO = 2
PERCENT_THREE = 3
PERCENT_FOUR = 4
PERCENT_FIVE = 5
PERCENT_SIX = 6
PERCENT_SEVEN = 7

TIME_FORMAT = "%Y-%m-%d %H:%M:00"
FILE_TIME_FORMAT = "%Y-%m-%d_%H_%M_00"
FILE_PDF_EXTENSION = ".pdf"
DATE_FORMAT = "%Y-%m-%d"

FILES_LOCATION  = "Files"
#MAIL_TO = ['varaparla.raja@gmail.com', 'tradeuser2018@gmail.com', 'kmasani81@gmail.com']
MAIL_TO = ['varaparla.raja@gmail.com', 'tradeuser2018@gmail.com']


# intra_olh_trade column Names.


INTRA_OLH_TRADE_TICKER = "ticker"
INTRA_OLH_TRADE_TRADE_DATE = "TradeDate"
INTRA_OLH_TRADE_TRADE_TIME = "TradeTime"
INTRA_OLH_TRADE_OPEN = "Open"
INTRA_OLH_TRADE_HIGH = "High"
INTRA_OLH_TRADE_LOW = "Low"
INTRA_OLH_TRADE_CLOSE = "Close"
INTRA_OLH_TRADE_PCLOSE = "PClose"
INTRA_OLH_TRADE_ATP = "Atp"
INTRA_OLH_TRADE_IPIVOT = "Ipivot"
INTRA_OLH_TRADE_NSE_TRADE = "NSE_Trade"
INTRA_OLH_TRADE_BSE_TRADE = "BSE_Trade"
INTRA_OLH_TRADE_ENTRY1 = "Entry1"
INTRA_OLH_TRADE_ENTRY2 = "Entry2"
INTRA_OLH_TRADE_ENTRY3 = "Entry3"
INTRA_OLH_TRADE_SL = "SL"
INTRA_OLH_TRADE_TARGET1 = "Target1"
INTRA_OLH_TRADE_TARGET2 = "Target2"
INTRA_OLH_TRADE_TARGET3 = "Target3"
INTRA_OLH_TRADE_TARGET4 = "Target4"
INTRA_OLH_TRADE_TARGET5 = "Target5"


TIME_930 = "09:30:00"
TIME_5MIN = "5min"
TIME_15MIN = "15min"
TIME_30MIN = "30min"
TIME_HOUR = "hour"


tables_time = {"5min":"intra_data_5min"
    , "15min":"intra_data_15min"
    , "30min":"intra_data_30min"
    , "hour":"intra_data_hour"
               }













