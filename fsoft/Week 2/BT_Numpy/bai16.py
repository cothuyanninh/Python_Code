from bs4 import BeautifulSoup
import requests
import numpy  as np

try:
	data = requests.get("https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_2018").content

except requests.exceptions.RequestException: 
	data = open("wiki.html", encoding = "utf8").read()

soup = BeautifulSoup(data, "html.parser")

title = soup.find_all("title")[0].get_text()
print(title)

td_tags = soup.find_all("td")
list_song = [td_tags[i].get_text()[1:-1] for i in range(0,200,2)]

# print("There are 100 song: \n", list_song)
number_listen = np.random.randint(100, 1001, 100)

list_name_number = list(zip(list_song, number_listen))
print("*"*20)
print("There are 100 song and numbers of listening: \n",list_name_number)

list_interested = [i for i in list_name_number if i[1] >= 800]
list_normal = [i for i in list_name_number if (i[1] < 800 and i[1] >= 500)]
list_not_interested = [i for i in list_name_number if i[1] < 500]

print("There are %d in list interested song."%len(list_interested))
print("There are %d in list normal song."%len(list_normal))
print("There are %d in list not interested song."%len(list_not_interested))

