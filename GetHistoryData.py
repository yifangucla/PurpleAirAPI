import datetime
import time
import pytz
import requests
import pandas


def get_time(t):
    tz = pytz.timezone("America/Los_Angeles")
    t = datetime.datetime.strptime(t, '%Y-%m-%d %H:%M:%S')
    date = datetime.datetime(t.year, t.month, t.day, t.hour, t.minute, t.second, tzinfo=tz)
    # Transfer to time stamp
    return date.timestamp()


headers = {
    'authority': 'api.purpleair.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'referer': 'https://api.purpleair.com/',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Yi Fang Laptop',
    #Unique API key granted for historical data
    'x-api-key': '791D694F-4A4F-11ED-B5AA-42010A800006',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'average': '60',
    'fields': 'temperature,humidity',
    'start_timestamp': str(get_time("2019-08-01 00:00:00")),
    'end_timestamp': str(get_time("2019-08-14 00:00:00")),
}

# Read the CSV file with sensor index
df = pandas.read_csv("./LA_PAlist_PR5_LT0_2019.csv")
# Read sensor_ind
sensor_index = df["sensor_ind"].values
csv_file = open("./res.csv", mode="w", encoding="utf-8")
# Request for historical data
for index in sensor_index:
    try:
        response = requests.get(f'https://api.purpleair.com/v1/sensors/{str(index)}/history',
                                params=params, headers=headers)
        print(f"Downloading sensor index: {index} ")
        content = response.json()
        data = content["data"]
        fields = content['fields']
        for item in data:
            if None in item or len(item) != len(fields):
                continue
            # Add index info to the data
            # timeValue = time.localtime()
            tz = pytz.timezone('America/Los_Angeles')
            dt = pytz.datetime.datetime.fromtimestamp(item[0], tz)
            item[0] = dt.strftime('%Y-%m-%d %H:%M:%S')
            item.insert(0, index)
            line = ",".join('%s' % i for i in item)
            csv_file.write(line)
            csv_file.write("\n")
    except Exception as e:
        print()

csv_file.close()
