import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from src.util.game_df import game_df


def gog_scrapper(driver): 
  print("Extracting gog Games Library")
  games_df = game_df()
  lib_url = "https://www.gog.com/account"
  driver.get(lib_url)

  WebDriverWait(driver, 5).until(
      lambda d: d.find_element(By.CSS_SELECTOR, ".account__products--games")
  )
  driver.implicitly_wait(60)
  list = driver.find_element(By.CLASS_NAME, "account__products--games")

  soup_games = BeautifulSoup(list.get_attribute("innerHTML"), "html.parser")
  games = soup_games.find_all("div", class_="product-row-wrapper")

  for game in games:
    new_row = pd.DataFrame(
        [
            {
                "name": game.find("span", class_="product-title__text").text,
                "image": game.find("img", class_="product-row__img")["srcset"].split(" ,")[1].replace(" 2x", ""),
                "Link": "",
                "origin": "gog",
            }
        ]
    )
    games_df = pd.concat([games_df, new_row], ignore_index=True)
  return games_df