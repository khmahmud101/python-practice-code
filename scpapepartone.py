import re
import requests
import sys
import logging
def get_category_list(content):
    return category_pat.findall(content)

def get_page_content(url):
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        logging.error(e)

    if response.ok:
        return response.text
    logging.error("can not get content from url:"+url)
    return None

