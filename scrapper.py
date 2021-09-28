from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import csv

file = open('/home/bilal/Documents/ray.csv', 'r')
csv_save = open('scrapped_final.csv', 'w')

csv_reader = csv.reader(file)
csv_writer = csv.writer(csv_save)
csv_writer.writerow(['Title', 'URL', 'Location'])

links = []

for rows in csv_reader:
    linktext = ''.join(rows)
    links.append(linktext)

for link in links:
    driver = webdriver.Chrome('/home/bilal/Documents/chromedriver')
    driver.get(link)
    soup = driver.page_source
    codebase = BeautifulSoup(soup, 'lxml')
    jobtitle = codebase.title.text
    joblocation = codebase.find('span', class_='sub-nav-cta__meta-text')
    joblink = codebase.find("meta", property="og:url")
    if jobtitle and joblink and joblocation:
        csv_writer.writerow([jobtitle, joblink["content"], joblocation.text])
    driver.close()
file.close()
csv_save.close()
