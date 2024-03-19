#Group member: Qianyi, Zixuan, Chengyi, Tommy
#Date: Mar. 19, 2024
#Purpose: Create a program about the sky

def main():
    season, time_hour, time_minute, weather = inp()
    if season == "spring":
        if 19 >= time_hour and time_hour <= 7:
            if weather == "sunny":
                yes()
            else:
                no()
        else:
            

def inp():
    season = input("Season (lowercase): ")
    time_hour, time_minute = map(int, input("Enter the time (Hour[space]Minute)(24hours): ").split())
    weather = input("Weather (sunny, cloudy, rainy, snowy):")
    return season, time_hour, time_minute, weather

def no():
    print("There are no visible stars in the sky... ")
def yes():
    print("There are visible stars in the sky! ")