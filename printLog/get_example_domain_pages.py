import time
import requests

PAGE_URL_LIST=[
    'http://example.com/1.page',
    'http://example.com/2.page',
    'http://example.com/3.page',
]

for page_url in PAGE_URL_LIST:
    res = requests.get(page_url, timeout=30)
    print(
        "page url: " + page_url + ", " + \
        "http status: " + str(res.status_code) + ", " + \
        "processing time: " + str(res.elapsed.total_seconds())      
    )

    time.sleep(1)