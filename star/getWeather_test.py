import urllib.request, urllib.error, json


location = "Markham,CA"
API_KEY = "PMHF3BX9NP3BNHDT7BYA2X6Y5"

def getSunData_JSON():
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?unitGroup=us&key={API_KEY}&include=days&elements=datetime,sunrise,sunset"
    request = urllib.request.Request(url,method="GET")
    try:
        with urllib.request.urlopen(request) as response:
            sunStatus = response.read().decode(response.headers.get_content_charset("utf-8"))
    except urllib.error.HTTPError as error:
        print("Check your Internet Connection and the API Server! ")
        exit()
    return json.loads(sunStatus)

def getSunData(day_offset):
    sunStatus = getSunData_JSON()
    day = sunStatus["days"][day_offset]
    sunrise = str(day["sunrise"]).split(":")
    sunset = str(day["sunset"]).split(":")
    return sunrise, sunset

def getWeather_JSON():
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/?key={API_KEY}"
    request = urllib.request.Request(url,method="GET")
    try:
        with urllib.request.urlopen(request) as response:
            weather = response.read().decode(response.headers.get_content_charset("utf-8"))
    except urllib.error.HTTPError as error:
        print("Check your Internet Connection and the API Server! ")
        exit()
    return json.loads(weather)

# Get weather of Markham
# Usage: 
# @para day_offset: the day to get weather, 0 means today
def getWeather(day_offset):
    weather = getWeather_JSON()
    day = weather["days"][day_offset]["preciptype"]
    return day

weather = getWeather_JSON()
day = weather["days"]
print(len(day))
