import gne
from selenium import webdriver
import time


driver=webdriver.Chrome()

driver.get('https://www.toutiao.com/a7010681185894466079/?log_from=5d70b2013f18d_1632322533013')
time.sleep(3)

extractor=gne.GeneralNewsExtractor()
html=driver.page_source
result=extractor.extract(html,host='https://p9.toutiaoimg.com',author_xpath='//span[@class="name"]/a/text()',publish_time_xpath=('//div[@class="article-meta"]/span[2]/text()'[0].split(' ')[0]))
print(result)
driver.close()
