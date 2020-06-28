from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/Users/song-yong-gyu/PythonWorkspace/start_selenium/chromedriver')
url = 'https://google.com'
driver.get(url)

driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys('python')
driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys(Keys.ENTER)
driver.find_elements_by_css_selector('.LC20lb.DKV0Md')[0].click()

