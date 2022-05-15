import requests,json

quote_url = 'http://quotes.stormconsultancy.co.uk/random.json'

def get_data():
    random_quote = requests.get(quote_url)
    quote = json.loads(random_quote.content)
    return quote