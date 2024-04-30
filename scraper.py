from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"

# Webdriver
browser = webdriver.Chrome()
browser.get(START_URL)
time.sleep(100)
planets_data = []

# Define Exoplanet Data Scrapping Method
def scrape() :
    print("Scraping...")
    for i in range(0,10) :
        print(f'scraping page{i+1}')
        sop = BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in sop.find_all('ul',attrs={'class','exoplanets'}) :
            li_tags =   ul_tag.find_all("li")
            temp_list = []
            for index,li_tag in enumerate(li_tags):
                if index == 0 :
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            hyperlink_li_tag = li_tags[0]
            temp_list.append("https://exoplanets.nasa.gov"+hyperlink_li_tag.find_all("a",href = True)[0]["href"])
            planets_data.append(temp_list)
        browser.find_element(by = By.XPATH,value = '').click()
        



        
# Calling Method 
scrape()   

# Define Header
headers = ['name','light_years_from_earth','planet_mass','stellar_magnitude','discovery_date']

# Define pandas DataFrame   
planet_df1 = pd.DataFrame(planets_data,column = headers)

# Convert to CSV
planet_df1.to_csv('scrapped_data.csv',index =True,index_label = "id")
