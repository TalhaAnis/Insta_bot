from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class instaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('./chromedriver')
        self.login()
        print("hi")

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_element_by_name('password').send_keys(Keys.RETURN)
    def follow_people(self, tags):
        for tag in tags:
            self.driver.get('https://www.instagram.com/explore/tags/{}/'.format(tag))
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]').click()
                                               
            for i in range(1000):
                try:
                    time.sleep(3)
                    follow_button = self.driver.find_element_by_class_name("oW_lN")
                    if not follow_button.text == 'Following':
                        follow_button.click()
                        time.sleep(2)
                    time.sleep(0.5)
                    right_button = self.driver.find_element_by_class_name("HBoOv")
                    if right_button:
                        right_button.click()
                    time.sleep(3)
                except Exception as ex:
                    print(ex)

if __name__ == '__main__':
    username = "" # add your username
    password = "" # add your password
    tags = ["cars", "technology", "fashion", "mobile"] # add tags here which you need to follow 
    igbot = instaBot(username, password)
    time.sleep(4)
    igbot.follow_people(tags)

