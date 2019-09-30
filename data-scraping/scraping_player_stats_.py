# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 09:32:40 2019

@author: bchirumamill
"""

from selenium import webdriver
#from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import csv
driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://www.prokabaddi.com/")
action = ActionChains(driver)

teamList = driver.find_elements_by_xpath("//li[@data-id='teams']/div/a")
print(len(teamList))
plyer_raids_df = [];
plyer_tackles_df = [];

for i in range(len(teamList)):
   WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//li[@data-id='teams']")))
   teamMenu = driver.find_elements_by_xpath("//li[@data-id='teams']")
   teamMenu[0].click()
   team = driver.find_elements_by_xpath("//li[@data-id='teams']/div/a")[i];
   team.click()
   WebDriverWait(driver, 1).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'more-btn')))
   viewFullTeams = driver.find_elements_by_class_name("more-btn")
   for viewFullTeam in viewFullTeams:
      
       if'VIEW FULL SQUAD' == viewFullTeam.text:
           viewFullTeam.click()
           WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'si-plyrImg')))
           ply_profiles = driver.find_elements_by_class_name("si-plyrImg")
           
           for ply in range(len(ply_profiles)):
               WebDriverWait(driver, 2).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'si-plyrImg')))
               driver.find_elements_by_class_name("si-plyrImg")[ply].click()
               WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'si-name')))
               ply_name = driver.find_elements_by_class_name("si-name")
               try:
                   driver.find_elements_by_xpath("//div[@data-tabtype='stats']")[0].click()
               except Exception:
                   print("expection")
                   
              
               raids_info = [];
               tackles_info = [];
               print(ply_name[0].text)
               ply_stats_info =  driver.find_elements_by_xpath("//div[contains(@class,'si-data-section')]/div[@class='si-tbl-wraper']")
               ply_raid_inf = ply_stats_info[1].find_elements_by_class_name("si-tbl-data")[1].find_elements_by_class_name("si-data-block")
               
               raids_info.append( ply_name[0].text);
               tackles_info.append(ply_name[0].text);
               
               raids_info.append(ply_raid_inf[0].text)
               raids_info.append(ply_raid_inf[4].text)
               raids_info.append(ply_raid_inf[1].text)
               
            
               ply_tackles_inf = ply_stats_info[2].find_elements_by_class_name("si-tbl-data")[1].find_elements_by_class_name("si-data-block")
               tackles_info.append(ply_tackles_inf[4].text)
               tackles_info.append(ply_tackles_inf[2].text)
               tackles_info.append(ply_tackles_inf[5].text)
               
               plyer_raids_df.append(raids_info)
               plyer_tackles_df.append(tackles_info)
               
               driver.back()
           
           
           break;
   
with open('player_raids.csv', 'w',  newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'total','scored','avg'])
    writer.writerows(plyer_raids_df)
    
with open('player_tackles.csv', 'w',  newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'total','scored','avg'])
    writer.writerows(plyer_tackles_df)
driver.close()