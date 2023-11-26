import requests


def convert_percentage_to_scale(percentage_value):
    scaled_value = (percentage_value / 100) * 5
    return round(scaled_value, 2)


def getHTMLDocument(url, params):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64)"
            "AppleWebKit/537.36 (KHTML, like Gecko)"
            "Chrome/44.0.2403.157 Safari/537.36"
        ),
        "Accept-Language": "en-US, en;q=0.5",
    }
    response = requests.get(url, params=params, headers=headers)

    return response.status_code, response.text
