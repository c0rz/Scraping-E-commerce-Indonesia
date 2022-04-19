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
    shopee = json.loads(requests.get('https://shopee.co.id/api/v4/search/search_user?keyword=' +
                                     keywords+'&limit=1&offset='+str(i)+'&page=search_user&with_search_cover=true', headers=headers).text)
    toko = shopee['data']['users']
    for list in toko:
        nama_toko = list['shopname']
        id_toko = list['shopid']
        is_official_shop = list['is_official_shop']
        follower_count = list['follower_count']
        following_count = list['following_count']

        time.sleep(3)
        
        shop_info = json.loads(requests.get('https://shopee.co.id/api/v4/product/get_shop_info?shopid='+str(id_toko), headers=headers).text)
        shop_location = shop_info['data']['shop_location']
        rating_star = shop_info['data']['rating_star']
        place = shop_info['data']['place']
        print('['+str(penomoran)+'] ' + list['shopname'])
    penomoran = penomoran + 1
    
    # edit to csv
    list_toko.append([nama_toko, place, rating_star])
    time.sleep(3)

df = pd.DataFrame(list_toko, columns=['name', 'city', 'rating_star'])
df.to_csv(keywords+'.csv', index=False)
