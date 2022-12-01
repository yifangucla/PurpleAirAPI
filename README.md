# PurpleAirAPI

The objective of the code provided in this repository is to download the data of Purple Air sensors using the new API system updated July 2022.
https://community.purpleair.com/t/new-version-of-the-purpleair-api-on-july-18th/1251

You can view the Purple Air sensors' map at https://map.purpleair.com/.

The repository includes code to download the sensors' list using API, and also download the historical data using API.

The official API guide of Purple Air sensor is at https://api.purpleair.com/.

In order to get your API keys, you need to contact Purple Air at contact@purpleair.com.
In order to download the historical data, you need to get your API key upgraded to have historical endpoint access.

To be noticed, the historical data PurpleAir provided is unorganized (the time and date will be disordered). 

Also, there is a time window limitation to download historical data for one call/one request.
Historical Endpoint Data Request Periods
Real-time: 2 days
10-minute : 3 days
30-minute: 7 days
1-hour: 14 days
6-hour: 90 days
1-day: 1 year

What's more, PurpleAir ask users to stay below or around 1000 requests daily.

If you have any question of how to use the code, please feel free to email me at fangyi@g.ucla.edu.
