import requests
import json
import re

def search(arg):

    # arg is a nascode and is mandatory

    # Return nothing if client didn't pass in a nascode parameter
    if not ('nascode' in arg):
        return

    # retrieve nascode from request parameter
    nascode = arg['nascode']

    # Construct an access URL for the NASC API
    r = requests.get('http://webservices.arabidopsis.info:3000/stock/' + nascode)

    if r.ok:
        return r.headers['Content-Type'], r.content
    else:
        return 'text/plaintext; charset=ISO-8859-1', 'An error occurred on the remote server'

def list(arg):

    """Retrieves a list of all stocks
    no parameters required
    """                                   
    pass
