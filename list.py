import bs4
import glob
import json

files = glob.glob("data/*.html")

files = sorted(files)

map = {}

for i in range(len(files)):

    file = files[i]

    print(i+1, len(files))

    soup = bs4.BeautifulSoup(open(file), 'html.parser')

    div = soup.find(class_="prevNextList")

    lis = div.find_all("li")

    for li in lis:
        a = li.find("a")

        if not a:
            continue

        text = a.text

        url = a.get("href")

        # print(text, url)

        map[text] = "https://japanknowledge.com" + url

with open('list.json', 'w') as f:
    json.dump(map, f, indent=4)