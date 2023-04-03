import requests
import time

api_key = "YOUR API KEY"
endpoint = "https://api.mobygames.com/v1/"
rate = 0.1


def search_game(title):
    url = f"{endpoint}games"
    params = {"api_key": api_key, "title": title, "format": "normal"}
    response = requests.get(url, params=params)
    data = response.json()
    oldest_game = None
    oldest_date = None
    if "games" in data:
        for game in data["games"]:
            if "platforms" in game:
                for platform in game["platforms"]:
                    if "first_release_date" in platform:
                        release_date = platform["first_release_date"]
                        if oldest_date is None or release_date < oldest_date:
                            oldest_game = game
                            oldest_date = release_date
    if oldest_game is not None:
        print(f"Title: {oldest_game['title']}")
        print(f"First release date: {oldest_date}")
    else:
        print("No game found with a first release date")
    time.sleep(rate)


title1 = input("Enter the title of the first game: ")
search_game(title1)

title2 = input("Enter the title of the second game: ")
search_game(title2)
