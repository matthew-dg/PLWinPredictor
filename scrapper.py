import pandas as pd

def scrape (url):
    table = pd.read_html(url)[0]
    #tidy up table, remove notes section and lines between rows 
    table = table[::2].iloc[:, :-1]
    return table 
