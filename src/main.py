import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def first_exercise():
    a  = 0 
    list = []
    while a < 15:
        a+=1
        list.append(a)
    print(list)

def secundary_exercise():
    search_google ='body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div.SDkEP > div.a4bIc > input'
    select_url ='#rso > div:nth-child(18) > div > div > div.yuRUbf > a > h3'
    data_link = ''
    url ='https://www.google.com'
    word ='musica moderna'
    #Chromedriver
    #abrir navegador 
    ruta_chromedriver = 'C:\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=ruta_chromedriver)
    driver.maximize_window()
    driver.get(url)
    
    driver.find_element_by_css_selector(search_google).click()
    driver.find_element_by_css_selector(search_google).send_keys(word)
    driver.find_element_by_css_selector(search_google).send_keys(Keys.ENTER)
    driver.find_element_by_css_selector(select_url).click()
    data_link = driver.page_source
    print(data_link)
    
def third_exercise(url):
    username='yefersoncasti@gmail.com'
    passwd='Skills2020'

    #selectores :
    btn_select_sing_in = 'body > nav > div > a.nav__button-secondary'
    select_user = '#username'
    select_paswd ='#password'
    btn_login = '#organic-div > form > div.login__form_action_container > button'

    #abrir navegador 
    ruta_chromedriver = 'C:\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=ruta_chromedriver)
    driver.maximize_window()
    driver.get(url)

    driver.find_element_by_css_selector(btn_select_sing_in).click()
    #login 
    time.sleep(5)
    driver.find_element_by_css_selector(select_user).send_keys(username)
    driver.find_element_by_css_selector(select_paswd).send_keys(passwd)
    driver.find_element_by_css_selector(btn_login).click()

    time.sleep(5)
    #cerrar
    driver.quit()

def main():
    first_exercise()
    # time.sleep(10)
    secundary_exercise()
    # time.sleep(20)
    third_exercise('https://www.linkedin.com')

if __name__ == '__main__':
    main()