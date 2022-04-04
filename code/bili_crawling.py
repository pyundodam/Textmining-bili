from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
chrome_options.add_argument('headless')

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=chrome_options)

driver.implicitly_wait(5)

driver.get("https://search.bilibili.com/all?keyword=%E7%BF%BB%E5%94%B1&from_source=webtop_search&spm_id_from=333.851")
driver.maximize_window()

data = []

title = driver.find_elements(By.CLASS_NAME,"bili-video-card__info--tit")
author = driver.find_elements(By.CLASS_NAME,"bili-video-card__info--author")
date = driver.find_elements(By.CLASS_NAME,"bili-video-card__info--date")

for title, author, date in zip(title, author, date):
        data.append([title.text, author.text, date.text])


baseurl = "https://search.bilibili.com/all?keyword=%E7%BF%BB%E5%94%B1&from_source=webtop_search&spm_id_from=333.851&page=2&o={}"
pagenum = 36

for page in range (10):
    url = baseurl.format(pagenum)
    driver.get(url)
    driver.maximize_window()
    title = driver.find_elements(By.CLASS_NAME,"bili-video-card__info--tit")
    author = driver.find_elements(By.CLASS_NAME,"bili-video-card__info--author")
    date = driver.find_elements(By.CLASS_NAME,"bili-video-card__info--date")
    time.sleep(5)
    pagenum = pagenum+36
    for title, author, date in zip(title, author, date):
        data.append([title.text, author.text, date.text])

df = pd.DataFrame(data)
# print(df)
df.to_excel('bili_Keyword_翻唱.xlsx')
# print("finished")
driver.close()

