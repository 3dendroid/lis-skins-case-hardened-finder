from seleniumbase import SB
import pyautogui as pag

with SB(headed=True,
        undetected=True,
        maximize=True,
        ad_block=True,
        skip_js_waits=True) as driver:

    driver.open('https://lis-skins.ru/market/csgo/five-seven-case-hardened-factory-new/')
    driver.click("//div[@class='item row market_item market_item_104821961']")
    driver.click("//div[@class='links']//a[@class='market-screenshot-link'][contains(text(),'Скриншот')]")
    driver.switch_to_newest_window()
    pag.screenshot('pattern', region=(0, 0, 300, 400))
    # continue
