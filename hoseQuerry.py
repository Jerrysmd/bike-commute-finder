# -*- coding: utf-8 -*-
import time

import requests

if __name__ == '__main__':
    key = ""
    types = "小区"
    city = "浦东新区"
    offset = 50
    keywords = '上海市'

    url = "https://restapi.amap.com/v3/place/text"

    for page in range(1000):
        params = {
            "key": key,
            "keywords": keywords,
            "city": city,
            "output": "json",
            "types": types,
            "offset": offset,
            "page": page
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            results = response.json()["pois"]
            for result in results:
                print(result["name"])
        else:
            print("请求失败")

        time.sleep(1)
