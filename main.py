import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import re
import json 
import urllib.parse

caps = DesiredCapabilities.CHROME

caps['goog:loggingPrefs'] = {'performance': 'ALL'}

chrome_options = webdriver.ChromeOptions()
chrome_options.set_capability(
                        "goog:loggingPrefs", {"performance": "ALL", "browser": "ALL"}
                    )
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.northerntrust.com/united-states/home')
elements = driver.

sleep(10)

def process_browser_log_entry(entry):
    response = json.loads(entry['message'])['message']
    return response

browser_log = driver.get_log('performance') 
events = [process_browser_log_entry(entry) for entry in browser_log]
events = [event for event in events if 'Network.response' in event['method']]

url_list = [collect_event["params"]["response"]["url"] for collect_event in events if "response" in collect_event["params"]]


ga_urls = [url for url in url_list if re.search( r'\bcollect\b', url)]

gtm_calls = [urllib.parse.parse_qs(gtm_call) for gtm_call in ga_urls ]


with open('result.json', 'w') as fp:
    json.dump(gtm_calls, fp)

print(gtm_calls)

print(elements)
