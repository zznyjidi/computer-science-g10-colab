#Group member: Qianyi, Zixuan, Chengyi, Tommy
#Date: Mar. 19, 2024
#Purpose: Mystery Madness Code 2 - Doc 1 - Create a program about the sky
        #Check if you can currently see stars
import urllib.request, urllib.error, json

location = "Markham,CA"
API_KEY = "PMHF3BX9NP3BNHDT7BYA2X6Y5"

def main():
    global location, API_KEY
    sunrise, sunset, time_hour, time_min, weather = inp()

    if ((time_hour >= sunset[0]) or (time_hour <= sunrise[0])) and ((time_min >= sunset[1]) or (time_min <= sunrise[1])):
        istime = True
        if weather == "sunny":
            isweather = True
        else:
            isweather = False
    else:
        istime = False


    if istime and isweather:
        yes()
    elif not istime:
        no_time()
    else:
        no_weather()

def inp():
#   season = input("Season (lowercase): ")

    time_hour, time_minute = map(int, input("Enter the time (Hours:Minute)(24hours): ").split(":"))
    offset = int(input("Which day will you go (0 means today, 14 max): "))
#   weather = input("Weather: ")
    weather = getWeather(offset)
    sunrise, sunset = getSunData(offset)
    return sunrise, sunset, time_hour, time_minute, weather

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
    return list(map(int, sunrise)), list(map(int, sunset))

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

def no_weather():
    print("There are no visible stars in the sky...\nFind a better weather")
def no_time():
    print("There are no visible stars in the sky...\n" + "Wait for the sunset... ")
def yes():
    print("There are visible stars in the sky! ")

main()
#zznyjidi出品