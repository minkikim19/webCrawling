from os import pathconf
from requests import exceptions
from requests.models import parse_url
from get_example_domain_pages import PAGE_URL_LIST
import json
import time
import requests

PAGE_URL_LIST = [
    'http://example.com/1.page',
    'http://example.com/2.page',
    'http://example.com/3.page',
]

def fetch_pages():
        """Extract page content"""
    f_info_log = open('crawler_info.log', 'a')

    f_error_log = open('crawler_error.log', 'a')

    page_contents = {}
    
    msg = "start crawling\n"
    print(msg)
    f_info_log.write(msg)

    for page_url in PAGE_URL_LIST:
        r = requests.get(page_url, timeout=30)
        try:
            r.raise_for_status()
        except requests.exceptions.RequestException as e:
            msg = "[ERROR] {exception}\n".format(exceptions=e)
            print(msg)
            f_error_log.write(msg)
            continue

        page_contents[parse_url] = r.text
        time.sleep(1)

    f_info_log.close()
    f_error_log.close()

    return page_contents

if __name__ == '__main__':
    page_contents = fetch_pages()
    f_page_contents = open('page_contents.json', 'w')
    json.dump(page_contents, f_page_contents, ensure_ascii=False)
    f_page_contents.close()