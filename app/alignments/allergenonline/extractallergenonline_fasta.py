# -*- coding: utf-8 -*-
"""ExtractALLERGENONLINE_FASTA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HFPyZPTVrEwp6romMyAP-JYc5vypzl5J
"""

import pandas as pd
from bs4 import BeautifulSoup
import requests
from csv import writer
!pip install selenium
!apt-get update # to update ubuntu to correctly run apt install
!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin
import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
from selenium import webdriver
from selenium.webdriver.common.by import Bychrome_options = webdriver.ChromeOptions()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Chrome('chromedriver',options=chrome_options)

df = pd.read_csv("allergen_online.csv")
df.head()

urls = df["sequences-href"]
urls[:5]

sequences = []

for i,u in enumerate(urls):
  print("processing url", i, "/", len(urls)-1)
  url = u+"?report=fasta"
  wd.get(url)
  delay = 10 # seconds
  try:
      fasta = WebDriverWait(wd, delay).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div > pre"))).text
      if fasta != "" and fasta != None:
        sequences.append(fasta)
  except TimeoutException:
      print("Loading took too much time!")

fasta_all_str = ""
for i,s in enumerate(sequences):
  if i<len(sequences):
    fasta_all_str += s + "\n"

if fasta_all_str != "":
    with open('result.fasta', 'w') as f:
      f.write(fasta_all_str)

fasta_all_str

wd.implicitly_wait(10)

# page = requests.get(url)
# print(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# fasta_div = soup.find("div", {"id": "c"})
# # fasta = fasta_div.findChildren("pre" , recursive=False)
# fasta_div

fasta_div = wd.find_element(by=By.ID, value="viewercontent1") 
fasta_div.find_elements()