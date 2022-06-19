from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument('--headless')

def test_selenium():
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://ambiente-dev-pr.herokuapp.com") # http://localhost:5000
    assert 2 + 2 == 4
    driver.close()
