from scrapper import scraper
from pythag_expct import pythag_expct

if __name__ == "__main__":
    table = scraper("https://fbref.com/en/comps/9/Premier-League-Stats")
    print(pythag_expct(table, 'Manchester Utd'))
