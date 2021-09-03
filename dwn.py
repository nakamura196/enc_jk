import os
import requests
import time

start = 1000
end = 92979000

for i in range(0, end):
    index = start + 5000 * i

    if i > end:
        break

    id = "42200SRFJ{}".format(str(index).zfill(8))
    url = "https://japanknowledge.com/lib/display/?lid=" + id

    path = "data/{}.html".format(id)

    if not os.path.exists(path):

        print(url)

        time.sleep(1)

        res = requests.get(url)

        with open(path, 'w') as file:
            file.write(res.text)