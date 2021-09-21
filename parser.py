import bs4
import requests
import urllib.parse


class Parser:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
            'Accept-Language': 'ru'
        }

    def get_page_text(self, page: int = None):
        params = {
            'cd': 1,
            'radius': 0,
        }
        if page and page > 1:
            params['p'] = str(page)

        url = 'https://www.avito.ru/moskva/avtomobili/audi/q7-ASgBAgICAkTgtg3elyjitg3UrSg'
        result = self.session.get(url, params=params)
        return result.text

    def get_pages_amount(self):
        text = self.get_page_text()
        soup = bs4.BeautifulSoup(text, 'lxml')

        container = soup.select('a.pagination-page')
        last_button = container[-1]
        href = last_button.get('href')
        if not href:
            return 0

        r = urllib.parse.urlparse(href)
        params = urllib.parse.parse_qs(r.query)
        return int(params['p'][0])

    def parse_advert(self, item):
        url_block = item.select_one(
            'a.link-link-MbQDP.link-design-default-_nSbv.title-root-j7cja.iva-item-title-_qCwt.title-listRedesign-XHq38.title-root_maxHeight-SXHes')
        href = url_block.get('href')
        if href:
            url = 'https://www.avito.ru' + href
        else:
            url = None

        title_block = item.select_one(
            'h3.title-root-j7cja.iva-item-title-_qCwt.title-listRedesign-XHq38.title-root_maxHeight-SXHes.text-text-LurtD.text-size-s-BxGpL.text-bold-SinUO')
        title = title_block.string.strip()

        return {
            'title': title,
            'url': url,
        }

    def parse_page(self, page: int = None):
        text = self.get_page_text(page=page)
        soup = bs4.BeautifulSoup(text, 'lxml')

        adverts_wrapper = soup.select(
            'div.iva-item-root-Nj_hb.photo-slider-slider-_PvpN.iva-item-list-H_dpX.iva-item-redesign-nV4C4.iva-item-responsive-gIKjW.items-item-My3ih.items-listItem-Gd1jN.js-catalog-item-enum')
        for advert in adverts_wrapper:
            block = self.parse_advert(item=advert)
            print(block)

    def parse_adverts(self):
        limit = self.get_pages_amount()
        for i in range(1, limit + 1):
            self.parse_page(page=i)
