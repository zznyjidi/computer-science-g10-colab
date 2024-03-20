#Group member: Qianyi, Zixuan, Chengyi, Tommy
#Date: Mar. 19, 2024
#Purpose: Mystery Madness Code 2 - Doc 1 - Create a program about the sky
        #Check if you can currently see stars
import urllib.request, urllib.error, json

#weather = 

def main():
    #global weather
    season, time_hour, weather = inp()
    if season == "spring":
        if time_hour >= 19 or time_hour <= 7:
            istime = True
            if weather == "sunny":
                isweather = True
            else:
                isweather = False
        else:
            istime = False
    elif season == "summer":
        if time_hour >= 20 or time_hour <= 5:
            istime = True
            if weather == "sunny":
                isweather = True
            else:
                isweather = False
        else:
            istime = False
    elif season == "autumn" or season == "fall":
        istime = True
        if time_hour >= 19 or time_hour <= 7:
            if weather == "sunny":
                isweather = True
            else:
                isweather = False
        else:
            istime = False
    elif season == "winter":
        istime = True
        if time_hour >= 17 or time_hour <= 8:
            if weather == "sunny":
                isweather = True
            else:
                isweather = False
        else:
            istime = False
    else:
        print("N/A")

    if istime and isweather:
        yes()
    elif not istime:
        no_time()
    else:
        no_weather()

def inp():
    season = input("Season (lowercase): ")
    time_hour, time_minute = map(int, input("Enter the time (Hours[space]Minute)(24hours): ").split())
    weather = input("Weather: ")
    return season, time_hour, weather

def getWeather_JSON():
    location = "Markham,CA"
    API_KEY = "PMHF3BX9NP3BNHDT7BYA2X6Y5"
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