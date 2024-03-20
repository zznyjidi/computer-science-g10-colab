import urllib.request, urllib.error, json

def getWeather_JSON():
    location = "Markham,CA"
    API_KEY = ""
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/?key={API_KEY}"
    request = urllib.request.Request(url,method="GET")
    try:
        with urllib.request.urlopen(request) as response:
            weather = response.read().decode(response.headers.get_content_charset("utf-8"))
    except urllib.error.HTTPError as error:
        print("Check your Internet Connection and the API Server! ")
        exit()
    return json.loads(weather)

def getWeather(day_offset):
    weather = getWeather_JSON()
    day = weather["days"][day_offset]["preciptype"]
    return day
    

print(*getWeather(0))
