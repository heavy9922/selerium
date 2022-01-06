from selenium import webdriver
import time


def first_exercise():
    a  = 0 
    list = []
    while a < 15:
        a+=1
        list.append(a)
    print(list)

def secundary_exercise(url):
    #Chromedriver
    ruta_chromedriver = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
    driver = webdriver.Chrome(executable_path=ruta_chromedriver)

    driver.maximize_window()
    driver.get(url)
    # time.sleep(5)
    # driver.find_element_by_class_name('vbplogin').click()
    # driver.find_element_by_name('log').send_keys('hola')
    # time.sleep(10)
    # driver.find_element_by_name('pwd').send_keys('secreto')
    time.sleep(10)

def main():
    first_exercise()
    secundary_exercise('https://www.python.org/')

if __name__ == '__main__':
    main()