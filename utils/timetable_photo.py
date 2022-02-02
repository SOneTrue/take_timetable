import asyncio
import requests
from bs4 import BeautifulSoup
from lxml import etree
from loguru import logger
URL = "https://btgp.ru/zameny-v-raspisanii.html"

HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})


async def check_updates():
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "html.parser")
    web_page = etree.HTML(str(soup))
    table_link = web_page.xpath('//div[contains(@class, "item column-1")]/p[last()]//a/@href')[0]
    logger.info(table_link)
    return table_link
