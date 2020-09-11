from selenium import webdriver
import time

# export PATH=$PATH:/path/to/directory/of/executable/downloaded/in/previous/step
#Run this command first
# export PATH=$PATH:"/media/sadman/Windows-10/Ddrive/Python - Datasets/Web Page Refresh"

count = 0
refreshrate=5
driver=webdriver.Firefox()
driver.get('https://www.youtube.com/watch?v=IHHQm4MeoV0')
driver.find_element_by_id("player-container").click()
time.sleep(refreshrate)

while count < 10:
	time.sleep(refreshrate)
	driver.refresh()
	driver.find_element_by_id("player-container").click()

	count += 1















