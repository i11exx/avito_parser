import requests


class Parser:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
            'Accept-Language': 'ru'
        }

    def get_page(self, page: int = None):
        params = {
            'cd': 1,
            'radius': 0,
        }
        if page and page > 1:
            # setattr(params, 'p', page)
            params['p'] = str(page)

        url = 'https://www.avito.ru/moskva/avtomobili/audi/q7-ASgBAgICAkTgtg3elyjitg3UrSg'
        result = self.session.get(url, params=params)
        return result.text
