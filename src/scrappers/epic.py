import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

from src.util.game_df import game_df


def epic_scrapper(driver):
  print("Extracting epic Games Library")
  games_df = game_df()
  lib_url = "https://www.epicgames.com/account/connections?lang=pt-BR&productname=egs"
  driver.get(lib_url)
  time.sleep(3)

  WebDriverWait(driver, 5).until(
      lambda d: d.find_element(
        By.CSS_SELECTOR, ".am-dlv5a8")
  )
  driver.implicitly_wait(60)
  driver.find_element(By.CSS_SELECTOR, "button.am-9ct68q").click()

  while True:
    try:
      WebDriverWait(driver, 5).until(
          lambda d: d.find_element(
            By.CSS_SELECTOR, ".am-1nbh9ao")
      )
      driver.find_element(By.CSS_SELECTOR, "button.am-1nbh9ao").click()
      driver.implicitly_wait(5)
    except:
      break
  time.sleep(1)

  list = driver.find_element(By.CLASS_NAME, "am-dlv5a8")
  soup_games = BeautifulSoup(list.get_attribute("innerHTML"), "html.parser")
  games = soup_games.find_all("div", class_="am-1chb4re")

  for game in games:
    new_row = pd.DataFrame(
        [
            {
                "name": game.find("h4").text,
                "image": game.find("img")["src"],
                "Link": "",
                "origin": "epic",
            }
        ]
    )
    games_df = pd.concat([games_df, new_row], ignore_index=True)
  return games_df
