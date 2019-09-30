from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
driver = webdriver.PhantomJS(executable_path="phantomjs.exe")
driver.get("https://www.prokabaddi.com/standings")
lists = driver.find_elements_by_xpath("//div[contains(@class,'sipk-standing-dataRow')]")
dataList = [];

for elem in lists:
    spanElements = elem.find_elements_by_class_name('sipk-table-col')
    data = []
    for span in spanElements:
        if span.text and span.text.strip():
            data.append(span.text)
    if len(data) != 0:
     dataList.append( data)
    
with open('standings.csv', 'w',  newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['rank', 'team','points','w','l','t','Pts'])
    writer.writerows(dataList)
driver.close()