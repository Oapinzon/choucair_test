from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome(executable_path=r"C:\driver_chrome\chromedriver.exe")
driver.get("https://www.choucairtesting.com/empleos-2/")

driver.execute_script("window.scrollTo(0,2070)")
time.sleep(3)
driver.close()