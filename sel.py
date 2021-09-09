from selenium.webdriver import Chrome

driver_path = "D:\chromedriver\chromedriver.exe"

driver = Chrome(executable_path=driver_path)
#driver = Chrome(driver_path)
driver.get('https://www.lazada.com.ph/shop-laptops/')
driver.implicitly_wait(60)
link_elements = driver.find_elements_by_css_selector('div._8JShU > a')
links = []
for link_el in link_elements:
    href = link_el.get_attribute("href")
    print(href)
    links.append(href)

print('Finish scraping')
driver.quit()
