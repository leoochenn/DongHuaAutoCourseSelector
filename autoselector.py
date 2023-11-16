#   this is an auto course selector for Dung-Hua University
#   written by leoochenn 2023/11/15

#   please enter your username and password
username = "username"
password = "password"


#   first we need to import some helper
from selenium import webdriver  #   this is a tool to open web browser like firefox, chrome, and edge
from selenium.webdriver.common.by import By
import time #   waitting the page to log


#   this function opens up the browser, and go the target link
def open_browser():
    firefox_driver.get('https://sys.ndhu.edu.tw/aa/class/subjselect/')


#   this function uses username and password to log in the website.
def logIn():
    while True:
        try:
            if firefox_driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_ed_StudNo"]'):
                firefox_driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_ed_StudNo"]').send_keys(username)
            else:
                print("username ---not found")

            if firefox_driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_ed_pass"]'):
                firefox_driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_ed_pass"]').send_keys(password)
            else:
                print("password ---not found")

            if firefox_driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_BtnLoginNew"]'):
                firefox_driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_BtnLoginNew"]').click()
            else:
                print("login button ---not found")
            break

        except:
            print("login ---not found")


#   this function click the get course bottom, and listed all the course you want to choose.
def getCourse():
    while True:
        try:
            if firefox_driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_Button7"]'):
                firefox_driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_Button7"]').click()
                break
        except:
            print("get course bottom ---not found yet")


#   this function uses two while loop to go through all the wanted courses, and click each one of them.
def chooseCourse():
    while True:
        try:
            if firefox_driver.find_element(By.CSS_SELECTOR, "input[value*='加選']"):
                numElements = firefox_driver.find_elements(By.CSS_SELECTOR, "input[value*='加選']")
                while numElements != 0:
                    try:
                        if firefox_driver.find_element(By.CSS_SELECTOR, "input[value*='加選']"):
                            firefox_driver.find_element(By.CSS_SELECTOR, "input[value*='加選']").click()
                            numElements -= 1
                    except:
                        print("choose course loadding......")
        except:
            print("choose course ---not found")

if __name__ == '__main__':
    firefox_driver = webdriver.Firefox()    #   create the web driver.
    open_browser()  #   open browser and go to the target website.
    logIn() #   log in to the web site.
    getCourse() #   get the course you want.
    chooseCourse()  #   click all of them.
    firefox_driver.quit()   #   close the browser.
