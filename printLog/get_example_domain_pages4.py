import json
import time

import requests
from requests import exceptions

PAGE_URL_LIST = [
    'http://example.com/1.html',
    'http://example.com/2.html',
    'http://example.com/3.html',
]

def fetch_pages():
    """Extract page content"""

    with open('craler_info.log', 'a') as f_info_log, \
        open('crawler_error.log', 'a') as f_error_log:

        page_contents = {}
        msg = "[INFO] start crawl\n"
        print(msg)
        f_info_log.write(msg)

        for page_url in PAGE_URL_LIST:
            try:
                r=requests.get(page_url, timeout=30)
                r.raise_for_status()
            except requests.exceptions.RequestException as e:
                msg="[ERROR] {exception}\n".format(Exception=e)
                print(msg)
                f_error_log.write(msg)
                continue

            page_contents[page_url] =r.text
            time.sleep(1)

        return page_contents

if __name__ == '__main__':
    page_contents = fetch_pages()
    with open('page_contents.json', 'w') as f_page_contents:
        json.dump(page_contents, f_page_contents, ensure_ascii=False)