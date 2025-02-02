# GameMerge | Game library scrapper

A way to organize your game collection. Consolidate all your libraries easily and automatically. Extract your game library from Steam, GOG and Epic Games.

## About

GameMerge is an automation tool that uses your access to app stores to collect and organize information about your game collection. You need to have a browser logged into your accounts to perform the extraction.

## Configuration

Create a `.env` file and add the path to your chrome user data folder.

Example:
```bash
PATH_CHROME_PROFILE="C:\Users\<YOUR_USER_FOLDER>\AppData\Local\Google\Chrome\User Data"
```

## Run the application

First mount the enviroment:
```bash
python -m venv .venv
```

Install the dependecies:
```bash
pip install -r requirements.txt
```

Run the automation:
```bash
.\.venv\Scripts\Activate.ps1

.\index.py
```