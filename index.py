from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

from src.scrappers.epic import epic_scrapper
from src.scrappers.gog import gog_scrapper
from src.scrappers.steam import steam_scrapper
from src.util.build_html import build_html

user_data_dir = r"--user-data-dir=C:\Users\david\AppData\Local\Google\Chrome\User Data"
options = Options()
# options.add_argument("--headless")
options.add_argument(user_data_dir)
options.add_argument("--profile-directory=Default")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

epic_df = epic_scrapper(driver)
steam_df = steam_scrapper(driver)
gog_df = gog_scrapper(driver)

driver.quit()

games_df = pd.concat([epic_df, steam_df, gog_df], ignore_index=True)
games_df.sort_values(by="name", inplace=True)
games_df.to_json("static/games.json", index=False, orient="records", indent=4)

build_html(games_df)