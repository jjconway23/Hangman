import requests


def get_words():
    """
    Gets words from api, returns list of 5 words 
    """
    response = requests.get("https://random-word-api.herokuapp.com/word?number=5&length=7")
    words = response.json()
    return words

