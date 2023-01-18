from scrapper import scraper
from pythag_expct import pythag_expct

table = scraper("https://fbref.com/en/comps/9/Premier-League-Stats")
print(pythag_expct(table, 'Manchester Utd'))