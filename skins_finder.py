from seleniumbase import SB
import requests

file_name = "images/pattern.png"

with SB(headed=True,
        undetected=True,
        maximize=True,
        ad_block=True,
        headless=False,
        skip_js_waits=True) as driver:

    driver.open('https://lis-skins.ru/market/csgo/five-seven-case-hardened-factory-new/')

    elements = driver.find_elements(".item.row.market_item")

    for index, element in enumerate(elements):
        element.click()
        driver.click("//div[@class='links']//a[@class='market-screenshot-link'][contains(text(),'Скриншот')]")
        driver.switch_to_tab(0)
        url = driver.get_current_url()
        response = requests.get(url)

        with open(f"images/pattern_{index}.png", 'wb') as file:
            file.write(response.content)

        driver.go_back()
