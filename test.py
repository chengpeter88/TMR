# import streamlit as st
import pandas as pd 
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from bs4 import BeautifulSoup as Soup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import streamlit as st

# 開啟chromedriver  
driver= webdriver.Chrome('Chromedriver')
# chrome_options = Options()
# Options.chrome_excutbale_path = '/usr/bin/chromewebdriver'
# driver=webdriver.Chrome(chrome_options=chrome_options)
# url ='https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=TW&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped&media_type=all'
# driver=.get(url)