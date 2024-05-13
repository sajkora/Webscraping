import requests
from bs4 import BeautifulSoup
import pandas as pd
from playwright.sync_api import sync_playwright
from time import sleep
import random
import csv
import os
from tkinter import filedialog
from tkinter import *
import shutil

def scrape_data():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.coingecko.com/en/all-cryptocurrencies")
        print(page.title())
        for _ in range (1,6):
            page.click(selector='[data-more-content-target="loadMoreButton"]')
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


def get_random_crypto():
    project_dir = "./"
    csv_file_path = os.path.join(project_dir, 'Crypto Data.csv')

    if not os.path.exists(csv_file_path):
        print(f"Error: The file '{csv_file_path}' does not exist.")
        return None

    if not os.path.isfile(csv_file_path):
        print(f"Error: The file '{csv_file_path}' is not a valid file.")
        return None

    if os.stat(csv_file_path).st_size == 0:
        print(f"Error: The file '{csv_file_path}' is empty.")
        return None

    try:
        with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)

            if not rows:
                print(f"Error: The file '{csv_file_path}' is empty or contains invalid data.")
                return None

            random_row = random.choice(rows)
            return random_row

    except Exception as e:
        print(f"Error: Failed to read the file '{csv_file_path}' due to the following error: {e}")
        return None
    
def download_csv_to_folder(directory=None):
    root = Tk()
    root.withdraw()

    if directory is None:
        folder_selected = filedialog.askdirectory()
    else:
        folder_selected = directory

    

    try:
        if os.path.exists("Crypto Data.csv"):
            destination_file_path = os.path.join(folder_selected, "Crypto Data.csv")

            shutil.copyfile("Crypto Data.csv", destination_file_path)
            print(f"File 'Crypto Data.csv' downloaded to: {destination_file_path}")
        else:
            print(f"Error: Source file '{"Crypto Data.csv"}' not found.")
    except Exception as e:
        print(f"Error occurred: {e}")

