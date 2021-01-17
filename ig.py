from selenium import webdriver
from time import sleep

# yksinkertainen ohjelma jolla kirjaudutaan twitteriin ja tykätään postista
# käyttää seleniumia

class TwitterBotti:
    def __init__(self, sahkoposti, pw):
        self.bot = webdriver.Chrome()
        self.sahkoposti = sahkoposti
        self.pw = pw
    

# sisäänkirjautuminen   
    def login(self):
        botti = self.bot
        botti.get("https://twitter.com/login")
        sleep(3)
        botti.find_element_by_xpath("//input[@name=\"session[username_or_email]\"]").send_keys(self.sahkoposti)
        botti.find_element_by_xpath("//input[@name=\"session[password]\"]").send_keys(self.pw)
        botti.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div').click()
        sleep(3)
# tykkääminen
    def likee_postista(self):
        likeeja = self.bot
        likeeja.get("https://twitter.com/explore")
        sleep(3)
        likeeja.find_element_by_xpath("//a[contains(text(), 'true')]").click
        sleep(3)

cd = TwitterBotti('davedoubledaves@gmail.com', 'TheQuickDogJumps4')
cd.login()
cd.likee_postista()