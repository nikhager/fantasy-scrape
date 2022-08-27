# FANTASY BASKETBALL WEBSCRAPER

# IMPORTS
import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd


# FUNCTIONS
def split_col(tbl, col_name, idx):
    for word in tbl.loc[:, col_name]:
        print(word.split()[idx])

# SETUP

url = "https://fantasy.espn.com/basketball/livedraftresults?leagueId=33775603"
# https://hashtagbasketball.com/fantasy-basketball-projections
r = req.get(url)
data = r.content

soup = bs(data, "html.parser")
table = soup.find_all('table')[2]
df = pd.read_html(str(table))[0]

# CLEAN

# # delete extra rows
# for word in df.loc[:, 'R#']:
#     if word == 'R#':
#         pass

# FNAME LNAME COLUMNS

# NOTES COLUMN
# df.insert(loc = -1, column = 'Notes', value = new_col)

# EXPORT TO CSV
df.to_excel('fantasy_data3.xlsx')
