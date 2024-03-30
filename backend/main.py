from bs4 import BeautifulSoup
import requests
import pandas as pd

#pip install bs4
#pip install requests
#pip install pandas
#jesli te komendy nie dzialaja upewnij sie ze masz otwarty caly folder backend tak zeby pojawial sie tez folder .idea

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.6; Win64; x64) Gecko/20100101 Firefox/86'
         'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=',
         'Accept-language': 'en-US,en;q=0.5',
         'Connection': 'keep-alive',
         'Upgrade-Insecure-Requests': '1',
         'Cache-Control': 'max-age=0'
         }



base_url='https://www.coingecko.com/en/all-cryptocurrencies'

tables = []


response = requests.get(base_url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
df_list = pd.read_html(str(soup))
for df in df_list:
    tables.append(df)

master_table = pd.concat(tables)
master_table = master_table.loc[:,master_table.columns[1:-1]]
master_table.to_csv('Crypto Data.csv', index=False)