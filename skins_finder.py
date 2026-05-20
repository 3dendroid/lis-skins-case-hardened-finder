import os
import time

from seleniumbase import SB

with (SB (headed=True,
          headless=False,
          incognito=True,
          undetected=True,
          maximize=True,
          ad_block=True,
          skip_js_waits=True)
      as driver):
    driver.open ('https://lis-skins.ru/market/csgo/five-seven-case-hardened-factory-new/')

    # elements = driver.find_elements (".item.row")
    time.sleep (2)
    print ('CLICK TO ITEM')
    driver.click ('.item.row')

    time.sleep (2)
    print ('CLICK TO SCREENSHOT BUTTON')
    driver.click ("div[class='links'] a[class='market-screenshot-link']")

    time.sleep (2)
    print ('MAKE A SCREENSHOT')
    time.sleep (2)
    folder = r'C:\Users\SUPERDEN\PycharmProjects\lis-skins-case-hardened-finder\screenshots'
    if not os.path.exists (folder):
        os.makedirs (folder)
    screenshot_filename = os.path.join (folder, time.strftime ('%d_%m_%Y_%H_%M_%S') + '_screenshot.png')
    driver.save_screenshot (screenshot_filename)
    print (f'SCREENSHOT SAVED')

    time.sleep (2)
    print ('SWITCH TO PREVIOUS TAB')
    driver.switch_to_tab (0)

    time.sleep (2)
    print ('CLOSE POPUP WINDOW')
    driver.click ('div[class="popup-close"]')
    print ('FINISHED')
# DELETE THIS AFTER FIXING GIT PROBLEM

# for element in elements:
#     element.click ()
#     driver.click ("div[class='links'] a[class='market-screenshot-link']")
#     driver.switch_to_tab (0)
#     url = driver.get_current_url ()
#     response = requests.get (url)
#     driver.save_screenshot (f"screenshots/pattern_{datetime.now}.png")
#     with open (f"screenshots/pattern_{datetime.now}.png", 'wb') as file:
#         file.write (response.content)
