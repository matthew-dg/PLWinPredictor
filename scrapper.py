import pandas as pd

def scraper (url):
    table = pd.read_html(url)[0]
    #tidy up table, remove notes section and lines between rows 
    table = table.iloc[:, :-1]
    return table 
