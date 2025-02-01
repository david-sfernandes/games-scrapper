from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

from src.scrappers.epic import epic_scrapper
from src.scrappers.gog import gog_scrapper
from src.scrappers.steam import steam_scrapper

user_data_dir = r"--user-data-dir=C:\Users\david\AppData\Local\Google\Chrome\User Data"
chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument(user_data_dir)
chrome_options.add_argument("--profile-directory=Default")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

epic_df = epic_scrapper(driver)
steam_df = steam_scrapper(driver)
gog_df = gog_scrapper(driver)

driver.quit()

games_df = pd.concat([epic_df, steam_df, gog_df], ignore_index=True)
games_df.sort_values(by="name", inplace=True)
games_df.to_json("static/games.json", index=False, orient="records", indent=4)
