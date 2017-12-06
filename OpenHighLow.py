'''
    This will read data from Google Spread Sheets and Generate Trade Plan.
    This is Open=High/ Open=Low Strategy
'''

import os # OS Related
import json # JSON related
import gspread # Google Spread Sheets

from oauth2client.client import SignedJwtAssertionCredentials # Authention related

from IntraStratagies import open_high_low as olh
from utils import trade_utils

# Get the base project Dir
BASEDIR = os.path.dirname(os.getcwd())
#CONFDIR = BASEDIR+os.sep+"conf"
CONFDIR = os.getcwd()+os.sep+"conf"
# Credential file
CREDENTIALS_FILE = CONFDIR+os.sep+"creds.json"

# Load Credentials
JSON_KEY = json.load(open(CREDENTIALS_FILE))
SCOPE = ['https://spreadsheets.google.com/feeds']
# Get the Credentials from 'client_email' and 'private_key'
CREDENTIALS = SignedJwtAssertionCredentials(JSON_KEY['client_email']
                                            , JSON_KEY['private_key'].encode()
                                            , SCOPE)
# Authorize Google Client using Credentials
CLIENT = gspread.authorize(CREDENTIALS)


if __name__ == "__main__":
    OLH_SCRIPTS = olh.sheets_get_olh_data(CLIENT)
    # print([str(x) for x in olh_scripts])
    OLH_TRADES = olh.sheets_generate_olh_trade_data(OLH_SCRIPTS)
    trade_utils.generate_pdf_olh_intra(OLH_TRADES,"test.pdf")
    print("\n".join(str(x) for x in OLH_TRADES))
    trade_utils.generate_excel_olh_intra(OLH_TRADES,'test.xlsx')