from selenium import webdriver
#from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import csv
driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://www.prokabaddi.com/stats/49-96-total-points-scored-statistics")


teamStatsDropDown = driver.find_elements_by_xpath("//select[@id='si_dropdown']/option")
dataList = [];

for i in range(len(teamStatsDropDown)):
   teamStats = teamStatsDropDown[i];
   print(teamStats.text)
   teamStats.click()
   WebDriverWait(driver, 1).until(EC.visibility_of_all_elements_located((By.XPATH, "//select[@id='season_dropdown']/option")))
   seasonDropDown = driver.find_elements_by_xpath("//select[@id='season_dropdown']/option")
   for season in seasonDropDown:
       print(season.text)
       if('SEASON 7' != season.text):
           continue;
       season.click()
       WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'si-stats-partial-data')]/div[contains(@class,'sipk-lb-detailItem')]")))
       lists = driver.find_elements_by_xpath("//div[contains(@class,'si-stats-partial-data')]/div[contains(@class,'sipk-lb-detailItem')]")
       dataList = [];
       for elem in lists:
     
          # WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'sipk-lb-detailBlock')))
           spanElements = elem.find_elements_by_class_name('sipk-lb-detailBlock')
           data = []
           for span in spanElements:
               if span.text and span.text.strip():
                   data.append(span.text)
           dataList.append( data)
           driver.implicitly_wait(100)
       with open(teamStats.text+"_"+season.text+'.csv', 'w',  newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['rank', 'Name','Matches played','points'])
        writer.writerows(dataList)

driver.close()