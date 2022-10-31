from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen

url = 'https://www.dailyscript.com/scripts/abyss.html'

html_text = urlopen(url)

soup = BeautifulSoup(html_text, 'lxml')

save_file = open("/home/athoillah/Downloads/Data Engineering_DigitalSkola/Homework/MapReduce/The-Abyss-Script.txt", "w")
save_file.write(soup.get_text())
save_file.close()