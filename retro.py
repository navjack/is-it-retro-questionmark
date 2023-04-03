import requests
import time
from datetime import datetime

api_key = "YOUR API KEY"
endpoint = "https://api.mobygames.com/v1/"
rate = 1


def search_game(title):
    url = f"{endpoint}games"
    params = {"api_key": api_key, "title": title, "format": "normal"}
    response = requests.get(url, params=params)
    data = response.json()
    oldest_game = None
    oldest_date = None
    if 'games' in data:
        for game in data['games']:
            if 'platforms' in game:
                for platform in game['platforms']:
                    if 'first_release_date' in platform:
                        release_date = platform['first_release_date']
                        if oldest_date is None or release_date < oldest_date:
                            oldest_game = game
                            oldest_date = release_date
    if oldest_game is not None:
        print(f"Title: {oldest_game['title']}")
        print(f"First release year: {oldest_date[:4]}")
        return int(oldest_date[:4])
    else:
        print("No game found with a first release date")
        return None
    time.sleep(rate)

title1 = input('Enter the title of the first game: ')
year1 = search_game(title1)
if year1 is not None:
    today = datetime.now()
    delta_years = today.year - year1
    print(f"Years since first release: {delta_years}")

title2 = input('Enter the title of the second game: ')
year2 = search_game(title2)
if year2 is not None and year1 is not None:
    delta_years = year2 - year1
    print(f"Years between first releases: {delta_years}")
