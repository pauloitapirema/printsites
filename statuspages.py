import json
from playwright.sync_api import sync_playwright


with open("sites.json") as sites:
    dados = json.load(sites)


for i in dados:
    with sync_playwright() as p:
        browser = p.webkit.launch()
        page = browser.new_page()
        page.wait_for_load_state
        response = page.goto(i['url'])
        print(i['url'], response.status)
        browser.close()