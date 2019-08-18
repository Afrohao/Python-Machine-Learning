import requests
api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
Sapporo={'city' : '016010'}
Sendai={'city' : '040010'}
Tokyo={'city' : '130010'}
Osaka={'city' : '270000'}
Fukuoka={'city' : '400010'}

S='札幌'
Se='仙台'
T='東京'
O='大阪'
F='福岡'

city_list=[Sapporo, Sendai, Tokyo, Osaka, Fukuoka]
city=[S, Se, T, O, F]

while 1:
    print('城市代碼','1: 札幌','2: 仙台','3: 東京','4: 大阪 ','5: 福岡')
    print('請輸入欲查詢城市之代碼:')
    index=eval(input())
    weather_data = requests.get(api_url, params = city_list[index-1]).json()
    print(city[index-1],'的天氣是：')
    for weather in weather_data['forecasts']:
#       print(' ')
        print('日期 : '+ weather['date'])
        print(weather['dateLabel'] + '的天氣是' + weather['telop'])
        print(' ')
#http://weather.livedoor.com/weather_hacks/webservice -->api
