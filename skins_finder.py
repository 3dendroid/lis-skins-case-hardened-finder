from seleniumbase import SB
import requests

file_name = "pattern.png.png"

with SB(headed=True,
        undetected=True,
        maximize=True,
        ad_block=True,
        headless=False,
        skip_js_waits=True) as driver:
    driver.open('https://lis-skins.ru/market/csgo/five-seven-case-hardened-factory-new/')
    driver.click("(//div[@class='cell'])[5]")
    driver.click("//div[@class='links']//a[@class='market-screenshot-link'][contains(text(),'Скриншот')]")
    driver.switch_to_tab(0)
    url = driver.get_current_url()
    response = requests.get(url)
    with open(file_name, 'wb') as file:
        file.write(response.content)

