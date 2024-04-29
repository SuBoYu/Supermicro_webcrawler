from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import urllib.request
import re
from urllib.parse import urlparse, urlunparse
from collections import deque
import os


webdriver_service = Service("./chromedriver-mac-arm64/chromedriver")


options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
})

driver = webdriver.Chrome(service=webdriver_service, options=options)
visited_urls = set()
file_links = set()

def remove_query_param(url):
    parsed_url = urlparse(url)
    # remove ?mlg=0, query parameter
    clean_url = urlunparse(parsed_url._replace(query=''))
    return clean_url

def crawler(url):
    save_folder = "file"
    driver.get(url)
    queue = deque()
    queue.append(url)

    while queue:
        cur_url = queue.popleft()
        if cur_url in visited_urls:
            continue
        visited_urls.add(cur_url)
        print("link: ", cur_url)
        try:
            driver.get(cur_url)
        except:
            continue

        try:
            elements = driver.find_elements(By.TAG_NAME, 'a')
            for element in elements:
                href = element.get_attribute('href')
                if href and href.startswith('https://www.supermicro.com/'):
                    if (re.search(r'\.pdf', href) or re.search(r'\.txt', href)):
                        href = remove_query_param(href)
                        if href not in file_links:
                            file_links.add(href)
                            print("file: ", href)
                            filename = href.split('/')[-1]
                            save_path = f"{save_folder}/{filename}"
                            urllib.request.urlretrieve(href, save_path)
                    else:
                        queue.append(href)
        except:
            continue

    time.sleep(5)

try:
    crawler('https://www.supermicro.com/')

finally:
    driver.quit()

