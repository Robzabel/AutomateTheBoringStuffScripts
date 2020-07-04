#! /usr/bin/python3
#fire up a browser and go to a page
from selenium import webdriver
browser = webdriver.Firefox() #make firefox the browser of choice
browser.get('https://automatetheboringstuff.com') # browse to the web page
element = browser.find_element_by_css_selector('.main > div:nth-child(1) > ul:nth-child(20) > li:nth-child(1) > a:nth-child(1)')
element.click() # this enables you to click on stuff
#change the webpage and use a search box
browser.get('https://www.nisbets.co.uk/') #chnge the webpage to one with a search field
searchBox = browser.find_element_by_css_selector('.col-md-7 > div:nth-child(1) > form:nth-child(1) > div:nth-child(1)')#find the search field on the page
searchBox.click()#click to enter the text
searchBox = browser.find_element_by_css_selector('.col-md-7 > div:nth-child(1) > form:nth-child(1) > div:nth-child(1) > input:nth-child(1)')#find the element on the page that is ready to accept the text
searchBox.send_keys('mens shoes')#enter the search criteria
searchBox.submit()#submit search
#control the browser
browser.back()
browser.forward()
browser.refresh()
#browser.quit()
#read the web page
browser.get('https://automatetheboringstuff.com')
elem = browser.find_element_by_css_selector('.main > div:nth-child(1) > p:nth-child(8)')
print(elem.text)
