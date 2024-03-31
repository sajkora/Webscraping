import requests
from bs4 import BeautifulSoup
import pandas as pd
from playwright.sync_api import sync_playwright
from time import sleep

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.coingecko.com/en/all-cryptocurrencies")
    print(page.title())
    for _ in range (1,6):
        page.click(selector='[data-target="all-coins.showMore"]')
        sleep(0.5)
    kontent = page.content()
    browser.close()

tables = []
soup = BeautifulSoup(kontent, 'html.parser')
df_list = pd.read_html(str(soup))
for df in df_list:
    tables.append(df)

master_table = pd.concat(tables)
master_table = master_table.loc[:,master_table.columns[1:-1]]
master_table.to_csv('Crypto Data.csv', index=False)
