from selenium import webdriver
import time
import requests
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get('https://www.thesparksfoundationsingapore.org/')

print("TestCase #1:")
if(driver.title):
    print("Title Verification Successful!\n",driver.title)
else:
    print("Title Verification Failed!\n")

print("TestCase #2:")
try:
    driver.find_elements_by_tag_name('img')
    print("Image is present!\n")
except NoSuchElementException:
    print("Image is not present!\n")

print("TestCase #3:")
try:
    driver.find_element_by_partial_link_text("The Sparks Foundation").click()
    print("Home link works!\n")
except NoSuchElementException:
    print("Home Link Doesn't Work!\n")

print("TestCase #4:")
try:
    driver.find_element_by_class_name("navbar")
    print("Navbar Verification Successful!\n")
except NoSuchElementException:
    print("Navbar Verification Failed!\n")

print("TestCase #5:")
try:
    driver.find_element_by_link_text('About Us').click()
    time.sleep(3)
    driver.find_element_by_link_text('Vision, Mission and Values').click()
    time.sleep(3)
    print('Page visited Successfully!\n')
except NoSuchElementException:
    print("Page visit Failed! Does not exist.\n")
    time.sleep(3)

print("TestCase #6:")
try:
    driver.find_element_by_xpath("//span")
    time.sleep(3)
    print('Page visited Successfully!\n')
except NoSuchElementException:
    print("Page visit Failed! Does not exist.\n")
    time.sleep(3)

print("TestCase #7:")
try:
    driver.find_element_by_link_text('About Us').click()
    time.sleep(3)
    driver.find_element_by_link_text('Guiding Principles').click()
    print('Page visited Successfully!\n')
except NoSuchElementException:
    print("Page visit Failed! Does not exist.\n")
    time.sleep(3)

print("TestCase #8:")
try:
    driver.find_element_by_link_text('About Us').click()
    time.sleep(3)
    driver.find_element_by_link_text('Guiding Principles').click()

    elems = driver.find_elements_by_tag_name('h4')
    for i in range(0,len(elems)-1):
        print(elems[i].text)
    print('Page visited Successfully!\n')
except NoSuchElementException:
    print("Page visit Failed! Does not exist.\n")
    time.sleep(3)

print('TestCase #9:')
try:
    driver.find_element_by_link_text('Policies and Code').click()
    time.sleep(3)
    driver.find_element_by_link_text("Policies").click()
    time.sleep(3)
    print('Policy page exists. Success!\n')
except NoSuchElementException:
    print('Policy Page Does not exist. Failed!\n')
    time.sleep(3)

print('TestCase #10:')
try:
    driver.find_element_by_link_text('Programs').click()
    time.sleep(3)
    driver.find_element_by_link_text("Workshops").click()
    time.sleep(3)
    driver.find_element_by_link_text('LEARN MORE').click()
    time.sleep(3)
    print('Workshop Page Verified!\n')
except NoSuchElementException:
    print('No New Tab opened. Failed!\n')

print("TestCase #11")
try:
    driver.find_element_by_link_text('LINKS').click()
    time.sleep(3)
    driver.find_element_by_link_text('Software & App').click()
    time.sleep(3)
    print('LINKS Verfication successful!\n')
except NoSuchElementException:
    print("LINKS Verification Failed!\n")

print('TestCase #12:')
try:
    driver.find_element_by_xpath('//*[@id="home"]/div/div[1]/h1/a/*').click()
    print('Found Logo! Success!\n')
    time.sleep(3)
except NoSuchElementException:
    print('No logo found!\n')

print("TestCase #13:")
try:
    driver.find_element_by_link_text('Join Us').click()
    time.sleep(3)
    driver.find_element_by_link_text('Why Join Us').click()
    time.sleep(3)

    driver.find_element_by_class_name('button-w3layouts').click()
    time.sleep(3)
    print("Form Verification Successful!\n")
    time.sleep(3)
except NoSuchElementException:
    print("Form Verification Failed!\n")
    time.sleep(3)

print("TestCase #14:")
try:
    driver.find_element_by_link_text("Contact Us").click()
    time.sleep(1)
    info = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[2]/p[2]')
    time.sleep(1)
    print(info.text)
    print()
    info1 = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/p')
    time.sleep(1)
    print(info1.text)
    print()
    info2 = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/p/span/a')
    time.sleep(1)
    print(info2.text)
    print()
    print("Contact Page Verification Sucessful!\n")
except NoSuchElementException:
    print("Contact Page Verification unsuccessful!")

print("TestCase #15:")
try:
    driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/ul/li[1]/a").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/ul/li[2]/a").click()
    
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/ul/li[3]/a").click()
    
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/ul/li[4]/a").click()
    
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/ul/li[5]/a").click()
    
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/ul/li[6]/a").click()
    
    time.sleep(1)
    print()
    print("Contact Page Verification Sucessful!\n")
except NoSuchElementException:
    print("Contact Page Verification unsuccessful!")


print("TestCase #16:")

try:
    driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/ul/li[1]/a").click()
    
    print("Jobs at Angel.co Portal page:- Success\n")
    time.sleep(8)
except NoSuchElementException:
    print("Contact Page Verification unsuccessful!")