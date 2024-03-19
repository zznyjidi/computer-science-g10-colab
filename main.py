#Group member: Qianyi, Zixuan, Chengyi, Tommy
#Date: Mar. 19, 2024
#Purpose: Create a program about the sky

def main():
    season, time_hour, time_minute, weather = inp()
    if season == "spring":
        

def inp():
    season = input("Season (lowercase): ")
    time_hour, time_minute = map(int, input("Enter the time (Hour[space]Minute): ").split())
    weather = input("Weather (sunny, cloudy, rainy, snowy):")
    return season, time_hour, time_minute, weather