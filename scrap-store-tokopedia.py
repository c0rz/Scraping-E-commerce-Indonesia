import requests
import pandas as pd
import json
import time



headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36 OPR/58.0.3135.79'}

list_toko = []

keywords = input("Masukan keywords: ")
total = input("Masukan Jumlah: ")

penomoran = 1

for i in range(1, int(total)+1):
    tokopedia = json.loads(requests.get('https://ace.tokopedia.com/search/v1/shop?device=dekstop&q=' +
                           keywords+'&rows=1&source=search&start='+str(i), headers=headers).text)
    toko = tokopedia['data']
    for list in toko:
        print('['+str(penomoran)+'] ' + list['name'])
        penomoran = penomoran + 1
        list_toko.append([list['name'], list['city'], list['rating']['rate_accuracy'],  list['rating']['total_tx'],
                         list['rating']['reputation_score'], list['rating']['rate_cancel'], list['is_official']])
        time.sleep(3)

df = pd.DataFrame(list_toko, columns=['name', 'city', 'rate_accuracy', 'total_tx',
                  'reputation_score', 'rate_cancel', 'is_official'])
df.to_csv(keywords+'.csv', index=False)
