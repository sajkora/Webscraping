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
from flask import flash


def clean_text(text):
    """ Utility function to clean text by removing extra spaces and newlines. """
    if text:
        return ' '.join(text.split())
    return 'N/A'
def scrape_data():
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.coingecko.com/en/all-cryptocurrencies")
        print(page.title())
        for _ in range (1,6):
           selector = '[data-action="click->more-content#loadMoreContent"][data-more-content-target="loadMoreButton"]'
           page.click(selector)
           sleep(0.5)
        kontent = page.content()
        browser.close()

    data = []
    soup = BeautifulSoup(kontent, 'html.parser')
    rows = soup.select('table tbody tr[data-view-component="true"]')
    print(f"Number of rows found: {len(rows)}")
    for row in soup.select('table tbody tr[data-view-component="true"]'):
        
        name_element = row.select_one('.tw-text-gray-700.tw-font-semibold')
        name = clean_text(name_element.text) if name_element else 'N/A'
        
        # Extract price
        price_element = row.select_one('[data-price-target="price"]')
        price = clean_text(price_element.text) if price_element else 'N/A'
        
        def get_change_and_direction(td_index):
            change_element = row.select_one(f'td:nth-of-type({td_index}) .gecko-down, td:nth-of-type({td_index}) .gecko-up')
            if change_element:
                change = clean_text(change_element.text)
                direction = 'down' if 'gecko-down' in change_element.get('class', []) else 'up'
            else:
                change = 'N/A'
                direction = 'N/A'
            return change, direction

        change_1h, direction_1h = get_change_and_direction(4)
        change_24h, direction_24h = get_change_and_direction(5)
        change_7d, direction_7d = get_change_and_direction(6)
        change_30d, direction_30d = get_change_and_direction(7)

        # Extract 24h volume and supplies
        volume_24h_element = row.select_one('td:nth-of-type(8)')
        volume_24h = clean_text(volume_24h_element.text) if volume_24h_element else 'N/A'
        
        circulating_supply_element = row.select_one('td:nth-of-type(9)')
        circulating_supply = clean_text(circulating_supply_element.text) if circulating_supply_element else 'N/A'
        
        total_supply_element = row.select_one('td:nth-of-type(10)')
        total_supply = clean_text(total_supply_element.text) if total_supply_element else 'N/A'
        

        data.append({
            'Name': name,
            'Price': price,
            'Change 1h': change_1h,
            'Direction 1h': direction_1h,
            'Change 24h': change_24h,
            'Direction 24h': direction_24h,
            'Change 7d': change_7d,
            'Direction 7d': direction_7d,
            'Change 30d': change_30d,
            'Direction 30d': direction_30d,
            '24h Volume': volume_24h,
            'Circulating Supply': circulating_supply,
            'Total Supply': total_supply
        })

    df = pd.DataFrame(data)
    if not df.empty:
        df.to_csv('Crypto Data.csv', index=False)
        print("CSV file has been written.")
    else:
        print("DataFrame is empty. No file written.")

 

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


def read_users():
    users = pd.read_csv("users.csv")
    return users.to_dict(orient="records")

def write_user(user):
    users = read_users()
    if user['username'] not in [u['username'] for u in users]:
        with open('users.csv', 'a', newline='') as csvfile:
            fieldnames = ['username', 'password']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if len(users) == 0:
                writer.writeheader()
            writer.writerow(user)
            flash('Account created successfully!', category='error')
    else:
        flash('Username already exists. Please choose a different username.', category='error')


