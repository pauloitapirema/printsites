import json
from playwright.sync_api import sync_playwright


with open("sites.json") as sites:
    dados = json.load(sites)


for i in dados:
    with sync_playwright() as p:
        browser = p.webkit.launch()
        page = browser.new_page()
        page.goto(i['url'])
        page.screenshot(path=i['titulo']+".png")
        browser.close()