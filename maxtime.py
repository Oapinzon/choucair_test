from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\opinzon\Documents\OMAR\vscode\webdrivers\78.0.3904.11\chromedriver")

driver.get("http://operacion.choucairtesting.com/MaxtimeChc/Login.aspx?ReturnUrl=%2fMaxtimeChc")

omar = driver.find_element_by_xpath("//*[@id='Logon_v0_MainLayoutEdit_xaf_l30_xaf_dviUserName_Edit_I']")
omar.send_keys("opinzona")
time.sleep(5)

omar = driver.find_element_by_xpath("//*[@id='Logon_v0_MainLayoutEdit_xaf_l35_xaf_dviPassword_Edit_I']")
omar.send_keys("choumar20*")
omar.send_keys(Keys.ENTER)
time.sleep(5)

omar = driver.find_element_by_xpath("//*[@id='Vertical_v1_LE_v2_cell0_0_xaf_Fecha_View']")
omar.click()
time.sleep(5)

omar = driver.find_element_by_xpath("//*[@id='Vertical_v5_MainLayoutView_xaf_l103_xaf_dviReporteDetallado_ToolBar_Menu_DXI0_T']/a")
omar.click()
time.sleep(5)


omar = driver.find_element_by_xpath("//*[@id='Vertical_v8_MainLayoutEdit_xaf_l128_xaf_dviProyecto_Edit_Find_BImg']")
omar.click()
time.sleep(5)



"""
driver.close()
"""

