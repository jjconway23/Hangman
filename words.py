import requests
def getWords():
    """
    Gets words from api, returns list of words printed to the console
    """
    response = requests.get("https://random-word-api.herokuapp.com/word?number=5&length=7")
    words = response.json()
    return words

