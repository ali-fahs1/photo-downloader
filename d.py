import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests
import wget

os.environ['PATH'] += r"C:\seleniumdriver"
src=[]
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get("https://www.dubizzle.com.lb/ads/q-iphone/")
for x in range(1,10):
    m = driver.find_elements(By.XPATH,f'//*[@id="body-wrapper"]/div/header[2]/div/div/div/div[2]/div[2]/div[2]/div/div[2]/ul[1]/li[{x}]/article/div[1]/picture/img')
    for i in m:                        
        url=i.get_attribute('data-src')
        src.append(url)
        f=open(i.get_attribute('alt')+".jpg","wb")
        f.write(requests.get(url).content)

        
                
       


