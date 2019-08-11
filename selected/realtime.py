from selenium import webdriver
import time
import os
import cv2
from PIL import Image
import extcolors as ji

"""Save a screenshot from spotify.com in current directory"""
chromedriver = "C:/Users/Pooja/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"]=chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get('https://www.incois.gov.in/portal/osf/osfCoastal.jsp?region=coastal&area=westbengal&param=swh&ln=en')
screenshot = driver.save_screenshot("my_screenshot1.png")
driver.quit()

im = Image.open('my_screenshot1.png')

outfile = "result.jpg"

region = im.crop((500, 350, 900, 900))
region.save(outfile, "png")
colors, pixel_count = ji.extract(outfile)
for x in colors:
    if ((x[0][0] == 246 and x[0][1] == 157 and x[0][2] == 73) or (
        x[0][0] == 213 and x[0][1] == 254 and x[0][2] == 160) or (
        x[0][0] == 249 and x[0][1] == 219 and x[0][2] == 105) or (
        x[0][0] == 247 and x[0][1] == 220 and x[0][2] == 105)):
        print('alert there')
    else:
        print('No Alert!')
        break


