# -*- coding: utf-8 -*-
import requests

if __name__ == '__main__':

    # 高德地图开发者密钥
    key = '1abe0c950a951d862f3bae917bb6f971'

    # 起点地址（小区）
    origin = '上海市中新家园'

    # 终点地址（地铁站）
    destination = '上海市马当路地铁站'


    # 获取起点和终点的经纬度
    def get_location(address):
        url = 'https://restapi.amap.com/v3/geocode/geo'
        params = {
            'key': key,
            'address': address,
        }
        response = requests.get(url, params=params)
        result = response.json()
        if result['status'] == '1' and len(result['geocodes']) > 0:
            location = result['geocodes'][0]['location']
            return location
        return None


    # 获取起点和终点的经纬度
    origin_location = get_location(origin)
    destination_location = get_location(destination)

    if origin_location is None:
        print('获取小区经纬度失败')
    elif destination_location is None:
        print('获取地铁站经纬度失败')
    else:
        # 调用骑行路径规划接口
        url = 'https://restapi.amap.com/v4/direction/bicycling'
        params = {
            'key': key,
            'origin': origin_location,
            'destination': destination_location,
        }
        response = requests.get(url, params=params)
        result = response.json()
        if result['errmsg'] == 'OK':
            path = result['data']['paths'][0]
            distance = path['distance']
            duration = path['duration']
            print('从{}到{}的骑行时间为{}分钟'.format(origin, destination, duration // 60))
        else:
            print('骑行路径规划失败')
