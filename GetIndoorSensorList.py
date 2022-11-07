import requests

headers = {
    'authority': 'api.purpleair.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'referer': 'https://api.purpleair.com/',
    'sec-ch-ua': '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Yi Fang',
    'x-api-key': '791D694F-4A4F-11ED-B5AA-42010A800006',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'fields': 'sensor_index,latitude,longitude,location_type,position_rating,private,date_created,uptime',
}

response = requests.get('https://api.purpleair.com/v1/sensors',
                        params=params,
                        headers=headers)
content = response.json()
data = content['data']
fields = content['fields']
location_type_index = fields.index("location_type")
csv_file = open("./res.csv", mode="w", encoding="utf-8")
for item in data:
    if None in item or item[location_type_index] != 1:
        continue
    line = ",".join('%s' % i for i in item)
    csv_file.write(line)
    csv_file.write("\n")
csv_file.close()