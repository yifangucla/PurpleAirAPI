# PurpleAirAPI

The objective of the code provided in this repository is to download the data of Purple Air sensors using the new API system.

You can view the Purple Air sensors' map at https://map.purpleair.com/.

The repository will include code to download the sensors' list using API, and also download the historical data using API.

The official API guide of Purple Air sensor is at https://api.purpleair.com/.

In order to get your API keys, you need to contact Purple Air at contact@purpleair.com.

To be noticed, the PurpleAir historical API is released as of July 18, 2022. For more information, view this post: https://community.purpleair.com/t/new-version-of-the-purpleair-api-on-july-18th/1251.

The historical API can currently only query one sensor at a time. You will need to collect the sensor indexes of the devices you want to query. You can use a latitude and longitude bounding box with the Get Sensors Data request to do so. Then, you will have to request the historical data for each device.

Also, the data from individual sensors will update no less than every 30 seconds. As a courtesy, The Purple Air ask that you limit the number of requests to no more than once every 1 to 10 minutes, assuming you are only using the API to obtain data from sensors. If retrieving data from multiple sensors at once, please send a single request rather than individual requests in succession.
