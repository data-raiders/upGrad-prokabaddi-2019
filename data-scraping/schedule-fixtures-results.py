# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 20:18:12 2019

@author: bchirumamill
"""
from selenium import webdriver
#from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import csv
driver = webdriver.PhantomJS(executable_path="phantomjs.exe")
driver.get("https://www.prokabaddi.com/schedule-fixtures-results")


teamStatsDropDown = driver.find_elements_by_xpath("//select[contains(@class,'si-months-change')]/option")
dataList = [];

for i in reversed(range(len(teamStatsDropDown))):
   teamStats = teamStatsDropDown[i];
   print(teamStats.text)
   if teamStats.text == 'MONTH':
      continue
   teamStats.click()
   WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "si-fix-box-body")))
   scheduleList = driver.find_elements_by_class_name("si-fix-box-body")
   for schedule in scheduleList:
     #  WebDriverWait(driver, 1).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "fix-teamName")))
       teamNames = schedule.find_elements_by_class_name("fix-teamName")
       data = []
       data.append(teamNames[0].text.replace('\n', ' '))
       data.append(teamNames[1].text.replace('\n', ' '))
       result = schedule.find_elements_by_class_name("mat-resultStatus")
       if result[0].text:
           winTeam = result[0].text[0:result[0].text.find("Beat")]
           data.append( winTeam[0:winTeam.find("beat")])
       else:
           data.append("YTP")
      # matchStatus = schedule.find_elements_by_class_name("matStatus")
      # if matchStatus[0].text:
        #   data.append(matchStatus[0].text[result[0].text.find("- ")+2:])
       dataList.append(data)
       print("------------------------")

with open('schedule-fixtures-results.csv', 'w',  newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Team A', 'Team B','Win Team'])
    writer.writerows(dataList)

driver.close()