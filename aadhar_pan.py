from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import pandas as pd

def check_adhar_pan(aadhar, pan):
    service = Service(executable_path='chromedriver.exe')
    options = Options()
    options.add_argument('--disable-logging')
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://eportal.incometax.gov.in/iec/foservices/#/pre-login/link-aadhaar-status')

    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, 'mat-input-0')))

        pan_input = driver.find_element(By.ID, 'mat-input-0')
        pan_input.send_keys(pan)

        aadhar_input = driver.find_element(By.ID, 'mat-input-1')
        aadhar_input.send_keys(aadhar)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="maincontentid"]/app-link-aadhaar-status/div[1]/div/div[2]/form/div[2]/div/button[1]')))
        status_button = driver.find_element(By.XPATH, '//*[@id="maincontentid"]/app-link-aadhaar-status/div[1]/div/div[2]/form/div[2]/div/button[1]') 
        driver.execute_script("arguments[0].click();", status_button)

        wait.until(EC.presence_of_element_located((By.ID, 'linkAadhaarFailure_desc')))
        linkAadhaarFailure_desc = driver.find_element(By.ID, 'linkAadhaarFailure_desc')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="linkAadhaarFailure_desc"]/div/span')))
        span_element = linkAadhaarFailure_desc.find_element(By.XPATH, '//*[@id="linkAadhaarFailure_desc"]/div/span')

        print(span_element.get_attribute('innerHTML'))
        return span_element.get_attribute('innerHTML')

    finally:
        driver.quit()

check_adhar_pan('367670981561', 'CRRPG9924O')

