import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from src.util.game_df import game_df
import time


def steam_scrapper(driver):
  print("Extracting steam Games Library")
  games_df = game_df()
  lib_url = "https://steamcommunity.com/profiles/76561198859880953/games/?tab=all"
  driver.get(lib_url)

  WebDriverWait(driver, 5).until(
      lambda d: d.find_element(By.CSS_SELECTOR, "._3tY9vKLCmyG2H2Q4rUJpkr ._2-pQFn1G7dZ7667rrakcU3 picture")
  )
  driver.execute_script("window.scrollTo({ left:0, top: document.body.scrollHeight/2, behavior: 'smooth' });")
  driver.execute_script("window.scrollTo({ left:0, top: document.body.scrollHeight, behavior: 'smooth' });")
  time.sleep(5)
  list = driver.find_element(By.CLASS_NAME, "_3tY9vKLCmyG2H2Q4rUJpkr")

  soup_games = BeautifulSoup(list.get_attribute("innerHTML"), "html.parser")
  games = soup_games.find_all("div", class_="_2-pQFn1G7dZ7667rrakcU3")

  for game in games:
    new_row = pd.DataFrame(
        [
            {
                "name": game.find("a", class_="_22awlPiAoaZjQMqxJhp-KP").text,
                "image": game.select("._1CHM8-0EM9IeDAZ47-cYit")[0].find("img")[
                    "src"
                ],
                "Link": game.find("a", class_="_22awlPiAoaZjQMqxJhp-KP")["href"],
                "origin": "steam",
            }
        ]
    )
    games_df = pd.concat([games_df, new_row], ignore_index=True)
  print(len(games_df), "games found")
  return games_df
